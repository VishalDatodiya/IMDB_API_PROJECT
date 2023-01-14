from django.urls import path
from watchlist_app.api.views import WatchListView, WatchListDetail, StreamPlatformList, StreamPlatformDetail, ReviewList, ReviewDetail,ReviewCreate

urlpatterns = [
    
    # Function Based View Urls
    
#     path('', WatchListView, name='watchlist'),
#     path('<int:pk>/', WatchListDetail, name='watchlistDetail'),
    
    
    # Class based View Urls
    path('', WatchListView.as_view(), name="watchlist"),
    path('<int:pk>/', WatchListDetail.as_view(), name="watchListDetail"),
    
    # Stream Plateform Urls
    path('stream/', StreamPlatformList.as_view(), name='streamPlateformList'),
    path('stream/<int:pk>/', StreamPlatformDetail.as_view(), name='streamPlateformDetail'),
    
    
    # Reviews URLs
    # I want all the reviews of a purticular movie only
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name="reviewCreate"),
    path('<int:pk>/reviews/',ReviewList.as_view(), name="reviews"),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name="reviewDetail"),    
    
    
    
    
]
