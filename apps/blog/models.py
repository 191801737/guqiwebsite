from django.db import models
import datetime


from DjangoUeditor.models import UEditorField
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name=u'标题')
    content = UEditorField(verbose_name=u'内容', width=600, height=300, toolbars="full", imagePath="blog/ueditor",
                           filePath="blog/ueditor", upload_settings={"imageMaxSize": 1204000}, default='')
    image = models.ImageField(upload_to='blog/%Y/%m', verbose_name=u'文章图片', max_length=100, default='image/default.png')
    author = models.CharField(max_length=100, verbose_name=u'作者', default=u'管理员')
    pub_date = models.DateTimeField(default=datetime.datetime.now, verbose_name=u'发表时间')
    update_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u'更新时间')

    class Meta:
        verbose_name = u'新闻'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


