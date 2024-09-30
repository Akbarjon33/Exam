from django.urls import path
from .views import (
    RegisterView,
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    PostListView,
    PostDetailView,
    UploadImageView,
    CreatePostView,
    CreateCommentView,
    ToggleFavoriteView,
)

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('api/posts/', PostListView.as_view(), name='post_list'),
    path('api/posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('api/upload-image/', UploadImageView.as_view(), name='upload_image'),
    path('api/create-post/', CreatePostView.as_view(), name='create_post'),
    path('api/create-comment/', CreateCommentView.as_view(), name='create_comment'),
    path('api/toggle-favorite/<int:post_id>/', ToggleFavoriteView.as_view(), name='toggle_favorite'),
]
