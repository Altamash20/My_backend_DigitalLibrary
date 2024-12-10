from auth_app.models import Book

def run():
    book = Book()
    book.Title = 'My Biography'
    book.Author = 'Someone2'
    book.ISBN = '28066'
    book.Genre = Book.TypeChoices.OTHER
    book.Cover_Image_URL = 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fhighschool.latimes.com%2Fbeacon-park-school%2Fopinion-why-we-should-read-classical-literature%2F&psig=AOvVaw1Cr3qZtW94YHJyk_QNVQ1p&ust=1733951942800000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCKiAiL-QnooDFQAAAAAdAAAAABAI'

    book.save()
