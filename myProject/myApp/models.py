# myApp/models.py
from django.db import models

class Book(models.Model):
    # 每个字段都是 Field 类的实例
    # 字符字段是 CharField，日期字段被表示为 DateTImeField
    # 定义某些 Field 类实例需要参数。如上面的 max_length=100 中的 max_length。
    # 这个参数的用处不止于用来定义数据结构，也用于验证数据
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    pub_house = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')