from django.db import models
from django.core import validators
from django.db.models import Avg

from django.contrib.auth.models import User

from datetime import datetime


class Place(models.Model):

    name = models.CharField(max_length=50, )
    added_on = models.DateTimeField(auto_now_add=True, editable=False)
    location = models.CharField(max_length=50,)
    description = models.TextField()
    photo = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='places')

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
    added_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def get_formatted_time(self):
        result = [
            datetime.date(self.added_on).strftime('%d/%m/%y'),
            datetime.time(self.added_on).strftime('%H:%M'),
        ]
        return f' at '.join(result)

    def __str__(self):
        return f'Reviewer: {self.username}, stars: {self.stars}'


class Like(models.Model):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    review = models.ForeignKey(Review, related_name='likes', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'review']

    def __str__(self):
        return f'{self.user.username} Liked comment from Username: {self.review.username}'




