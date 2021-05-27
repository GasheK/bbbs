from django.test import TestCase

from bbbs.common.models import User

USERNAME_ADMIN = 'admin@mail.ru'
USERNAME_MODERATOR_GENERAL = 'general@mail.ru'
USERNAME_MODERATOR_REGIONAL = 'regional@mail.ru'
USERNAME_MENTOR = 'mentor@mail.ru'
USERNAME_SUPERUSER = 'superr@mail.ru'


class UsersManagersTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user_admin = User.objects.create_user(
            username=USERNAME_ADMIN,
            role=User.ADMIN
        )
        cls.user_moderator_general = User.objects.create_user(
            username=USERNAME_MODERATOR_GENERAL,
            role=User.MODERATOR_GENERAL
        )
        cls.user_moderator_regional = User.objects.create_user(
            username=USERNAME_MODERATOR_REGIONAL,
            role=User.MODERATOR_REGIONAL
        )
        cls.user_moderator_mentor = User.objects.create_user(
            username=USERNAME_MENTOR,
            role=User.MENTOR
        )
        cls.user_superuser = User.objects.create_superuser(
            username=USERNAME_SUPERUSER,
        )

    def test_create_admin(self):
        user = self.user_admin
        self.assertEqual(user.username, USERNAME_ADMIN)
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_create_moderator_general(self):
        user = self.user_moderator_general
        self.assertEqual(user.username, USERNAME_MODERATOR_GENERAL)
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_moderator_regional(self):
        user = self.user_moderator_regional
        self.assertEqual(user.username, USERNAME_MODERATOR_REGIONAL)
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_moderator_mentor(self):
        user = self.user_moderator_mentor
        self.assertEqual(user.username, USERNAME_MENTOR)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        user = self.user_superuser
        self.assertEqual(user.username, USERNAME_SUPERUSER)
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertEqual(user.role, User.ADMIN)

