from django.db import models
from accounts.models import CustomUser

def user_photo_upload_to(instance, filename):
    user_id = instance.remember_tree.user.id
    return f'user_{user_id}/rememberTree_photos/{filename}'

# 기억나무 모델
class rememberTree(models.Model): 
    treeName = models.CharField(max_length=20)
    myName = models.CharField(max_length=100, null=False, default='토닥토닥') 
    flowerType = models.CharField(max_length=20, null= False, default='')
    growth_period = models.DateField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='trees')

    def __str__(self):
        return self.treeName

# 사진 모델
class Photo(models.Model):
    image = models.ImageField(upload_to=user_photo_upload_to)
    description = models.CharField(max_length=255, blank=True, null=True)
    remember_tree = models.ForeignKey(rememberTree, on_delete=models.CASCADE, related_name='photos')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo {self.id} for {self.remember_tree.treeName}"