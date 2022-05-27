from django.db import models
from django.urls import reverse
from django.utils import timezone
#from django_countries.fields import CountryField

# Create your models here.

# https://docs.djangoproject.com/en/1.10/_modules/django/db/models

# 可以理解为定义表

class News(models.Model):
    
    # 此处定义的可以理解为表的列 具体的参数参考文档

    newsId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=45)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, blank=True)
    kind = models.ForeignKey('Kind', on_delete=models.SET_NULL, null=True)
    text = models.TextField(null=True)
    tags = models.ManyToManyField('Tags')
    time = models.DateTimeField(default=timezone.now)

    # 此处的定义可以理解为这个表的默认排序方式

    class Meta:
        ordering = ['time']

    # 此处定义的是我们在页面中显示的内容

    def __str__(self):
        return '{} - {}'.format(self.title, self.author)

    # 此处定义的是我们点进这个 News 之后进入的具体描述的页面的 url

    def get_absolute_url(self):
        # 这个 reverse 意思是逆着这个 'news-detail'的名字去追踪 url
        return reverse('news-detail', args=[self.id])


class Author(models.Model):

    authorId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    # gender = models.CharField(choices=[('f', 'Female'), ('m', 'Male')], max_length=1)
    # nationality = CountryField(null=True, blank=True) 这个需要包 django-countries
    nationality = models.CharField(max_length=45, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['nationality', 'name']

    def __str__(self):
        return self.name


class Kind(models.Model):

    name = models.CharField(max_length=45)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Tags(models.Model):

    name = models.CharField(max_length=45)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
