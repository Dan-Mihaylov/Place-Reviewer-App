from django.db import models
from django.core import validators
from django.db.models import Avg


class Place(models.Model):

    name = models.CharField(max_length=50, )
    added_on = models.DateTimeField(auto_now_add=True, editable=False)
    location = models.CharField(max_length=50,)
    description = models.TextField()
    photo = models.URLField(blank=True, null=True)

    def total_stars(self):
        return self.reviews.aggregate(average=Avg('stars'))

    def __repr__(self):
        return f"{self.name} | {self.location}"

    def __str__(self):
        return f"{self.name} | {self.location}"


class Review(models.Model):
    username = models.CharField(max_length=50)
    stars = models.IntegerField(
        validators=[
            validators.MaxValueValidator(5),
            validators.MinValueValidator(1),
        ]
    )
    comment = models.TextField()
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='reviews')

