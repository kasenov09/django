from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields =  ['body']Установка прошла успешно! Поздравляем!
Вы видите данную страницу, потому что указали DEBUG=True в файле настроек и