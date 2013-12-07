from django.contrib import admin
from firstapp.models import OSCUser, Book, Cat


class OSCUserAdmin(admin.ModelAdmin):
    # fields = (('name','sex'),'blog')
    # exclude = ('age',)
    pass


class BookAdmin(admin.ModelAdmin):
    # list_display = ('owner',)
    # search_fields = ('book_name', )
    # # date_hierarchy = 'date'
    # ordering = ('-owner__age',)
    # raw_id_fields = ('owner',)
    # filter_horizontal = ('learner',)
    pass


admin.site.register(OSCUser,OSCUserAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Cat)