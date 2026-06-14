from rest_framework import serializers


def validate_book_name_length(value):
    if len(value) < 10:
        raise serializers.ValidationError('Book Title must be at least 10 characters')
