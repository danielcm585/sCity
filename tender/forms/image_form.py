from django.forms import ModelForm
from tender.models.image_model import Image

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['image']