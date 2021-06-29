from django.db import models
from courses.models import ClassModel
from django.utils import timezone
from PIL import Image
baseurl = 'http://192.168.0.209:8000'

class UserModel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    classes = models.ManyToManyField(ClassModel)    #the class joined
    role = models.IntegerField(default=0)     #guest-0, user-1, admin-2
    create_time = models.DateTimeField(default=timezone.now)
    phone = models.CharField(max_length=255)
    wechat = models.CharField(max_length=255)
    email = models.EmailField()
    major = models.CharField(max_length=255)
    onecard = models.ImageField(upload_to='uploads/')


    class Meta:
        ordering = ('name',)
        db_table = 'users_user'

    def get_onecard(self):
        if self.onecard:
            return baseurl + self.onecard.url
        return ''
