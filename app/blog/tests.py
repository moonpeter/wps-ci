from django.test import TestCase


# Create your tests here.


class BlogTest(TestCase):
    def test_post_list(self):
        response = self.client.get('/posts/')
