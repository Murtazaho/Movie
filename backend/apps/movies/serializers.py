from rest_framework import serializers
from .models import Movie
#MovieSerializer will inherite form serializers.ModelSerializer
class MovieSerializer(serializers.ModelSerializer):
      image = serializers.ImageField(allow_null=True)
      class Meta:

        # Serializer modle and the fields
        model = Movie
        fields = '__all__'