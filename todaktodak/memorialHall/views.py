from django.shortcuts import render
from .models import MemorialHall, Wreath, Message
from .serializers import MemorialHallSerializer, WreathSerializer, MessageSeralizer
from rest_framework.viewsets import ModelViewSet
from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .pagenation import MemorialHallPagination, MessagePagination
from rest_framework.permissions import IsAuthenticated, AllowAny

#추모관 페이지네이션(한페이지 6개 추모관)
class MemorialHallViewSet(ModelViewSet) :
    queryset = MemorialHall.objects.all()
    serializer_class = MemorialHallSerializer
    pagination_class = MemorialHallPagination
    
    #검색
    def get_queryset(self):
        queryset = MemorialHall.objects.all().order_by('-date')
        search_keyword = self.request.GET.get('q', '')

        if search_keyword:
            queryset = queryset.filter(
                Q(name__icontains=search_keyword)
            )
        return queryset
    
    #내가 참여한 추모관
    @action(detail=False, methods=['get'], url_path='my-participation')
    def my_participation(self, request):
        user = request.user
        participated_halls = self.queryset.filter(participants=user).order_by('-date')
        serializer = self.get_serializer(participated_halls, many=True)
        return Response(serializer.data)
    
    # 토큰을 통해 비공개 추모관 접근
    @action(detail=True, methods=['get'], url_path='access', permission_classes=[AllowAny])
    def access_private_hall(self, request, pk=None):
        token = request.query_params.get('token')
        hall = get_object_or_404(MemorialHall, pk=pk, token=token)
        serializer = self.get_serializer(hall)
        return Response(serializer.data)

    # 추모관 참여하기
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def participate(self, request, pk=None):
        hall = get_object_or_404(MemorialHall, pk=pk)
        if hall.private:
            token = request.data.get('token')
            if not token or token != str(hall.token):
                return Response({'status': 'Invalid token'}, status=400)
        user = request.user
        hall.participation.add(user)
        return Response({'status': 'participated'})

    # 추모관 참여 취소하기
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def unparticipate(self, request, pk=None):
        hall = get_object_or_404(MemorialHall, pk=pk)
        user = request.user
        hall.participation.remove(user)
        return Response({'status': 'unparticipated'})
   
#헌화하기
class WreathViewSet(ModelViewSet):
    queryset = Wreath.objects.all()
    serializer_class = WreathSerializer
    pagination_class = None  # 페이지네이션을 사용하지 않도록 설정
    
    def perform_create(self, serializer):
        serializer.save(nickname = self.request.user)
        
    def get_queryset(self, **kwargs): # Override, 4
        id = self.kwargs['memorialHall_id']
        return self.queryset.filter(hall=id).order_by('-created_at')
    
    # 내가 한 헌화 신청만 확인
    @action(detail=False, methods=['get'], url_path='my-wreaths')
    def my_wreaths(self, request):
        user = request.user
        my_wreaths = self.queryset.filter(nickname=user).order_by('-created_at')
        serializer = self.get_serializer(my_wreaths, many=True)
        return Response(serializer.data)
    
#추모글 - 헌화의 한마디도 같이 보이게 구현필요)
class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSeralizer
    pagination_class = MessagePagination

    def perform_create(self, serializer):
        serializer.save(nickname = self.request.user)
    
    def get_queryset(self, **kwargs): # Override, 4
        id = self.kwargs['memorialHall_id']
        return self.queryset.filter(hall=id).order_by('-created_at')
    #memorialHall로 MemorialHall과 foriegnkey연결시켰더니 인식 못하는 오류!!
    
    #토닥토닥
    @action(detail=True, methods=['post'])
    def todak(self, request, pk=None, memorialHall_id=None):
        message = get_object_or_404(Message, pk=pk) 
        # message = get_object_or_404(Message, pk=pk, hall=memorialHall_id) 
        user = request.user
        
        if user in message.todak.all():
            message.todak.remove(user)
            return Response({'status': 'todak removed'})
        else:
            message.todak.add(user)
            return Response({'status': 'todak added'})
    #공감해요 
    @action(detail=True, methods=['post'])
    def sympathizek(self, request, pk=None, memorialHall_id=None):
        message = get_object_or_404(Message, pk=pk)
        user = request.user
        
        if user in message.sympathize.all():
            message.sympathize.remove(user)
            return Response({'status': 'sympathize removed'})
        else:
            message.sympathize.add(user)
            return Response({'status': 'sympathize added'})
    #슬퍼요
    @action(detail=True, methods=['post'])
    def sad(self, request, pk=None, memorialHall_id=None):
        message = get_object_or_404(Message, pk=pk)
        user = request.user
        
        if user in message.sad.all():
            message.sad.remove(user)
            return Response({'status': 'sad removed'})
        else:
            message.sad.add(user)
            return Response({'status': 'sad added'})
    #추모해요
    @action(detail=True, methods=['post'])
    def commemorate(self, request, pk=None, memorialHall_id=None):
        message = get_object_or_404(Message, pk=pk)
        user = request.user
        
        if user in message.commemorate.all():
            message.commemorate.remove(user)
            return Response({'status': 'commemorate removed'})
        else:
            message.commemorate.add(user)
            return Response({'status': 'commemorate added'})
    #함께해요
    @action(detail=True, methods=['post'])
    def together(self, request, pk=None, memorialHall_id=None):
        message = get_object_or_404(Message, pk=pk)
        user = request.user
        
        if user in message.together.all():
            message.together.remove(user)
            return Response({'status': 'together removed'})
        else:
            message.together.add(user)
            return Response({'status': 'together added'})