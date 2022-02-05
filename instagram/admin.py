from django.contrib          import admin
from django.utils.safestring import mark_safe

from .models        import Post, Comment

# 첫번째 방법
# admin.site.register(Post)

# 두번째 방법
# class PostAdmin(admin.ModelAdmin):
#     pass

# admin.site.register(Post, PostAdmin)

# 세번째 방법(주로 사용하는 방법)
# list_display : 모델 리스트에 출력할 컬럼 지정
# list_display_links : list_display 지정된 이름 중에, detail 링크를 걸 속성 리스트
# search_fields : admin내 검색 UI를 통해, DB를 통한 where 쿼리 대상 필드 리스트
# list_filter : 지정 필드값으로 필터링 옵션 제공
@admin.register(Post) # Wrapping
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo_tag', 'message', 'message_length', 'is_public', 'created_at', 'updated_at']
    list_display_links = ['message']
    list_filter = ['created_at', 'is_public']
    search_fields = ['message']
    
    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" style="width: 70px;" />')
        return None
    def message_length(self, post):
        return f'{len(post.message)} 글자'
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass