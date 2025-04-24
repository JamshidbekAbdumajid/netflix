# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import  status
from rest_framework.response import Response
from rest_framework.decorators import action
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAuthenticated

from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
# from typing_extensions import ReadOnly

from .models import Movie, Actor, Casting,Commit
from .serializers import MovieSerializer,ActorSerializer
# from rest_framework import filters

# from rest_framework.decorators import api_view


# class CommitAPIVew(APIView):
#     permission_classes = [IsAuthenticated]
# #     # authentication_classes = [TokenAuthentication]
#
#     def delete(self, request, *args, **kwargs):
#         try:
#             # Assuming you're passing an 'id' in the URL or request data
#             commit_id = kwargs.get('id') or request.data.get('id')
#             commit = Commit.objects.get(id=commit_id, user=request.user)
#
#             commit.delete()
#             return Response(
#                 {"message": "Commit deleted successfully"},
#                 status=status.HTTP_204_NO_CONTENT
#             )
#
#         except Commit.DoesNotExist:
#             return Response(
#                 {"error": "Commit not found or you don't have permission"},
#                 status=status.HTTP_404_NOT_FOUND
#             )
#         except Exception as e:
#             return Response(
#                 {"error": str(e)},
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#
#
#     def get(self,request,*args,**kwargs):
#         serializer = CommitSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def post(self, request, *args, **kwargs):
    #     serializer = CommitSerializer(data=request.data, context={'request': request})
    #     if serializer.is_valid():
    #         serializer.save(user=request.user)
    #         return Response({'message': 'Commit created successfully!', 'data': serializer.data}, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #


# class CommitVIewSet(ModelViewSet):
#     # serializer_class = CommitSerializer
#     # authentication_classes = (TokenAuthentication,)
#     # permission_classes = (IsAuthenticated,)
#     queryset = Commit.objects.all()
#     def perform_create(self, serializer):
#         serializer.validated_data["user"] = self.request.user
#         serializer.save()


class ActorViewSet(ReadOnlyModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all().order_by('-imdb')
    serializer_class = MovieSerializer
    # filter_backends = [DjangoFilterBackend]
    filterset_fields = ['genre']
    # filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    ordering_fields = ['imdb','-imdb']
    search_fields = ['name']

    @action(detail=True, methods=['post'])
    def add_actor(self, request, pk=None):
        movie = self.get_object()
        actor_id = request.data.get('actor_id')
        role = request.data.get('role', '')
        joined_at = request.data.get('joined_at', None)

        if not actor_id:
            return Response({"error": "actor_id is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            actor = Actor.objects.get(pk=actor_id)
        except Actor.DoesNotExist:
            return Response({"error": "Actor not found"}, status=status.HTTP_404_NOT_FOUND)

        casting, created = Casting.objects.get_or_create(
            actor=actor,
            movie=movie,
            defaults={'role': role, 'joined_at': joined_at}
        )

        if not created:
            return Response({"message": "Actor already added to movie"}, status=status.HTTP_200_OK)

        return Response({"message": "Actor added successfully"}, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def remove_actor(self, request, pk=None):
        movie = self.get_object()
        actor_id = request.data.get('actor_id')

        try:
            casting = Casting.objects.get(actor_id=actor_id, movie=movie)
        except Casting.DoesNotExist:
            return Response({"error": "Actor not found in this movie"}, status=status.HTTP_404_NOT_FOUND)

        casting.delete()
        return Response({"status": "Actor removed"}, status=status.HTTP_200_OK)
#
    # class MovieActorAPIView(APIView):
    #     def get(self, request, pk):
    #         try:
    #             movie = Movie.objects.get(id=pk)
    #         except Movie.DoesNotExist:
    #             return Response({"error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)
    #
    #         actors = movie.actors.all()
    #         serializer = ActorSerializer(actors, many=True)
    #         return Response(serializer.data, status=status.HTTP_200_OK)
