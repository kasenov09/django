from django.contrib.auth import get_user_model
from rest_framework.response import Response

from .models import Post
from .serializers import Post