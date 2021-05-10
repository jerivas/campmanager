import pytest
from django.contrib.auth import get_user_model
from django.core.management import call_command
from django_dynamic_fixture import G

from finances.models import Transaction
from logistics.choices import GENERATIONS
from logistics.models import SmallGroup
from signup.models import Camper, Counselor, Guest, Parent, Payment

User = get_user_model()


@pytest.mark.django_db
class TestNewCamp:
    def test_delete_records(self, camp):
        camp.signup_fee = 5
        camp.save()

        dad = G(Parent)
        camper = G(
            Camper,
            balance=50,
            signed_up=True,
            permission_status=Camper.PRINTED,
            fined=True,
            has_medical_record=True,
            father=dad,
        )
        G(Payment, content_object=camper)
        G(Camper, permission_status=Camper.INCOMPLETE, n=10)
        G(Parent, fathered=None, mothered=None, n=10)
        G(Transaction, n=10)
        G(Guest, n=10)
        counselor_count = Counselor.objects.update(
            balance=50,
            signed_up=True,
            fined=True,
            has_gov_id=True,
            has_medical_record=True,
        )
        assert counselor_count > 0, "Create some counselors to test"

        call_command("newcamp")

        assert Parent.objects.get().pk == dad.pk
        assert Camper.objects.get().pk == camper.pk
        camper.refresh_from_db()
        assert camper.balance == 0
        assert camper.permission_status == Camper.INCOMPLETE
        assert not camper.no_pay
        assert not camper.signed_up
        assert not camper.fined
        assert not camper.has_medical_record

        assert not Payment.objects.exists()
        assert not Transaction.objects.exists()
        assert not Guest.objects.exists()

        assert Counselor.objects.exists()
        assert not Counselor.objects.filter(balance__gt=0).exists()
        assert not Counselor.objects.filter(signed_up=True).exists()
        assert not Counselor.objects.filter(fined=True).exists()
        assert not Counselor.objects.filter(has_gov_id=True).exists()
        assert not Counselor.objects.filter(has_medical_record=True).exists()

    def test_update_small_groups(self):
        for generation, _ in GENERATIONS:
            G(SmallGroup, generation=generation, cabin="cabin", bus="bus")
        assert SmallGroup.objects.exists()

        call_command("newcamp")

        assert SmallGroup.objects.exists()
        assert not SmallGroup.objects.filter(
            generation=GENERATIONS[0][0]
        ).exists(), "First generation groups should not exist"
        assert not SmallGroup.objects.exclude(cabin="").exists()
        assert not SmallGroup.objects.exclude(bus="").exists()
