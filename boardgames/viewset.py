from .serializers import BoardGameSerializer, CollectionSerializer
from rest_framework import viewsets
from boardgamegeek.exceptions import BGGItemNotFoundError, BGGApiRetryError
from .utils import get_game_new, get_user_collection
from rest_framework.response import Response
from rest_framework import status


class BoardgameViewSet(viewsets.ViewSet):
    """
    A view set responible to handeling interactions to get boardgames.
    """

    def list(self, request):
        ''' When boardgame list is called require a username be passed in
            Lookup the board games for this username then return the 
            games that user owns as well as information on those users connections. '''
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
        ''' Retrieve a single game based upon the boardgame id '''
        boardgame = get_game_new(pk)
        serializer = BoardGameSerializer(boardgame)
        return Response(serializer.data)
