from rest_framework import generics
from .models import Post, Comment
from .serializers import UserSerializer, PostSerializer, CommentSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import IsAuthenticated

# Регистрация пользователя
class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

# Эндпоинт для получения токена
class CustomTokenObtainPairView(TokenObtainPairView):
    pass

# Эндпоинт для обновления токена
class CustomTokenRefreshView(TokenRefreshView):
    pass

# Список публикаций
class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]  # Только авторизованные пользователи

# Детали публикации
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

# Загрузка изображений
class UploadImageView(generics.CreateAPIView):

    pass

# Создание публикации
class CreatePostView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

# Создание комментария
class CreateCommentView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

# Изменение статуса избранного
class ToggleFavoriteView(generics.UpdateAPIView):

    pass
