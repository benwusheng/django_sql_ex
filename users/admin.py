from django.contrib import admin
from users.models import BookInfo,HeroInfo

# Register your models here.

class HeroInfoStackInLine(admin.StackedInline):
    model = HeroInfo
    extra = 1

# class HeroInfoTabularInline(admin.TabularInline):
#     model = HeroInfo
#     extra = 1

class BookInfoAdmin(admin.ModelAdmin):
    list_per_page = 3
    actions_on_bottom = True

    list_display = ['id','btitle','pub_date']

    # fields = ['btitle','pub_date']

    fieldsets = (
        ('基本', {'fields': ['btitle', 'bpub_date']}),
        ('高级', {
            'fields': ['bread', 'bcomment'],
            'classes': ('collapse',)  # 是否折叠显示
        })
    )

    inlines = [HeroInfoStackInLine]

    # inlines = [HeroInfoTabularInline]


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id','hname','hcomment','hbook','read']

    list_filter = ['hbook','hgender']
    search_fields = ['hname','hcomment']




admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)


admin.site.site_header = '传智书城'
admin.site.site_title = '传智书城MIS'
admin.site.index_title = '欢迎使用传智书城MIS'