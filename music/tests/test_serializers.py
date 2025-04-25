from datetime import datetime

from django.test import TestCase

from music.models import Actor, Movie
from music.serializers import ActorSerializer,MovieSerializer


class TestActorSerializer(TestCase):
    def setUp(self):
        self.actor = Actor.objects.create(name='Example actor',birth_date='2020-03-16',gender='male')
        self.actor2 = Actor.objects.create(name='Example actor2')

    def test_data(self):
        data = ActorSerializer(self.actor).data
        assert data['id'] is not None
        assert data['name'] == 'Example actor'
        assert data['birth_date'] == '2020-03-16'
        assert data['gender'] == 'male'

class TestMovieSerializer(TestCase):
    def setUp(self):
        self.actor = Actor.objects.create(name='Example actor')
        self.movie = Movie.objects.create(name='Example movie',)

    def test_is_valid(self):
        data = {
            'id':1,
            'name':'Example movie',
            'year':1990,
            'imdb':'10',
            'genre':'Horror',
            'actors':[self.actor.id],
        }

        serializer = MovieSerializer(data=data)
        self.assertTrue(serializer.is_valid())
