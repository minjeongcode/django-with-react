from django.conf import settings
from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse
# from django.contrib.auth.models import User
# ->auth.User로 불러옴

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField(
        validators=[MinLengthValidator(10)]
    )
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y%m%d')
    tag_set = models.ManyToManyField('Tag', blank=True)
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Java의 toString
    def __str__(self):
        # return f'Custom Post object ({self.id})'
        # return 'Custom Post object ({})'.format(self.id)
        return self.message
    
    def get_absolute_url(self):
        return reverse('instagram:post_detail', args=[self.pk])
    
    
    class Meta:
        ordering = ['-id']
    
    # def message_length(self):
    #     return len(self.message)
    # message_length.short_description = '메세지 글자수' # 추가 컬럼 이름 변경
    # @property 라는 데코레이터로도 동일하게 활용 가능
    # admin에도 구현 가능
    
class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, limit_choices_to={'is_public': True})
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name