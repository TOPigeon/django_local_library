from django.db import models
from django.urls import reverse
from django.db.models import UniqueConstraint 
from django.db.models.functions import Lower

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

# Create your models here.
