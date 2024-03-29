from django.urls import path
from .views import *

urlpatterns = [
    path("colleges/",CollegeListAPI.as_view()),
    path("posts/",PostListAPI.as_view()),
    path("post_images/",PostImageListAPI.as_view()),
    path('books/', BookListAPI.as_view()),
    path('books/<str:static_id>', BookDetailAPI.as_view()),
    path('videos/', VideoListAPI.as_view()),
    path('front/', FrontPageAPI.as_view()),
    path('footer/', FooterAPI.as_view()),
]