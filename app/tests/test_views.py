from django.test import SimpleTestCase, TransactionTestCase


class StaticPageTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_api_page_status_code(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_contribute_page_status_code(self):
        response = self.client.get('/contribute/')
        self.assertEqual(response.status_code, 200)


class DynamicPageTests(TransactionTestCase):

    def test_latest_page_status_code(self):
        response = self.client.get('/latest/')
        self.assertEqual(response.status_code, 200)

    def test_tags_page_status_code(self):
        response = self.client.get('/tags/')
        self.assertEqual(response.status_code, 200)

    def test_search_query_view(self):
        from app.models import Tag, Tutorial
        tag = Tag.objects.create(name="django")
        t = Tutorial.objects.create(
            title="Django Advanced",
            link="https://djangoproject.com/adv",
            category=Tutorial.DOCS,
            publish=True
        )
        t.tags.add(tag)

        response = self.client.get('/search/?q=django')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/search/?q=django&category=docs')
        self.assertEqual(response.status_code, 200)

    def test_taglinks_view(self):
        from app.models import Tag, Tutorial
        tag = Tag.objects.create(name="python")
        t = Tutorial.objects.create(
            title="Python Advanced",
            link="https://python.org/adv",
            category=Tutorial.DOCS,
            publish=True
        )
        t.tags.add(tag)

        response = self.client.get('/tags/tag=python')
        self.assertEqual(response.status_code, 200)


class TestTemplateNames(TransactionTestCase):

    def test_home_page_name(self):
        response = self.client.get('/')
        self.assertTemplateUsed(template_name='home.html')

    def test_api_page_name(self):
        response = self.client.get('/api/')
        self.assertTemplateUsed(template_name='api.html')

    def test_about_page_name(self):
        response = self.client.get('/about/')
        self.assertTemplateUsed(template_name='about.html')

    def test_contribute_page_name(self):
        response = self.client.get('/contribute/')
        self.assertTemplateUsed(template_name='contribute.html')

    def test_latest_page_name(self):
        response = self.client.get('/latest/')
        self.assertTemplateUsed(template_name='latest.html')

    def test_tags_page_name(self):
        response = self.client.get('/tags/')
        self.assertTemplateUsed(template_name='tags.html')

