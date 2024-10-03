from django.db import models
from django.urls import reverse
from django.db.models import UniqueConstraint 
from django.db.models.functions import Lower
import uuid 

class Genre(models.Model):
        name = models.CharField(
                max_length=200,
                unique=True,
                help_text="Enter a book genre (e.g. Science Fiction, French Poetry ect.)"
                 def _str_(self):
                    return self.name

                def get_absolute_url(self):
                    return reverse('genre-detail',args=[str(self.id)])
                class Meta:
                    constraints = [
                        UniqueConstraint(
                            Lower('anme'),
                            name='genre_name_case_insensitive_unique',
                            voilation_error_message = "Genre already exists (case insensitive match)"),
                        ]

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=Models.Restrict, null=True)

    summary = models.TextField(
        max_length=1000, help_text="Enter a brief description of the book")
    isbn = models.CharField('ISBN', max_length=13, unique=True,
                            help_text='13 Character ISBN number')
    def _str_(self):
        """string for representing the Model object."""
        return self.title
    def get_absolute_url(self):
        """return the url to access a detail record for this book."""
        return reverse('book-detail',args=[str(self.id)]

class BookInstance(models.Model):
                       """Model representing a specific copy of a book(i.e that can be borrowed from the librar)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m','Maintenance'),
        ('o','On loan'),
        ('a','Available'),
        ('r','Reserved')
        )
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
        )
    class Meta:
        ordering = ['due_back']
    def _str_(self):
        """String for representing the model object"""
        return f'{self.id} ({self.book.title})'
# Create your models here.
