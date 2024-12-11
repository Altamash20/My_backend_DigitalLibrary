from auth_app.models import Book


def run():
    book = Book.objects.first()
    print('Genre:', book.Genre)
    print("ABC is a horror book?", book.was_a_Horror)