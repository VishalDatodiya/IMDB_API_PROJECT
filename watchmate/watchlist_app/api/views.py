from watchlist_app.models import WatchList
from watchlist_app.api.serializers import WatchListSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


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
    
    
@api_view()
def WatchListDetail(request, pk):
    watchlist = WatchList.objects.get(pk=pk)
    serializer = WatchListSerializer(watchlist)
    return Response(serializer.data)