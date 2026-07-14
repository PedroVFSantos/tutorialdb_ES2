from django.test import TransactionTestCase


class APITests(TransactionTestCase):

    def test_tutorials_page_status_code(self):
        response = self.client.get('/api/tutorials/')
        self.assertEqual(response.status_code, 200)

    def test_tags_page_status_code(self):
        response = self.client.get('/api/tags/')
        self.assertEqual(response.status_code, 200)

    def test_latest_page_status_code(self):
        response = self.client.get('/api/latest/')
        self.assertEqual(response.status_code, 200)

    def test_tutorial_tag_api(self):
        from app.models import Tag, Tutorial
        tag = Tag.objects.create(name="python")
        t = Tutorial.objects.create(
            title="Python Tutorial",
            link="https://python.org",
            category=Tutorial.DOCS,
            publish=True
        )
        t.tags.add(tag)
        response = self.client.get('/api/tutorials/python/')
        self.assertEqual(response.status_code, 200)

    def test_tutorial_tag_category_api(self):
        from app.models import Tag, Tutorial
        tag = Tag.objects.create(name="django")
        t = Tutorial.objects.create(
            title="Django Tutorial",
            link="https://djangoproject.com",
            category=Tutorial.DOCS,
            publish=True
        )
        t.tags.add(tag)
        response = self.client.get('/api/tutorials/django/docs/')
        self.assertEqual(response.status_code, 200)
