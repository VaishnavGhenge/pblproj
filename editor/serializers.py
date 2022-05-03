from rest_framework import serializers
from .models import UserFiles

class UserFilesSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserFiles
        fields = '__all__'