from django.contrib import admin

# Register your models here.
from main.models import Shoes





#  可以使用xadmin第三方拓展代替自带的admin模块

class ShoesAdmin(admin.ModelAdmin):
    # 默认情况下显示object对象
    list_display = ['shoe_id', 'shoe_brand', 'shoe_color', 'shoe_size', 'user_id',"create_date"]
    # 修改分页的默认的条数
    list_per_page = 10
    # 搜索字段
    search_fields = ['shoe_brand']

admin.site.register(Shoes, ShoesAdmin)