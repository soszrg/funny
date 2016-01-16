# Create your models here.
#encoding=utf8
from django.db import models
from django.utils import timezone

class UserManager(models.Manager):
    pass
    
class User(models.Model):
    name = models.CharField(r'用户名', max_length=20, null=False)
    email = models.EmailField(r'邮箱', null=False, unique=True)
    passwd = models.CharField(r'密码', null=False, max_length=30)
    is_active = models.BooleanField(r'激活', default=False)
    date_joined = models.DateTimeField(r'注册日期',default=timezone.now)
    objects = models.Manager
    self_objects = UserManager
    
    class Meta: 
        ordering = ['email']
        db_table = 'blog_user'
        
        
class BlogManager(models.Manager):
    pass

class Blog(models.Manager):
    title = models.CharField(r'主题', max_length=50, null=False)
    user = models.ForeignKey(User)
    content = models.TextField(r'内容', null=False)
    objects = models.Manager
    self_objects = BlogManager