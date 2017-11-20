# website

## 笔记

### apps 介绍
blog  新闻发布
contents 内容app
operation 用户操作
users 用户管理



# 文章表
class Article(models.Model):
    title = models.CharField(max_length=100, null=False)  # 标题
    intro = models.CharField(max_length=1000)  # 导语
    abstract = models.TextField()  # 摘要
    category = models.ForeignKey(Category, related_name="cate") #连接分类表的外键，多对一关系
    content = models.TextField(null=False)  # 内容
    publish_time = models.DateTimeField(null=False, default=now)  # 发布时间
    image = models.FileField(upload_to=‘article_image‘)  # 文章配图
    source_link = models.CharField(max_length=200)  # 原文链接
    author_name = models.CharField(max_length=100, null=False)  # 作者名字
    author_avatar = models.FileField(upload_to=‘author_avatar‘)  # 作者头像
    author_desc = models.CharField(max_length=100, null=False)  # 作者签名

    def __str__(self):
        return self.title


