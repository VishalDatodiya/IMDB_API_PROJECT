from django.urls import path
from watchlist_app.api.views import WatchListView, WatchListDetail

urlpatterns = [
    path('', WatchListView, name='watchlist'),
    path('<int:pk>/', WatchListDetail, name='watchlistDetail'),
]
