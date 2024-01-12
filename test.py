import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TheReviewApp.settings")
django.setup()


from TheReviewApp.review.models import Place, Avg


place = Place.objects.get(id=1)



