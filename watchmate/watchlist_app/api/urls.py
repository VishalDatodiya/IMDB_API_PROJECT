from django.urls import path
from watchlist_app.api.views import WatchListView, WatchListDetail, StreamPlatformList, StreamPlatformDetail

urlpatterns = [
    
    # Class based View Urls
    path('', WatchListView.as_view(), name="watchlist"),
    path('<int:pk>/', WatchListDetail.as_view(), name="watchListDetail"),
    
    # Stream Plateform Urls
    path('stream/', StreamPlatformList.as_view(), name='streamPlateformList'),
    path('stream/<int:pk>/', StreamPlatformDetail.as_view(), name='streamPlateformDetail'),
    
    
    # Function Based View Urls
    
#     path('', WatchListView, name='watchlist'),
#     path('<int:pk>/', WatchListDetail, name='watchlistDetail'),
]
