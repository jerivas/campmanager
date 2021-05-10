from django.core.management.base import BaseCommand

from signup.models import Counselor


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
        campers = Camper.objects.filter(
            signed_up=False, permission_status=Camper.INCOMPLETE
        )
        camper_count, _ = campers.delete()
        self.stdout.write(f"Deleted {camper_count} Campers")

        self.stdout.write("Deleting financial records")
        payment_count, _ = Payment.objects.all().delete()
        transaction_count, _ = Transaction.objects.all().delete()
        self.stdout.write(f"Deleted {payment_count} Payments")
        self.stdout.write(f"Deleted {transaction_count} Transactions")

        self.stdout.write("Deleting Guests")
        guest_count, _ = Guest.objects.all().delete()
        self.stdout.write(f"Deleted {guest_count} Guests")

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
            try:
                group.counselor.has_gov_id = False
                group.counselor.save()
            except Counselor.DoesNotExist:
                pass
        self.stdout.write("All small groups have been reset")

        self.stdout.write("Deleting Parents without children in record")
        parent_count, _ = Parent.objects.filter(mothered=None, fathered=None).delete()
        self.stdout.write(f"Deleted {parent_count} Parents")
