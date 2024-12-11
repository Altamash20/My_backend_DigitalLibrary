from django.test import TestCase
from auth_app.models import Book

# Create your tests here.
class BookTests(TestCase):
    def test_book_title_property(self):
        book = Book(Title='test')
        self.assertEqual(book.Title, 'test')

        book.Title = 'ABC'
        self.assertEqual(book.Title, 'ABC')
