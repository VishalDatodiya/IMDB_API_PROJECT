from rest_framework import serializers
# from rest_framework.validators import ValidationError
from watchlist_app.models import WatchList

class WatchListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    storyline = serializers.CharField()
    active = serializers.BooleanField(default=False)
    created_date = serializers.DateTimeField()
    
        
    def create(self, validated_data):
        return WatchList.objects.create(**validated_data)
        
        
    def update(self, instance, validate_data):
        instance.title = validate_data.get('title', instance.title)
        instance.storyline = validate_data.get('storyline', instance.storyline)
        instance.active = validate_data.get('active', instance.active)
        instance.created_date = validate_data.get('created_date', instance.created_date)
        instance.save()
        return instance
    
    # Field level Validation
    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Title length is too short.")
        return value
    
    
    # Validation on multiple fields
    def validate(self, data):
        if data['title'].lower() == data['storyline'].lower():
            raise serializers.ValidationError("Title and its Description should be Different.")
        return data