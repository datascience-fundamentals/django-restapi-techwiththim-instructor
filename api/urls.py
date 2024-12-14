from django.urls import path
from . import views

urlpatterns = [
    path('blogposts', views.BlogPostListCreateView.as_view(),
         name="blogpost-view-create"),
    path("blogposts/<int:pk>",
         views.BlogPostRetrieveUpdateDestroyView.as_view(), name="blogpost-view-update"),
    path("blogposts-custom", views.BlogPostList.as_view(),
         name="blogpost-view-list-custom")
]
