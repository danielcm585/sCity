from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from tender.models.item_model import Item
from tender.models.registrant_model import Registrant
from tender.forms.item_form import ItemForm
from tender.serializers.item_serializer import ItemSerializer

@api_view(['POST'])
def item_api(request, id):
    def post():
        if (request.user.is_authenticated):
            registrant = Registrant.objects.get(id=id)
            if (registrant != None):
                form = ItemForm(request.POST)
                if (form.is_valid()):
                    quantity = form.cleaned_data.get('quantity')
                    price = form.cleaned_data.get('price')

                    registrant.offer_price += price * quantity
                    registrant.save()

                    new_item = Item.objects.create(
                        registrant = registrant,
                        name = form.cleaned_data.get('name'),
                        quantity = quantity,
                        price = price,
                        description = form.cleaned_data.get('description'),
                    )
                    new_item_serialized = ItemSerializer(instance=new_item)
                    return Response(new_item_serialized, status=status.HTTP_201_CREATED)
                return Response(status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    if (request.method == 'POST'): return post()