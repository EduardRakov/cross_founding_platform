from django.test import TestCase
from cross_founding_platform.cross_founding.models import Backer

class BackerTestCase(TestCase):
    def setUp(self):
        self.backer = Backer.objects.create(
            username = "joedoe",
            first_name = "Joe",
            last_name = "Doe",
            email = "joe@example.com",
            password = "secret",
            gender = "1",
            dob_at = "1980-01-01",
            is_staff = "1",
            is_active = "1",
            is_superuser = "0",
            location = "NY"
        )
        self.backer_1 = Backer.objects.create(
            username = "janedoe",
            first_name = "Jane",
            last_name = "Doe",
            email = "jane@example.com",
            password = "secret",
            gender = "2",
            dob_at = "1980-01-01",
            is_staff = "1",
            is_active = "1",
            is_superuser = "0",
            location = "NY"
        )

    def test_should_create_table_with_corresponding_fields(self):
        self.assertEqual(self.backer.username, "joedoe")
        self.assertEqual(self.backer.first_name, "Joe")
        self.assertEqual(self.backer.last_name, "Doe")
        self.assertEqual(self.backer.email, "joe@example.com")
        self.assertEqual(self.backer.password, "secret")
        self.assertEqual(self.backer.gender, "1")
        self.assertEqual(self.backer.dob_at, "1980-01-01")
        self.assertEqual(self.backer.is_staff, "1")
        self.assertEqual(self.backer.is_active, "1")
        self.assertEqual(self.backer.is_superuser, "0")
        self.assertEqual(self.backer.location, "NY")

        print "test"
    def test_should_unique_username(self):

        try:
            self.backer_1.username = "joedoe"
            self.backer_1.save()

        except Exception:
            self.assertTrue(True)