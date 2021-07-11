import pytest
from django.test import TestCase
from apps.post.models import Post
from django.contrib.auth.models import User


class PostTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(
            username='test_user', password='test'
        )
        
    def test_create_post(self):
        Post.objects.create(
            title='test',
            text='test_description'
        )
    
    def test_all_post(self):
        print(Post.objects.all())






