from django.db import models

# Create your models here.
from django.db import models

class Bookmanage(models.Manager):
    def all(self):
        return self.filter(is_delete=False).all()

    def show_hero(self,btitle):
        return self.get(btitle=btitle).heroinfo_set.all()

# Create your models here.
class BookInfo(models.Model):
    """图书信息模型类"""
    # 1. 声明表的字段
    btitle = models.CharField(max_length=20, verbose_name='名称')  # varchar()
    bpub_date = models.DateField(verbose_name='发布日期')
    bread = models.IntegerField(default=0, verbose_name='阅读量')
    bcomment = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    image = models.ImageField(upload_to='bookface', verbose_name='图书', null=True)
    # 2. 表的信息设置
    # 默认设置表名：books_bookinfo
    class Meta:
        db_table = "tb_books"
        verbose_name = '图书'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称，中文没有复数情况

    # 3. 自定义功能
    def __str__(self):
        # 开发过程中，经常会打印模型对象，我们可以设置一些打印的文本
        return self.btitle

    def pub_date(self):
        return self.bpub_date.strftime('%Y年%m月%d日')

    pub_date.short_description = '发布日期'
    pub_date.admin_order_field = 'bpub_date'

    objs=Bookmanage()
    objects=models.Manager()

class HeroInfo(models.Model):
    """图书英雄模型类"""
    GENDER_CHOICES = (
        (0, 'male'),   # (数据表中的值，提示信息)  提示信息是后面提供给后台运营admin站点使用。
        (1, 'female')
    )
    hname = models.CharField(max_length=20, verbose_name='名称')
    # 设置字段的选项是每句类型，可以通过 choices选项来设置,choices选项的值是元组结构
    hgender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    hcomment = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    # models.ForeignKey("模型类名", )
    # 一旦设置了模型关联以后，操作的时候，这个hbook就是图书对象，数据保存时图书模型的主键id
    hbook = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')  # 外键
    # 在数据表中，BooleanField字段类型会转换成 0-1
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    image=models.ImageField(upload_to='books', verbose_name='英雄头像', null=True)

    class Meta:
        db_table = 'tb_heros'
        verbose_name = '英雄'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.hname

    def read(self):
        return self.hbook.bcomment

    read.short_description = '图书评论量'
    read.admin_order_field = 'hbook.bcomment'
