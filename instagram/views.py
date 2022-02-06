from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView
from .models import Post

def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q', '')
    
    if q:
        qs = qs.filter(message__icontains=q)
    # instagram/templates/instagram/post_list.html
    return render(request, 'instagram/post_list.html', {
        'post_list': qs,
        'q': q,
    })

# def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
#     post = get_object_or_404(Post, pk=pk)
#     # try:
#     #     post = Post.objects.get(pk=pk) # 없는 값을 받았을 때 DoesNotExist 예외 발생
#     # except Post.DoesNotExist:
#     #     raise Http404
    
#     return render(request, 'instagram/post_detail.html',{
#         'post': post,
#     })

post_detail = DetailView.as_view(model=Post)

def archive_year(request, year):
    return HttpResponse(f"{year}년 archives")