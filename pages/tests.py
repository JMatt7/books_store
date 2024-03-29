from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView, AboutPageView
# Create your tests here.

class TestHomePage(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get('/')

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_url_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_TemplateHome(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_url(self):
        self.assertContains(self.response, 'Homepage')

    def test_homepage_contains_incorrect_url(self):
        self.assertNotContains(self.response, 'False')

    def test_homepage_url_resolve_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )

class AboutHomePage(SimpleTestCase):

    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_url_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_TemplateHome(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_aboutpage_contains_correct_url(self):
        self.assertContains(self.response, 'About Page')

    def test_aboutpage_contains_incorrect_url(self):
        self.assertNotContains(self.response, 'False')

    def test_aboutpage_url_resolve_aboutpageview(self):
        view = resolve('/about/')
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__
        )