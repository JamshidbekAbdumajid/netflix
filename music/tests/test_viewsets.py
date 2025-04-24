from django.test import TestCase , Client
from music.models import Movie, Actor
from django.urls import reverse
from rest_framework import status


class TestMovieViewSet(TestCase):
    def setUp(self):
        # self.movie_low_rating = Movie.objects.create(
        #     name="Low Rating Movie",
        #     year=2020,
        #     genre="Action",
        #     imdb=5.2
        # )
        # self.movie_high_rating = Movie.objects.create(
        #     name="High Rating Movie",
        #     year=2019,
        #     genre="Drama",
        #     imdb=9.1
        # )
        # self.movie_medium_rating = Movie.objects.create(
        #     name="Medium Rating Movie",
        #     year=2021,
        #     genre="Comedy",
        #     imdb=7.5
        # )
        self.movie = Movie.objects.create(name='Example Movie')

        self.client = Client()


    # def test_movie_viewset(self):
    #     response = self.client.get('/movies/')
    #     data = response.data
    #
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(len(data), 1)
    #     self.assertIsNotNone(data[0]["id"])
    #     self.assertEqual(data[0]['name'], 'Example movie')
    def test_actor_viewset(self):
        response = self.client.get('/movies/?search=Example')
        data = response.data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertIsNotNone(data[0]["id"])
        self.assertEqual(data[0]['name'], 'Example Movie')

    #
    # def test_movie_viewset(self):
    #
    #     response = self.client.get( '/movies/?ordering=imdb/')
    #
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    #     ordered_movies = response.data
    #
    #     self.assertEqual(ordered_movies[0]['name'], "Low Rating Movie")  # 5.2
    #     self.assertEqual(ordered_movies[1]['name'], "Medium Rating Movie")  # 7.5
    #     self.assertEqual(ordered_movies[2]['name'], "High Rating Movie")  # 9.1
    #
    #
    #
    #
