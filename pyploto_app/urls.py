from pyploto_app import serializers
from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # JavaScript Web Tokens
    path('token/obtain/',  jwt_views.TokenObtainPairView.as_view(), name='token-create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(),    name='token-refresh'),
    path('blacklist/',     views.LogoutUser.as_view(),              name='token-blacklist'),
    # User paths
    path('users/',              views.UserList.as_view(),   name='user-list'),
    path('users/<str:username>',views.UserDetail.as_view(), name='user-detail'),
    path('users/create/',       views.UserCreate.as_view(), name='user-create'),
    # Posts paths
    path('posts/',              views.PostList.as_view(),                  name='post-list'),
    path('posts/create',        views.PostCreate.as_view(),                name='post-create'),
    path('posts/<int:pk>',      views.PostRetrieveUpdateDestroy.as_view(), name='post-detail'),
    # Comments paths
    path('comments/',         views.CommentListCreate.as_view(),            name='comment-list'),
    path('comments/<int:id>', views.CommentRetrieveUpdateDestroy.as_view(), name='comment-detail')
]