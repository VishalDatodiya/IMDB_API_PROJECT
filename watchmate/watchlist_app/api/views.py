from watchlist_app.models import WatchList
from watchlist_app.api.serializers import WatchListSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET','post'])
def WatchListView(request):
    
    if request.method == 'GET':
        wathlist = WatchList.objects.all()
        serializer = WatchListSerializer(wathlist, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    
@api_view(['GET','PUT','DELETE'])
def WatchListDetail(request, pk):
    
    if request.method == 'GET': 
        try:
            watchlist = WatchList.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(watchlist)
        return Response(serializer.data)

    if request.method == 'PUT':
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    if request.method == 'DELETE':
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        data = {
            'detail':"Deleted successfully",
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)