from .serializers import PostSerializer,UserSerialializer
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from .models import Post
# from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly
# Create your views here.
class PostViewSet(ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerialializer

class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer



class UserList(ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = PostSerializer


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = PostSerializer
