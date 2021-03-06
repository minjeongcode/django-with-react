from django.urls import path, re_path, register_converter

from instagram.converters import YearConverter, MonthConverter, DayConverter

from instagram import views

register_converter(YearConverter, 'year')
register_converter(MonthConverter, 'month')
register_converter(DayConverter, 'day')

app_name = 'instagram' # URL Reverse에서 namespace역할을 하게 됨.

urlpatterns = [
    path('new', views.post_new, name='post_new'),
    path('<int:pk>/edit', views.post_edit, name='post_edit'),
    
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    # re_path(r'(?P<pk>\d+)/$', views.post_detail),
    # path('archives/<int:year>', views.archive_year),
    # re_path(r'archives/(?P<year>20\d{2})', views.archive_year),
    # path('archives/<year:year>', views.archive_year),
    path('archive/', views.post_archive, name='post_archive'),
    path('archive/<year:year>/', views.post_archive_year, name='post_archive_year'),
    # path('archive/<year:year>/<month:month>', views.post_archive_month, name='post_archive_month'),
    # path('archive/<year:year>/<month:month>/<day:day>', views.post_archive_day, name='post_archive_day'),
]
