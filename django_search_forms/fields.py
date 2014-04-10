import re
from collections import namedtuple

from django import forms
from django.db.models import Q


QUOTATION_MARKS = re.compile(r'^"(.+)"$')


Search = namedtuple('Search', ['is_exact', 'string'])


class TextSearchField(forms.CharField):
    """This field converts data from the form into a Q object."""


    def __init__(self, *args, **kwargs):
        kwargs['required'] = False
        super(TextSearchField, self).__init__(*args, **kwargs)

    def _parse_search(self, value):
        """Parses the search string."""
        match = QUOTATION_MARKS.match(value)
        if match is None:
            return Search(is_exact=False, string=value)
        else:
            return Search(is_exact=True, string=match.group(1))


    def clean(self, value):
        value = super(TextSearchField, self).clean(value)
        search = self._parse_search(value)
        if search.is_exact:
            return Q(**{self.name: search.string})
        else:
            return Q(**{self.name + '__icontains': search.string})
