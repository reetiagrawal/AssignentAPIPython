from rest_framework import serializers
from .models import User
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=50)
    #lastname = serializers.CharField(max_length=50)
    #email = serializers.CharField(max_length=50)

#Create api
    def create(self,validated_data):
        return User.objects.create(**validated_data)

#Update API
    def update(self, instance, validated_data):
        instance.text = validated_data.get('text',instance.text)
        #instance.lastname = validated_data.get('lastname', instance.lastname)
        #instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
#Api For Registration Page

class RegistrationSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(max_length=50, min_length=6)
    username = serializers.CharField(max_length=50, min_length=6)
    password = serializers.CharField(max_length=150, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password')

    def validate(self, args):
        email = args.get('email', None)
        username = args.get('username', None)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': ('email already exists')})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username': ('username already exists')})

        return super().validate(args)


    #def create(self, validated_data):
     #   return User.objects.create_user(**validated_data)