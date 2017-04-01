from .serializers import BoardGameSerializer, CollectionSerializer
from rest_framework import viewsets
from boardgamegeek.exceptions import BGGItemNotFoundError, BGGApiRetryError
from .utils import get_game_new, get_user_collection
from rest_framework.response import Response
from rest_framework import status


class BoardgameViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """

    def list(self, request):
        username = request.GET.get('username', None)
        if username is not None:
            try:
                (collection, boardgames) = get_user_collection(username)
            except BGGItemNotFoundError as err:
                return Response({"status": ', '.join(err.args)},
                                status=status.HTTP_400_BAD_REQUEST)
            except BGGApiRetryError as err:
                return Response({"status": 'Please Wait a Minute and Try Again'},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"status": "required field not found."},
                            status=status.HTTP_404_NOT_FOUND)

        if boardgames is None:
            return Response({"status": "User is not found."},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = BoardGameSerializer(boardgames, many=True)
        collectionSerialized = CollectionSerializer(collection)
        return Response({'collection': collectionSerialized.data, 'games': serializer.data})

    def retrieve(self, request, pk=None):
        boardgame = get_game_new(pk)
        serializer = BoardGameSerializer(boardgame)
        return Response(serializer.data)
