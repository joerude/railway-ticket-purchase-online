from rest_framework.reverse import reverse
from django.urls import resolve


class TestUrls:
    def test_test_token_url(self):
        url = reverse("accounts:login")
        assert resolve(url).view_name == "accounts:login"

    def test_token_refresh_url(self):
        url = reverse("accounts:token-refresh")
        assert resolve(url).view_name == "accounts:token-refresh"

    def test_token_verify_url(self):
        url = reverse("accounts:token-verify")
        assert resolve(url).view_name == "accounts:token-verify"
