from django.db import models

# Create your models here.


class Shoes(models.Model):
    shoe_id = models.AutoField("编号",primary_key=True)
    shoe_brand = models.CharField("鞋子品牌",max_length=100)
    shoe_color = models.CharField("鞋子颜色",max_length=50)
    shoe_size = models.DecimalField("鞋子尺寸",decimal_places=1,max_digits=3)
    is_delete = models.BooleanField(default=False)
    create_date = models.DateTimeField("创建时间",auto_now_add=True)
    # 也可以使用外键
    user_id = models.IntegerField("用户编号")

    class Meta:
        db_table="shoes"
        ordering = ('create_date',)
        verbose_name = '鞋'
        verbose_name_plural = verbose_name

