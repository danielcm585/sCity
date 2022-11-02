from rest_framework import serializers

from tourism.models import Place

class PlaceSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField() 

    class Meta:
        model = Place
        fields = ['name','description','price','image_url']

    def get_image_url(self, place):
        request = self.context.get('request')
        photo_url = place.image.url
        return request.build_absolute_uri(photo_url)