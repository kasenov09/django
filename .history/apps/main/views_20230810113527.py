from django.contrib.auth import get_user_model
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer

User = get_user_model()


@api_view(['GET'])
def post_list(request):
    queryset = Post.objects.all()
    serializer = PostSerializer(qweryset, man)