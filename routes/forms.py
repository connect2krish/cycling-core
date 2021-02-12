from django import forms
from .models import Route


class RouteForm(forms.ModelForm):
    title = forms.CharField(label='')
    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={
            "id": "my-html-id",
            "class": "new-css-class-name class-two",
            "rows": 5,
            "cols": 20,
            "placeholder": "route description",
        }))
    distance = forms.DecimalField(initial=0.00)
    iframe_url = forms.CharField(required=True, widget=forms.Textarea(
        attrs={
            "id": "iframe-id",
            "class": "new-css-class-name class-two",
            "rows": 3,
            "cols": 20,
            "placeholder": "route description",
        }))
    url = forms.CharField(required=True, widget=forms.Textarea(
        attrs={
            "id": "url-id",
            "class": "new-css-class-name class-two",
            "rows": 3,
            "cols": 20,
            "placeholder": "route description",
        }))

    class Meta:
        model = Route
        fields = [
            'title',
            'description',
            'distance',
            'iframe_url',
            'url'
        ]
