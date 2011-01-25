from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ungettext
from django.contrib import admin

from django.http import HttpResponse
from django.core import serializers

from cmsplugin_news.forms import NewsForm
from cmsplugin_news.models import News

class NewsAdmin(admin.ModelAdmin):
    """
        Admin for news
    """
    date_hierarchy = 'pub_date'
    list_display = ('slug', 'title', 'is_published', 'pub_date', 'author')
    #list_editable = ('title', 'is_published')
    list_filter = ('is_published', )
    search_fields = ['title', 'excerpt', 'content']
    prepopulated_fields = {'slug': ('title',)}
    current_user_field = 'author' # will prepopulate this field when adding a new item
    form = NewsForm

    actions = ['make_published', 'make_unpublished']

    save_as = True
    save_on_top = True

    def queryset(self, request):
        """
            Override to use the objects and not just the default visibles only.
        """
        return News.objects.all()
 
    def add_view(self, request, form_url='', extra_context=None):
        # set the current user so that we can prepopulate the author field
        self._current_user = request.user
        return super(NewsAdmin, self).add_view(request, form_url, extra_context)

    def formfield_for_dbfield (self, db_field, **kwargs): 
        field = super(NewsAdmin, self).formfield_for_dbfield(db_field, **kwargs)

        # if we have a _current_user then preselect the currently logged in user
        if hasattr(self, '_current_user') and db_field.name == self.current_user_field:
            field.initial = self._current_user.pk 
        return  field
    
    def make_published(self, request, queryset):
        """
            Marks selected news items as published
        """
        rows_updated = queryset.update(is_published=True)
        self.message_user(request, ungettext('%(count)d newsitem was published',
                                            '%(count)d newsitems where published',
                                            rows_updated) % {'count': rows_updated})
    make_published.short_description = _('Publish selected news')

    def make_unpublished(self, request, queryset):
        """
            Marks selected news items as unpublished
        """
        rows_updated =queryset.update(is_published=False)
        self.message_user(request, ungettext('%(count)d newsitem was unpublished',
                                            '%(count)d newsitems where unpublished',
                                            rows_updated) % {'count': rows_updated})
    make_unpublished.short_description = _('Unpublish selected news')

admin.site.register(News, NewsAdmin)
