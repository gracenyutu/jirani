from rest_framework.response import Response
from rest_framework.decorators import api_view
from app.models import Neighborhood, Post, Profile, Business
from .serializers import ProfileSerializer, PostSerializer, UserSerializer, NeighborhoodSerializer, BusinessSerializer
from django.contrib.auth.models import User

@api_view(['GET'])
def getProfile(request):
    profile = Profile.objects.all()
    serializer = ProfileSerializer(profile, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getNeighborhood(request):
    neighborhood = Neighborhood.objects.all()
    serializer = NeighborhoodSerializer(neighborhood, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getBusiness(request):
    business = Business.objects.all()
    serializer = BusinessSerializer(business, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUser(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPost(request):
    post = Post.objects.all()
    serializer = PostSerializer(post, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
