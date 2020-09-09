from django.contrib import admin
from .models import HeaderSlider, PageSlider, PageHeaders, ProgrammsBig, ProgrammsSmall, MenuSlider, Reviews, QuestionsAnswers, Days, MenuList


admin.site.register(MenuList)
admin.site.register(Days)
admin.site.register(QuestionsAnswers)
admin.site.register(Reviews)
admin.site.register(MenuSlider)
admin.site.register(ProgrammsSmall)
admin.site.register(ProgrammsBig)
admin.site.register(PageHeaders)
admin.site.register(PageSlider)
admin.site.register(HeaderSlider)
