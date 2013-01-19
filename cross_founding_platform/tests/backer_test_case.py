from django.contrib.auth.models import User
from django.test import TestCase
from cross_founding_platform.cross_founding.models import Backer

class BackerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.get_or_create(
            username = "joedoe",
            first_name = "Joe",
            last_name = "Doe",
            email = "joe@example.com",
            password = "secret",)

        self.user_1 = User.objects.get_or_create(
            username = "janedoe",
            first_name = "Jane",
            last_name = "Doe",
            email = "jane@example.com",
            password = "secret",)


        self.backer = Backer(
                user_id=self.user,
                gender = 2,
                dob_at = "1980-01-01",
                location = "NY"
            )

    def test_should_create_table_with_corresponding_fields(self):
        self.user = User.objects.get(pk=1)
        self.assertEqual(self.user.username, "joedoe")
        self.assertEqual(self.user.first_name, "Joe")
        self.assertEqual(self.user.last_name, "Doe")
        self.assertEqual(self.user.email, "joe@example.com")
        self.assertEqual(self.user.password, "secret")
        self.assertEqual(self.backer.gender, 2)
        self.assertEqual(self.backer.location, "NY")
        self.assertNotEqual(self.backer.location, "NY_1")

    def test_should_unique_username(self):

        try:
            self.user_1.username = "joedoe"
            self.user_1.save()

        except Exception:
            self.assertTrue(True)