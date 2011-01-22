from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

class NewsApphook(CMSApp):
    name = _("Latest News")
    urls = ["cmsplugin_news.urls"]
    
apphook_pool.register(NewsApphook)
