from __future__ import unicode_literals

import operator
from functools import reduce

from django.db.models import Q


# FIXME: Workaround for https://code.djangoproject.com/ticket/26184
#        Remove when fixed.
def lookup_needs_distinct(opts, lookup_path):
    """
    Returns True if 'distinct()' should be used to query the given lookup path.
    """
    field = None
    # Go through the fields (following all relations) and look for an m2m
    for lookup_part in lookup_path.split("__"):
        if field is not None:
            # Checks whether the current lookup part is not a field.
            try:
                if (
                    field.get_transform(lookup_part) is not None
                    or field.get_lookup(lookup_part) is not None
                ):
                    continue
            except (NotImplementedError, TypeError):
                continue
        field = opts.get_field(lookup_part)
        if hasattr(field, "get_path_info"):
            # This field is a relation, update opts to follow the relation
            path_info = field.get_path_info()
            opts = path_info[-1].to_opts
            if any(path.m2m for path in path_info):
                # This field is a m2m relation so we know we need to call distinct
                return True
    return False


class UnaccentSearchMixin(object):
    """
    Performs admin searches using Postgres unaccent transformation.
    https://github.com/dezede/dezede/commit/5e8be29ef4f24ea016a78a5d78085e222bca79b3
    """

    def get_search_results(self, request, queryset, search_term):
        # FIXME: What follows is a copy of the original get_search_results.
        #        It is a workaround to https://code.djangoproject.com/ticket/26184
        #        Remove when fixed.

        def construct_search(field_name):
            if field_name.startswith("^"):
                return "%s__istartswith" % field_name[1:]
            elif field_name.startswith("="):
                return "%s__iexact" % field_name[1:]
            elif field_name.startswith("@"):
                return "%s__search" % field_name[1:]
            else:
                return "%s__icontains" % field_name

        use_distinct = False
        search_fields = self.get_search_fields(request)
        if search_fields and search_term:
            orm_lookups = [
                construct_search(str(search_field)) for search_field in search_fields
            ]
            for bit in search_term.split():
                or_queries = [Q(**{orm_lookup: bit}) for orm_lookup in orm_lookups]
                queryset = queryset.filter(reduce(operator.or_, or_queries))
            if not use_distinct:
                for search_spec in orm_lookups:
                    if lookup_needs_distinct(self.opts, search_spec):
                        use_distinct = True
                        break

        return queryset, use_distinct
