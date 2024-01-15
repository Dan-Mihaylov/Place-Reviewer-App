from django import forms
from .models import Place, Review


class ReviewWriteForm(forms.ModelForm):

    stars = forms.ChoiceField(
        choices=[(i, str(i)) for i in range(1, 6)],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # removing the labels for each field displayed
        for field_name, field in self.fields.items():
            field.label = False

    class Meta:
        model = Review
        fields = ['username', 'stars', 'comment']

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Username',
                }
            ),
            'comment': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Review',
                }
            )
        }


class PlaceAddForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # removing the labels in front of the forms.

        for field_name, field in self.fields.items():
            field.label = False

    class Meta:
        model = Place
        fields = ['name', 'location', 'description', 'photo']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Place Name',
                    'class': 'form-control',
                }
            ),
            'location': forms.TextInput(
                attrs={
                    'placeholder': 'Location',
                    'class': 'form-control',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                    'class': 'form-control',
                }
            ),
            'photo': forms.URLInput(
                attrs={
                    'placeholder': 'Photo URL',
                    'class': 'form-control',
                }
            ),
        }


class FilterForm(forms.Form):

    CHOICES = (
        ('time_a', 'Time Asc'),
        ('time_d', 'Time Desc'),
        ('stars_a', 'Stars Asc'),
        ('stars_d', 'Stars Desc'),
    )

    filter_by = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
