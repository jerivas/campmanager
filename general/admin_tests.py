import pytest

from conftest import FuncWebTest
from general.models import Camp


@pytest.mark.django_db
def test_camp_title(client: FuncWebTest, camp: Camp):
    # Expect the camp title to appear in all admin pages
    camp.title = "Testing Camp 2021"
    camp.save()

    # Admin home
    response = client.get_url("admin:index")
    assert "Testing Camp 2021" in response.html.find("title").string
    assert "Testing Camp 2021" in response.html.select("#grp-admin-title")[0].string

    # User list
    response = client.get_url("admin:auth_user_changelist")
    assert "Testing Camp 2021" in response.html.find("title").string
    assert "Testing Camp 2021" in response.html.select("#grp-admin-title")[0].string
