from django.test import TestCase, Client
from django.urls import reverse
from .models import Book

# Create your tests here.

class BookTest(TestCase):

    def setUp(self):
        self.book = Book.objects.create(
            title = "HP",
            author = "JK",
            price = "25.00",
        )

    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', "HP")
        self.assertEqual(f'{self.book.author}', "JK")
        self.assertEqual(f'{self.book.price}', "25.00")
    
    def test_book_list_view(self):
        resposne = self.client.get(reverse('book_list'))
        self.assertEqual(resposne.status_code, 200)
        self.assertContains(resposne, "HP")
        self.assertTemplateUsed(resposne, 'books/book_list.html')

    def test_book_deatil_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('books/1234')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "HP")
        self.assertTemplateUsed(response, 'books/book_detail.html')
