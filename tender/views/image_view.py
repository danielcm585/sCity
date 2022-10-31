from rest_framework import status
from rest_framework.response import Response
from tender.forms.image_form import ImageForm
from tender.models.image_model import Image
from tender.serializers.image_serializer import ImageSerializer

def new_image(request):
    def post():
        # Create new image
        form = ImageForm(request.POST, request.FILES)
        if (form.is_valid()):
            form.save()
            new_image = form.instance()
            new_image_serialized = ImageSerializer(instance=new_image)
            return Response(new_image_serialized.data, status=status.HTTP_201_CREATED)

    if (request.method == 'POST'): return post()

def one_image(request, id):
    def get():
        image = Image.objects.get(id=id)
        image_serialized = ImageSerializer(instance=image, context={ 'request': request })
        return Response(image_serialized.data, status=status.HTTP_200_OK)
    
    if (request.method == 'GET'): return get()