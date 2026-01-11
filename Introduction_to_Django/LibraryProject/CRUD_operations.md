## Create Operation

```python
from bookshelf.models import Book

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
book
## Retrieve Operation

from bookshelf.models import Book

book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year

## Update Operation

from bookshelf.models import Book

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book

## Delete Operation

from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

Book.objects.all()
