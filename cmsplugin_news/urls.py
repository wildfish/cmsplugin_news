from django.conf.urls.defaults import *

from cmsplugin_news.models import News

news_info_dict = {
    'queryset': News.published.all(),
    'date_field': 'pub_date',
}

news_info_month_dict = {
    'queryset': News.published.all(),
    'date_field': 'pub_date',
    'month_format': '%m',
}

urlpatterns = patterns('django.views.generic.date_based',
    (r'^$', 
        'archive_index', news_info_dict, 'news_archive_index'),
    
    (r'^(?P<year>\d{4})/$', 
        'archive_year', news_info_dict, 'news_archive_year'),
    
    (r'^(?P<year>\d{4})/(?P<month>\d{2})/$', 
        'archive_month', news_info_month_dict, 'news_archive_month'),
    
    (r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', 
        'archive_day', news_info_month_dict, 'news_archive_day'),
    
    (r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 
        'object_detail', news_info_month_dict, 'news_detail'),
)

