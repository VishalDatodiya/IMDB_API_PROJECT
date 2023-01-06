from rest_framework import serializers
from watchlist_app.models import WatchList

class WatchListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    storyline = serializers.CharField()
    active = serializers.BooleanField(default=False)
    created_date = serializers.DateTimeField()
    
        
    def create(self, validated_data):
        return WatchList.objects.create(**validated_data)
        
        
        
    # class Meta:
    #     model = WatchList
    #     fields = ['title','storyline','active','created_date']