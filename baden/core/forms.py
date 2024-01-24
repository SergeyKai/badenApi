from django import forms
from .models import Apartment, ApartmentImage

from django import forms


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class ApartmentForm(forms.ModelForm):
    images = MultipleFileField()

    class Meta:
        model = Apartment
        fields = '__all__'

    def save(self, commit=False):
        obj = super().save(commit=True)
        files = self.cleaned_data.get('images')
        for file in files:
            ApartmentImage.objects.create(
                apartment=obj,
                img=file
            )
        return obj
