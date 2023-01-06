from django.urls import path
from watchlist_app.api.views import WatchListView, WatchListDetail

urlpatterns = [
    
    # Class based View Urls
    path('', WatchListView.as_view(), name="watchlist"),
    path('<int:pk>/', WatchListDetail.as_view(), name="watchListDetail"),
    
    
    # Function Based View Urls
    
#     path('', WatchListView, name='watchlist'),
#     path('<int:pk>/', WatchListDetail, name='watchlistDetail'),
]
