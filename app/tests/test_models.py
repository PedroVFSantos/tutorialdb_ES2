from django.test import TestCase
from app.models import Tag, Tutorial

class TagModelTest(TestCase):
    def test_string_representation(self):
        tag = Tag(name="Python")
        self.assertEqual(str(tag), tag.name)

    def test_published_tutorials_count(self):
        tag = Tag.objects.create(name="Django")
        
        t1 = Tutorial.objects.create(
            title="Django Tutorial 1",
            link="https://example.com/1",
            category=Tutorial.DOCS,
            publish=True
        )
        t1.tags.add(tag)
        
        t2 = Tutorial.objects.create(
            title="Django Tutorial 2",
            link="https://example.com/2",
            category=Tutorial.DOCS,
            publish=False
        )
        t2.tags.add(tag)
        
        self.assertEqual(tag.published_tutorials_count(), 1)

class TutorialModelTest(TestCase):
    def setUp(self):
        self.tutorial = Tutorial(
            title="Learn Django",
            link="https://docs.djangoproject.com/",
            category=Tutorial.DOCS,
            publish=True
        )
        self.tutorial.save()

    def test_string_representation(self):
        self.assertEqual(str(self.tutorial), self.tutorial.title)

    def test_is_published(self):
        self.assertTrue(self.tutorial.is_published())

    def test_not_published(self):
        draft = Tutorial(
            title="Draft",
            link="http://example.com",
            category=Tutorial.ARTICLE,
            publish=False
        )
        draft.save()
        self.assertFalse(draft.is_published())
