from django.forms import ModelForm
from tender.models.item_model import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name','quantity','price','description']