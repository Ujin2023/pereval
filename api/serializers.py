from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['email', 'fam', 'name', 'otc', 'phone']

class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ['latitude', 'longitude', 'height']

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['title', 'img', 'date_added']

class PerevalAddedSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    coord = CoordsSerializer()
    images = ImagesSerializer(many=True)
    class Meta:
        model = PerevalAdded
        fields = ['date_added', 'beauty_title', 'title', 'other_titles', 'connect', 'add_time',
                  'user', 'coord', 'level_winter', 'level_summer', 'level_autumn', 'level_spring', 'images']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        coord_data = validated_data.pop('coord')
        images_data = validated_data.pop('images')
        user, created = Users.objects.get_or_create(email=user_data['email'], defaults=user_data)
        coord = Coords.objects.create(**coord_data)
        pereval = PerevalAdded.objects.create(user=user, coord=coord, **validated_data)
        for image_data in images_data:
            img_obj = Images.objects.create(**image_data)
            PerevalImages.objects.create(pereval_id=pereval, image_id=img_obj)

        return pereval