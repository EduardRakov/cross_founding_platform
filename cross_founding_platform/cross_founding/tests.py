from django.test import TestCase
from cross_founding_platform.cross_founding.models import CustomUser, Project, Backer

class SimpleTest(TestCase):
    def test_fields_tables(self):
        self.test_project = Project.objects.create(name = "project_name", description = "project_desc")
        self.test_backer = Backer.objects.create(test_field = "backer")
        self.test_user = CustomUser.objects.create(
            username = "batman",
            first_name = "Bruce",
            last_name = "Wayne",
            email = "bat@man.com",
            password = "iambatman",
            is_staff = "1",
            is_active = "1",
            is_superuser = "0",
            location = "NY",
            project_owner_id = "1",
            backer_id = "1"
        )
        self.assertEqual(self.test_user.username, "batman")
        self.assertEqual(self.test_project.name, "project_name")
        self.assertEqual(self.test_backer.test_field, "backer")
