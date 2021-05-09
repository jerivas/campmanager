import pytest
from ddf import G
from django.urls import reverse
from django.utils.dateparse import parse_datetime
from django.utils.timezone import now

from conftest import FuncWebTest
from finances.models import Transaction


@pytest.mark.django_db
class TestTransactionAdmin:
    def test_list(self, client: FuncWebTest, admin_url, result_count):
        G(Transaction, n=2)
        client.get_literal_url(admin_url(Transaction, "changelist"))
        assert result_count(client.last_response) == 2

    def test_list__actions(self, client: FuncWebTest, admin_url):
        client.get_literal_url(admin_url(Transaction, "changelist"))
        assert client.is_element_present(f"[href='{reverse('finances_report')}']")

    def test_create(self, client: FuncWebTest, admin_url):
        client.get_literal_url(admin_url(Transaction, "add"))
        client.fill_by_name(
            {
                "transaction_id": "11",
                "transaction_type": "income",
                "transaction_date": "2021-05-09",
                "amount": "33",
                "origin": "Origin XYZ",
                "destination": "Destination ABC",
            }
        )

        client.submit("[name='_save']")
        transaction = Transaction.objects.get()
        assert transaction.transaction_id == "11"
        assert transaction.transaction_type == "income"
        assert str(transaction.transaction_date) == "2021-05-09"
        assert transaction.amount == 33
        assert transaction.origin == "Origin XYZ"
        assert transaction.destination == "Destination ABC"

    def test_create__initial_date(self, client: FuncWebTest, admin_url):
        client.get_literal_url(admin_url(Transaction, "add"))
        initial_date = parse_datetime(
            client.value("[name='initial-transaction_date']")
        ).date()
        assert initial_date == now().date()

    def test_update(self, client: FuncWebTest, admin_url):
        transaction = G(Transaction, amount=20)
        client.get_literal_url(admin_url(Transaction, "change", transaction.pk))
        client.fill_by_name({"amount": "40"})
        client.submit("[name='_save']")

        transaction.refresh_from_db()
        assert transaction.amount == 40
