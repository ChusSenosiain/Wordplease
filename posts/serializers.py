#encoding=UTF-8
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from posts.models import Post

__author__ = 'Chus'


from rest_framework import serializers


class UserSerializer(serializers.Serializer):

    # Retornamos el id de usuario
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()

    # Un serializer tiene que tener los metodos create y update

    def create(self, validated_data):

        """
        Crea una instancia de User a partir de los datos del
        diccionario validated_data,
        :param validated_data:
        :return:
        """
        instance = User()
        return self.update(instance, validated_data)


    def update(self, instance, validated_data):

        """
        Actualiza una instancia de User a partir de los datos del
        diccionario validated_data
        :param instance:
        :param validated_data:
        :return:
        """
        instance.first_name = validated_data.get('first_name') # usamos get porque puede que no venga
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')

        # password encripted
        instance.password = make_password(validated_data.get('password'))

        # Guardamos el objeto (ojo que en web se guarda solo, acordarse de que para api hay que guardarlo)
        instance.save()

        return instance




class PostSerializer(serializers.Serializer):

    # Retornamos el id de usuario
    id = serializers.ReadOnlyField()
    owner = serializers.CharField()
    title = serializers.CharField()
    url = serializers.URLField()
    summary = serializers.CharField()
    created_on = serializers.DateTimeField()
    visibility  = serializers.CharField()

    # Un serializer tiene que tener los metodos create y update

    def create(self, validated_data):

        """
        Crea una instancia de User a partir de los datos del
        diccionario validated_data,
        :param validated_data:
        :return:
        """
        instance = Post()
        return self.update(instance, validated_data)


    def update(self, instance, validated_data):

        """
        Actualiza una instancia de User a partir de los datos del
        diccionario validated_data
        :param instance:
        :param validated_data:
        :return:
        """
        instance.title = validated_data.get('title')
        instance.image = validated_data.get('url')
        instance.summary = validated_data.get('summary')
        instance.created_at = validated_data.get('created_on')
        instance.visibility = validated_data.get('visibility')
        instance.owner = validated_data.get('owner')


        # Guardamos el objeto (ojo que en web se guarda solo, acordarse de que para api hay que guardarlo)
        instance.save()

        return instance

