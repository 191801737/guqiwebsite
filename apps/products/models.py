from django.db import models
import datetime


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'产品名称')
    desc = models.CharField(max_length=300, verbose_name=u'产品描述')
    detail = models.TextField(verbose_name=u'产品详情')
    image = models.ImageField(upload_to='product/%Y/%m', verbose_name=u'封面图片', max_length=100,
                              default='image/default.png')
    tag = models.CharField(default="", max_length=10, verbose_name="产品标签", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'产品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
