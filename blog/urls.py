from django.urls import path
from .views import HomeView, PostDetaileView, PostListView

app_name = 'blog'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('list', PostListView.as_view(), name='list'),
    path('detail/<int:id>', PostDetaileView.as_view(), name='detail')]
