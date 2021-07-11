from django.test import TestCase
from apps.comentary.models import Comentary
from django.contrib.auth.models import User


class ComentaryTestCase(TestCase):
    def test_create(self):
        user = User.objects.create_user(
            username='test_user', 
            password='test_password'
        )
        Comentary.objects.create(
            owner=user.profile,
            txt='test'
        )
        self.assertEqual(User.objects.last().profile, user.profile)


