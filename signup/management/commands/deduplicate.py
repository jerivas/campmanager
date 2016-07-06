# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Attempts to find duplicates in signup records."

    def handle(self, *args, **kwargs):
        from ...models import Camper, Counselor

        campers = Camper.objects.all()

        for camper in campers:
            # Check for similar Campers
            filters = {
                "first_name__unaccent__icontains": camper.first_name,
                "first_surname__unaccent__icontains": camper.first_surname,
            }
            if campers.filter(**filters).exclude(pk=camper.pk):
                self.stdout.write("Duplicate camper: %s" % camper)

            # Check for Campers added as Counselors
            filters.update({"small_group_id": camper.small_group_id})
            if Counselor.objects.filter(**filters):
                self.stdout.write("Counselor added as camper: %s" % camper)
