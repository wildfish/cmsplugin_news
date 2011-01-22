from django.utils.translation import ugettext_lazy as _

from datetime import datetime
from django.core.urlresolvers import reverse

from cms.utils.navigation import NavigationNode

from cmsplugin_news.models import News

def get_nodes(request):
    res = []

    items = News.published.all()

    years_done = []
    months_done = []
    days_done = []
    slug_done = []

    for item in items:
        date = item.pub_date

        if not date.year in years_done:
            years_done.append(date.year)
            year_node = NavigationNode(date.year, reverse('news_archive_year', kwargs=dict(year=date.year)))
            year_node.childrens = []
            months_done = []
            res.append(year_node)

        if not date.month in months_done:
            months_done.append(date.month)
            month_node = NavigationNode(datetime.strftime(date, '%B'),
                                reverse('news_archive_month', kwargs=dict(
                                    year=date.year,
                                    month=datetime.strftime(date, '%m'))))
            month_node.childrens = []
            days_done = []
            year_node.childrens.append(month_node)

        if not date.day in days_done:
            days_done.append(date.day)
            day_node = NavigationNode(datetime.strftime(date, '%d'),
                                reverse('news_archive_day', kwargs=dict(
                                    year=date.year,
                                    month=datetime.strftime(date, '%m'),
                                    day=datetime.strftime(date, '%d'))))
            day_node.childrens = []
            slug_done = []
            month_node.childrens.append(day_node)

        if not item.slug in slug_done:
            slug_done.append(item.slug)
            item_node = NavigationNode(item.title, item.get_absolute_url())
            item_node.childrens = []
            day_node.childrens.append(item_node)

    return res
