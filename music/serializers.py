from rest_framework import serializers
from music.models import Actor, Movie,Commit

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
         model = Actor
         fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
         model = Movie
         fields = '__all__'


class CommitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commit
        fields = ['movie_id', 'text']

    def create(self, validated_data):
        user = self.context['request'].user
        return Commit.objects.create(user=user, **validated_data)

    def perform_create(self, serializer):
      serializer.validated_data["user"] = self.request.user
      serializer.save()








