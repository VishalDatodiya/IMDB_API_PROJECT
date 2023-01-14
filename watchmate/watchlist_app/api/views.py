from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
# from rest_framework import mixins
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle, ScopedRateThrottle

from watchlist_app.api.permissions import IsAdminOrReadOnly, IsUserReviewOrReadOnly
from watchlist_app.models import WatchList, StreamPlatform, Review
from watchlist_app.api.serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer

# Scop rate throttling
from watchlist_app.api.trottling import ReviewCreateThrottle, ReviewListThrottle 






# =============================================================================================================

# Using generic (concrete class based view)

# =============================================================================================================


class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    
    permission_classes = [IsAuthenticated]
    
    # Scope rate trottle
    throttle_classes = [ReviewCreateThrottle]
    
    def get_queryset(self):
        return Review.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        watchlist = WatchList.objects.get(pk=pk)
        
        # Checking if same user posting review 2nd time for same movie
        review_user = self.request.user
        review_queryset = Review.objects.filter(watchlist=watchlist, review_user=review_user)  # here i am cheking on both movie and            
                                                                                                # user.It means same movie or same user
        
        if review_queryset.exists():
            raise ValidationError("You already gave the Review!")
        
        
        # Reting calculation after the isExist condition bcz we want to first check that is they Gave review or not otherwise it affect our calculations
        
        if watchlist.number_rating == 0:
            watchlist.average_rating = serializer.validated_data['rating']
        else:
            watchlist.average_rating = (watchlist.average_rating + serializer.validated_data['rating']) / 2
        
        watchlist.number_rating += 1
        watchlist.save()
        
        serializer.save(watchlist=watchlist, review_user=review_user)



class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes = [IsAuthenticated]
    
    # Local Throtting
    # throttle_classes = [UserRateThrottle, AnonRateThrottle]
    
    # Scope rate throttling
    throttle_classes = [ReviewListThrottle, AnonRateThrottle]
    
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    # permission_classes = [IsAdminOrReadOnly]
    permission_classes = [IsUserReviewOrReadOnly]

    # Local Throtting
    # throttle_classes = [UserRateThrottle, AnonRateThrottle]


    # Throttling rate scope where you don't need to create new throttling class
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'review-detail'

# =============================================================================================================

# Using mixing

# =============================================================================================================


# class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)


class StreamPlatformList(APIView):
    
    permission_classes = [IsAdminOrReadOnly]
    
    def get(self, request):
        platforms = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platforms, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class StreamPlatformDetail(APIView):
    
    permission_classes = [IsAdminOrReadOnly]
    
    def get(self, request, pk):
        try:
            plateform = StreamPlatform.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(plateform)
        return Response(serializer.data)

    def put(self, request, pk):
        plateform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(plateform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk):
        try:
            plateform = StreamPlatform.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        plateform.delete()
        data = {
            'detail':"Deleted successfully",
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


class WatchListView(APIView):
    
    permission_classes = [IsAdminOrReadOnly]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        wathlist = WatchList.objects.all()
        serializer = WatchListSerializer(wathlist, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WatchListDetail(APIView):
    
    permission_classes = [IsAdminOrReadOnly]
    
    def get(self, request, pk):
        try:
            watchlist = WatchList.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(watchlist)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        movie.delete()
        data = {
            'detail':"Deleted successfully",
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET','post'])
# def WatchListView(request):
    
#     if request.method == 'GET':
#         wathlist = WatchList.objects.all()
#         serializer = WatchListSerializer(wathlist, many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = WatchListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
    
    
# @api_view(['GET','PUT','DELETE'])
# def WatchListDetail(request, pk):
    
#     if request.method == 'GET': 
#         try:
#             watchlist = WatchList.objects.get(pk=pk)
#         except:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = WatchListSerializer(watchlist)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#         movie = WatchList.objects.get(pk=pk)
#         serializer = WatchListSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
    
#     if request.method == 'DELETE':
#         movie = WatchList.objects.get(pk=pk)
#         movie.delete()
#         data = {
#             'detail':"Deleted successfully",
#         }
#         return Response(data, status=status.HTTP_204_NO_CONTENT)