from django.db import models
import datetime
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name=u'标题')
    content = models.TextField(verbose_name=u'内容', null=True)
    image = models.ImageField(upload_to='blog/%Y/%m', verbose_name=u'文章图片', max_length=100, null=True, blank=True)
    author = models.CharField(max_length=100, verbose_name=u'作者', default=u'管理员')
    pub_date = models.DateTimeField(default=datetime.datetime.now, verbose_name=u'发表时间')
    update_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u'更新时间')

    class Meta:
        verbose_name = u'新闻'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


