
from django.contrib import admin
from .models import (
    HeaderSlider, 
    PageSlider, 
    PageHeaders, 
    ProgrammsBig, 
    ProgrammsSmall, 
    Reviews, 
    QuestionsAnswers, 
    MenuCategory,
    Menu,
    Customer, 
    Food,
    Cart,
    Order,
    Buy,
    Days 
    )


admin.site.register(QuestionsAnswers)
admin.site.register(Reviews)
admin.site.register(ProgrammsSmall)
admin.site.register(ProgrammsBig)
admin.site.register(PageHeaders)
admin.site.register(PageSlider)
admin.site.register(HeaderSlider)
admin.site.register(MenuCategory)
admin.site.register(Menu)
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(Food)
admin.site.register(Days)




@admin.register(Buy)
class BuyAdmin(admin.ModelAdmin):
     list_display = ('customer', 'phone', 'first_name', 'last_name', 'status', 'created_at', 'display_products')

     



