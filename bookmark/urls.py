from django.urls import path
from .views import *

urlpatterns = [
    path("", BookMarkListView.as_view(), name ='list'),
    path("add/", BookmarkCreateView.as_view(), name='add'),
    path("detail/<int:pk>/", BookmarkDetailView.as_view(), name='detail'),
    path("update/<int:pk>/", BookmarkUpateView.as_view(), name='update'),
    path("delete/<int:pk>/", BookmarkDeleteView.as_view(), name='delete'),
]

#201372055 2학년 B반 김지호
