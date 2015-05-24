from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Deletes all financial records, graduates all generations, " \
           "and resets all customs permissions. Camper records are kept" \
           "for the convinience of not having to enter them again."

    def handle(self, *args, **options):
        from logistics.choices import GENERATIONS
        from logistics.models import SmallGroup
        from signup.models import Payment, Guest, Parent
        from finances.models import Transaction

        self.stdout.write("Deleting financial records")
        Payment.objects.all().delete()
        Transaction.objects.all().delete()
        self.stdout.write("All financial records deleted")

        self.stdout.write("Deleting Guests")
        Guest.objects.all().delete()
        self.stdout.write("All Guests deleted")

        self.stdout.write("Graduating generations")
        last_generation = GENERATIONS[-1][0]
        for group in SmallGroup.objects.all():
            if group.generation == last_generation:
                group.delete()
            else:
                group.generation += 1
                group.save()
                group.camper_set.update(
                    balance=0, no_pay=False, permission_status=0,
                    signed_up=False)
                group.counselor.balance = 0
                group.counselor.no_pay = False
                group.counselor.save()
        self.stdout.write("All generations graduated successfully")

        self.stdout.write("Deleting Parents without Children")
        Parent.objects.filter(mothered=None, fathered=None).delete()
        self.stdout.write("All left-over Parents deleted")
