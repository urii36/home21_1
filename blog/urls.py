from django.urls import path

from blog.views import BlogDeleteView, BlogUpdateView, BlogListView, BlogCreateView

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='list'),
    path('detail/<slug>/', BlogPostDetailView.as_view(), name='detail'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('update/<slug>/', BlogUpdateView.as_view(), name='update'),
    path('delete/<slug>/', BlogDeleteView.as_view(), name='delete'),
]