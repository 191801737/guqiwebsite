from django.db import models
import datetime


from DjangoUeditor.models import UEditorField
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='标题')
    content = UEditorField(verbose_name='内容', width=600, height=300, toolbars="full", imagePath="blog/ueditors/",
                           filePath="blog/ueditors/", default='')
    image = models.ImageField(upload_to='blog/%Y/%m', verbose_name='封面图', max_length=100, default='image/default.png',
                              null=True, blank=True)
    author = models.CharField(max_length=100, verbose_name='作者', default='管理员')
    pub_date = models.DateTimeField(default=datetime.datetime.now, verbose_name='发表时间')
    update_time = models.DateTimeField(default=datetime.datetime.now, verbose_name='更新时间')

    class Meta:
        verbose_name = '新闻'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # delete old file when replacing by updating the file
        try:
            this = Article.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except:
            pass  # when new photo then we do nothing, normal case
        super(Article, self).save(*args, **kwargs)


class Case(models.Model):
    title = models.CharField(max_length=256, verbose_name='标题')
    desc = models.CharField(max_length=256, verbose_name='描述', default="")
    content = UEditorField(verbose_name='内容', width=600, height=300, toolbars="full", imagePath="blog/ueditors/",
                           filePath="blog/ueditors/", default='')
    image = models.ImageField(upload_to='blog/%Y/%m', verbose_name='封面图', max_length=100, default='image/default.png',
                              null=True, blank=True)
    author = models.CharField(max_length=100, verbose_name='发布人', default='管理员')
    pub_date = models.DateTimeField(default=datetime.datetime.now, verbose_name='发表时间')
    update_time = models.DateTimeField(default=datetime.datetime.now, verbose_name='更新时间')

    class Meta:
        verbose_name = '成功案例'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # delete old file when replacing by updating the file
        try:
            this = Case.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except:
            pass  # when new photo then we do nothing, normal case
        super(Case, self).save(*args, **kwargs)


class Introduce(models.Model):
    title = models.CharField(max_length=256, verbose_name='标题', null=True, blank=True)
    content = UEditorField(verbose_name='公司简介', width=600, height=300, toolbars="full", imagePath="blog/ueditors/",
                           filePath="blog/ueditors/", default='')
    culture = UEditorField(verbose_name='企业文化', width=600, height=300, toolbars="full", imagePath="blog/ueditors/",
                           filePath="blog/ueditors/", default='')
    idea = UEditorField(verbose_name='经营理念', width=600, height=300, toolbars="full", imagePath="blog/ueditors/",
                        filePath="blog/ueditors/", default='')
    contact = UEditorField(verbose_name='联系我们', width=600, height=300, toolbars="full", imagePath="blog/ueditors/",
                           filePath="blog/ueditors/", default='')
    pub_date = models.DateTimeField(default=datetime.datetime.now, verbose_name='发表时间')
    update_time = models.DateTimeField(default=datetime.datetime.now, verbose_name='更新时间')

    class Meta:
        verbose_name = '关于我们'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
