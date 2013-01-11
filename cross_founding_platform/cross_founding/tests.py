from django.test import TestCase
from cross_founding_platform.cross_founding.models import Backer

class BackerTestCase(TestCase):
    def setUp(self):
        self.foo = Backer.objects.create(
            username = "joedoe",
            first_name = "Joe",
            last_name = "Doe",
            email = "joe@example.com",
            password = "secret",
            dob_at = "1980-01-01",
            is_staff = "1",
            is_active = "1",
            is_superuser = "0",
            location = "NY"
        )
        self.bar = Backer.objects.create(
            username = "janedoe",
            first_name = "Jane",
            last_name = "Doe",
            email = "jane@example.com",
            password = "secret",
            dob_at = "1980-01-01",
            is_staff = "1",
            is_active = "1",
            is_superuser = "0",
            location = "NY"
        )

    def test_should_create_table_with_corresponding_fields(self):
        self.assertEqual(self.foo.username, "joedoe")
        self.assertEqual(self.foo.first_name, "Joe")
        self.assertEqual(self.foo.last_name, "Doe")
        self.assertEqual(self.foo.email, "joe@example.com")
        self.assertEqual(self.foo.password, "secret")
        self.assertEqual(self.foo.dob_at, "1980-01-01")
        self.assertEqual(self.foo.is_staff, "1")
        self.assertEqual(self.foo.is_active, "1")
        self.assertEqual(self.foo.is_superuser, "0")
        self.assertEqual(self.foo.location, "NY")

    def test_should_unique_username(self):
        pass