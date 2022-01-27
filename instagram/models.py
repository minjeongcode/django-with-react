from django.db import models

class Post(models.Model):
    message = models.TextField()
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y%m%d')
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Java의 toString
    def __str__(self):
        # return f'Custom Post object ({self.id})'
        # return 'Custom Post object ({})'.format(self.id)
        return self.message
    
    # def message_length(self):
    #     return len(self.message)
    # message_length.short_description = '메세지 글자수' # 추가 컬럼 이름 변경
    # @property 라는 데코레이터로도 동일하게 활용 가능
    # admin에도 구현 가능