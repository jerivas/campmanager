import pytest
from ddf import G
from django.contrib.auth import get_user_model
from django.test.testcases import SimpleTestCase
from django_functest import FuncWebTestMixin

from general.models import Camp
from utils.urls import admin_url as _admin_url

User = get_user_model()


class FuncWebTest(FuncWebTestMixin, SimpleTestCase):
    pass


@pytest.fixture
def client():
    """
    Enhanced test client for classic Django views and the admin
    https://django-functest.readthedocs.io/en/latest/common.html
    https://github.com/django-webtest/django-webtest/blob/master/django_webtest/pytest_plugin.py
    """
    user = G(User, is_staff=True, is_superuser=True)
    client = FuncWebTest()
    client._patch_settings()
    client.renew_app()
    client.app.set_user(user)
    client.user = user
    yield client
    client._unpatch_settings()


@pytest.fixture
def camp():
    camp = Camp.get_solo()
    yield camp
    camp.clear_cache()


@pytest.fixture(scope="session")
def admin_url():
    return _admin_url


@pytest.fixture(scope="session")
def result_count():
    """
    Count the number of items matching a selector.
    By default counts results in the Django admin changelist.
    """

    def _count(response, selector="#result_list tbody tr"):
        return len(response.html.select(selector))

    return _count
