from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import rememberTree,Photo
from .serializers import RememberSerializer,PhotoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import MultiPartParser, FormParser

#APIView 사용 : HTTP request에 대한 처리
#TreeAPIView : 기억나무 심기 view
class TreeAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            tree = get_object_or_404(rememberTree, pk=pk)
            serializer = RememberSerializer(tree)
        else:
            trees = rememberTree.objects.all()
            serializer = RememberSerializer(trees, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.user)
        print(request.data)
        data = {
            'treeName': request.data.get('tree_name'),
            'myName': request.data.get('my_name'),
            'flowerType': request.data.get('flower_type'),
            'growth_period': request.data.get('growth_period')
        }
        serializer = RememberSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # 인증된 사용자를 설정
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        data = {
            'treeName': request.data.get('tree_name'),
            'myName': request.data.get('my_name'),
            'flowerType': request.data.get('flower_type'),
            'growth_period': request.data.get('growth_period')
        }
        tree = get_object_or_404(rememberTree, pk=pk)
        serializer = RememberSerializer(tree, data=data)
        if serializer.is_valid():
            serializer.save(user=request.user) 
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        tree = get_object_or_404(rememberTree, pk=pk)
        tree.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PhotoAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, tree_id, pk=None):
        tree = get_object_or_404(rememberTree, pk=tree_id)
        if pk:
            photo = get_object_or_404(Photo, pk=pk, remember_tree=tree)
            serializer = PhotoSerializer(photo)
        else:
            photos = Photo.objects.filter(remember_tree=tree)
            serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)

    def post(self, request, tree_id):
        print(request.data)
        tree = get_object_or_404(rememberTree, pk=tree_id)
        data = {
            'rememberPhoto': request.data.get('rememberPhoto'),
            'description': request.data.get('description'),
            'rememberDate': request.data.get('rememberDate'),
            'comment': request.data.get('comment'),
            'remember_tree': tree.id,
        }
        serializer = PhotoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, tree_id, pk):
        tree = get_object_or_404(rememberTree, pk=tree_id)
        photo = get_object_or_404(Photo, pk=pk, remember_tree=tree)
        data = {
            'rememberPhoto': request.data.get('remember_photo'),
            'description': request.data.get('description'),
            'rememberDate': request.data.get('remember_date'),
            'comment': request.data.get('comment'),
            'remember_tree': tree.id,
        }
        serializer = PhotoSerializer(photo, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, tree_id, pk):
        tree = get_object_or_404(rememberTree, pk=tree_id)
        photo = get_object_or_404(Photo, pk=pk, remember_tree=tree)
        photo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)