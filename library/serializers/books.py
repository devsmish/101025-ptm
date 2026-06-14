from rest_framework import serializers
from django.utils import timezone

from library.models import Book, Publisher, Genre
from library.serializers.genres import GenreSerializer
from library.validators import validate_book_name_length





class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


class BookListSerializer(serializers.ModelSerializer):
    """
    Модел сериалайзер умеет привязываться к конкретной указаной модели.
    Когда мы указываем ему мета класс, там мы говорим:
    1. На какую модель должен привязаться сериалайзер
    2. В этой модели, на какие поля он должен смотреть (fields), или
    какие поля он должен исключить (exclude)
    """
    # created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', write_only=True)
    publisher = PublisherSerializer()
    genres = serializers.PrimaryKeyRelatedField(many=True, queryset=Genre.objects.all())

    class Meta:
        model = Book
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[validate_book_name_length])
    class Meta:
        model = Book
        fields = '__all__'

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError('Price must be greater than 0')
        return value

    def validate(self, data):
        if 'discounted_price' in data and data['discounted_price'] and data['discounted_price'] >= data['price']:
            raise serializers.ValidationError('Discounted price must be less than price')
        return data

    def create(self, validated_data):
        validated_data['created_at'] = timezone.now()
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'title' in validated_data:
            validated_data['title'] = validated_data['title'].strip().upper()
        return super().update(instance, validated_data)
