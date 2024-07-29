from django.db import models
from accounts.models import CustomUser
import uuid

def get_thumbnail_upload_path(instance, filename):
    return f'thumbnail/{instance.name}/{filename}'

#헌화 공간 신청
class MemorialHall(models.Model):
    name = models.CharField(verbose_name="추모관 이름", max_length=100)
    date = models.DateTimeField(verbose_name="추모일")
    info = models.CharField(verbose_name="소개글", max_length=50)
    public = models.BooleanField(verbose_name="공개", default=True)
    private = models.BooleanField(verbose_name="비공개", default=False)
    thumbnail = models.ImageField(verbose_name="대표사진", upload_to=get_thumbnail_upload_path, blank=True, null=True)
    participation = models.ManyToManyField(CustomUser, related_name='participation_halls', blank=True)
    # 고유한 토큰 필드 추가, 기본값을 null로 설정 : private가 true일때만 token 생성
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, null=True, blank=True)  
    
    def __str__(self) :
        return self.name
    
    def save(self, *args, **kwargs):
        if self.private and not self.token:
            self.token = uuid.uuid4()
        elif not self.private:
            self.token = None  # 비공개가 아닌 경우 토큰을 제거
        super(MemorialHall, self).save(*args, **kwargs)

#헌화하기 - 결제하기 페이지와 연결 필요
class Wreath(models.Model):
    donation = models.IntegerField(verbose_name="헌화금액", default=1000)
    comment = models.CharField(verbose_name="헌화 한마디", max_length=50, blank=True, null=True)
    name = models.CharField(verbose_name="성함", max_length=10)
    hall = models.ForeignKey(MemorialHall, on_delete=models.CASCADE)
    nickname = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name="작성일", auto_now_add=True)
    
    def __str__(self):
        return self.name

#헌화 공간 밑 추모글 
class Message(models.Model):
    content = models.TextField(verbose_name="추모글", default='')
    hall = models.ForeignKey(MemorialHall, on_delete=models.CASCADE)
    nickname = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name="작성일", auto_now_add=True)
    todak = models.ManyToManyField(CustomUser, related_name='todak_message')
    sympathize = models.ManyToManyField(CustomUser, related_name='sym_msg')
    sad = models.ManyToManyField(CustomUser, related_name='sad_msg')
    commemorate = models.ManyToManyField(CustomUser, related_name='com_msg')
    together = models.ManyToManyField(CustomUser, related_name='together_msg')
    
    def __str__(self):
        return self.content