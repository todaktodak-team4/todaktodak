from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import rememberTree
from .serializers import RememberSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

#APIView 사용 : HTTP request에 대한 처리
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
