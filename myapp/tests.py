from django.test import TestCase

class TestCalls(TestCase):

    def test_call_view_load(self):
        response = self.client.get('/myapp/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"Hello, world. You're at the myapp index.")

