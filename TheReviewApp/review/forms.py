from django import forms
from TheReviewApp.review.models import Place, Review


class EditPlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['name', 'location', 'description', 'user', 'photo']

    def __init__(self, *args, **kwargs):    # user=None
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        self.fields['user'].widget = forms.HiddenInput()

        # if user is not None:
        #     self.fields['user'].initial = user
        #     self.fields['user'].widget = forms.HiddenInput()
        #     self.fields['user'].required = False


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

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # removing the labels in front of the forms.

        for field_name, field in self.fields.items():
            field.label = False

        if user is not None:
            self.fields['user'].initial = user
            self.fields['user'].widget = forms.HiddenInput()
            self.fields['user'].required = False

    class Meta:
        model = Place
        fields = ['name', 'location', 'description', 'photo', 'user']
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
