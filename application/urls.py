from django.urls import path
from application import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('content/', views.MediaListView.as_view(), name='content'),
    path('content/<int:pk>', views.MediaDetailView.as_view(), name='content-detail')
]
