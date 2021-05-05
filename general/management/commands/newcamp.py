from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = (
        "Deletes all financial records, resets all small groups, "
        "and customs information. Camper records are kept"
        "for the convenience of not having to enter them again."
    )

    def handle(self, *args, **options):
        from finances.models import Transaction
        from logistics.choices import GENERATIONS
        from logistics.models import SmallGroup
        from signup.models import Camper, Guest, Parent, Payment

        self.stdout.write("Deleting Campers that didn't sign up")
        filters = {"signed_up": False, "permission_status": Camper.INCOMPLETE}
        campers = Camper.objects.filter(**filters).delete()
        self.stdout.write("Deleted %s Campers" % campers[0])

        self.stdout.write("Deleting financial records")
        Payment.objects.all().delete()
        Transaction.objects.all().delete()
        self.stdout.write("All financial records deleted")

        self.stdout.write("Deleting Guests")
        Guest.objects.all().delete()
        self.stdout.write("All Guests deleted")

        self.stdout.write("Resseting small groups")
        last_generation = GENERATIONS[-1][0]
        for group in SmallGroup.objects.all():
            if group.generation != last_generation:
                group.generation += 1
            group.cabin = group.bus = ""
            group.save()
            reset_fields = {
                "balance": 0,
                "no_pay": False,
                "signed_up": False,
                "permission_status": Camper.INCOMPLETE,
                "fined": False,
                "has_medical_record": False,
            }
            group.camper_set.update(**reset_fields)
            for field, value in reset_fields.items():
                try:
                    setattr(group.counselor, field, value)
                except AttributeError:
                    pass
            group.counselor.has_gov_id = False
            group.counselor.save()
        self.stdout.write("All small groups have been reset")

        self.stdout.write("Deleting Parents without children in record")
        parents = Parent.objects.filter(mothered=None, fathered=None).delete()
        self.stdout.write("Deleted %s parents" % parents[0])
