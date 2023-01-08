from django.urls import path
from watchlist_app.api.views import WatchListView, WatchListDetail, StreamPlatformList, StreamPlatformDetail, ReviewList, ReviewDetail

urlpatterns = [
    
    # Class based View Urls
    path('', WatchListView.as_view(), name="watchlist"),
    path('<int:pk>/', WatchListDetail.as_view(), name="watchListDetail"),
    
    # Stream Plateform Urls
    path('stream/', StreamPlatformList.as_view(), name='streamPlateformList'),
    path('stream/<int:pk>/', StreamPlatformDetail.as_view(), name='streamPlateformDetail'),
    
    
    # Reviews URLs
    path('reviews/',ReviewList.as_view(), name="reviews"),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name="reviewDetail"),    
    # Function Based View Urls
    
#     path('', WatchListView, name='watchlist'),
#     path('<int:pk>/', WatchListDetail, name='watchlistDetail'),
]
