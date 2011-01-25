"""
Tests for the cmsplugin_news app
"""

import datetime

from django.test import TestCase
from django.contrib.auth.models import Permission, User

from models import News

class NewsTest(TestCase):
    def setUp(self):
        self.today = datetime.datetime.today()
        self.yesterday = self.today - datetime.timedelta(days=1)
        self.tomorrow = self.today + datetime.timedelta(days=1)

    def tearDown(self):
        pass


    def test_unpublished(self):
        """
            Test if unpublished items are hidden by default
        """
        unpublished = News.objects.create(
            title='Unpublished News',
            slug='unpublished-news',
            is_published=False,
            pub_date=self.yesterday,
        )
        self.assertEquals(News.published.count(), 0)
        unpublished.is_published = True
        unpublished.save()
        self.assertEquals(News.published.count(), 1)
        unpublished.is_published = False
        unpublished.save()
        self.assertEquals(News.published.count(), 0)

        unpublished.delete()

    def test_future_published(self):
        """
            Tests that items with a future published date are hidden
        """
        future_published = News.objects.create(
            title='Future published News',
            slug='future-published-news',
            is_published=True,
            pub_date=self.tomorrow,
        )
        self.assertEquals(News.published.count(), 0)
        future_published.pub_date = self.yesterday
        future_published.save()
        self.assertEquals(News.published.count(), 1)
        future_published.pub_date = self.tomorrow
        future_published.save()
        self.assertEquals(News.published.count(), 0)

    def test_publish_permissions(self):
        """
            Tests assigning of can_publish permission for superuser/non superuser users
        """
        superuser = User.objects.create(username='superman', is_staff=True, is_superuser=True)
        averagepleb = User.objects.create(username='pleb', is_staff=True, is_superuser=False)

        permission = 'news.can_publish'

        self.assertTrue(superuser.has_perm(permission))
        self.assertFalse(averagepleb.has_perm(permission))
