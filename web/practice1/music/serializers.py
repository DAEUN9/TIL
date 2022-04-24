from .models import Artist, Music
from rest_framework import serializers

class ArtistListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name')


class MusicListSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id', 'title')

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'
        read_only_fields = ('artist',)

class ArtistSerializer(serializers.ModelSerializer):
    music_set = MusicSerializer(many=True, read_only=True)
    music_count = serializers.IntegerField(source='music_set.count', read_only=True)
    class Meta:
        model = Artist
        fields = ('id', 'name', 'music_set', 'music_count',)