from auth_app.models import Book


def run():
    book = Book.objects.first()
    print('Author:', book.Genre)
    print("abcxyz?", book.was_a_Horror)