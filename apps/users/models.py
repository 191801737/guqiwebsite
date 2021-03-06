from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u'昵称', default='')
    birthday = models.DateField(verbose_name=u'生日', null=True, blank=True)
    gender = models.CharField(max_length=10, choices=(("male", u'男'), ('female', u'女')), default='female')
    address = models.CharField(max_length=100, default=u'')
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(max_length=100, upload_to='image/%Y/%m', verbose_name=u'头像', default='image/default.png')

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        # delete old file when replacing by updating the file
        try:
            this = UserProfile.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except:
            pass  # when new photo then we do nothing, normal case
        super(UserProfile, self).save(*args, **kwargs)


class IndexBanner(models.Model):
    """首页背景图"""
    image = models.ImageField(max_length=100, upload_to='banner/%Y/%m', verbose_name=u'首页背景',default='image/default.png', null=True, blank=True)
    url = models.URLField(max_length=200, verbose_name=u'访问地址', null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u"首页背景图"
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs):
        # delete old file when replacing by updating the file
        try:
            this = IndexBanner.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except:
            pass  # when new photo then we do nothing, normal case
        super(IndexBanner, self).save(*args, **kwargs)


class ProductBanner(models.Model):
    """产品轮播图"""
    title = models.CharField(max_length=100, verbose_name='标题', null=True, blank=True)
    image = models.ImageField(max_length=100, upload_to='banner/%Y/%m', verbose_name='产品轮播图',default='image/default.png', null=True, blank=True)
    url = models.URLField(max_length=200, verbose_name='访问地址')
    index = models.IntegerField(default=100, verbose_name='顺序', null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = "产品轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # delete old file when replacing by updating the file
        try:
            this = ProductBanner.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except:
            pass  # when new photo then we do nothing, normal case
        super(ProductBanner, self).save(*args, **kwargs)


class CaseBanner(models.Model):
    """成功案例轮播图"""
    title = models.CharField(max_length=100, verbose_name='标题', null=True, blank=True)
    image = models.ImageField(max_length=100, upload_to='banner/%Y/%m', verbose_name='案例轮播图', default='image/default.png', null=True, blank=True, )
    url = models.URLField(max_length=200, verbose_name='访问地址')
    index = models.IntegerField(default=100, verbose_name='顺序', null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = "案例轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # delete old file when replacing by updating the file
        try:
            this = CaseBanner.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except:
            pass  # when new photo then we do nothing, normal case
        super(CaseBanner, self).save(*args, **kwargs)
