from django.test import TestCase

from model_bakery import baker, seq


class AccountTest(TestCase):
    def test_account_list(self):
        cur = baker.make_recipe("accounts.tests.curator", _quantity=3)

        assert len(cur) == 3
