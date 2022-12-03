from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('topic/', views.TopicList.as_view(), name='topic-list'),  #list all topics
    path('topic/<int:pk>/', views.TopicDetail.as_view(), name='topic-detail'), #get a topic
    path('comment/', views.CommentList.as_view(), name='comment-list'), #list all comments
    path('comment/<int:pk>/', views.CommentDetail.as_view(), name='comment-detail'), #get a comment
    path('topic/<int:topic_id>/comments/', views.individual_comments.as_view(), name='individual-comments'), #get all comments for a topic
]