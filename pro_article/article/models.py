from django.db import models


# Create your models here.
class Categary(models.Model):
    Categary_text = models.CharField('栏目名', max_length=50)

    def __str__(self):
        return self.Categary_text


#
#
class Article(models.Model):
    cat = models.ForeignKey(Categary, verbose_name='栏目', null=True, on_delete=models.SET_NULL)
    Article_text = models.CharField('标题', max_length=100)
    Article_url = models.CharField('链接',max_length=300)
    # Article_image=models.ImageField(upload_to='img',verbose_name='图片')
    img_url=models.CharField('图片地址', max_length=500)
    abstract = models.CharField('摘要', max_length=100)
    content = models.CharField('正文', max_length=500)
    pub_date = models.DateTimeField('创建时间')


    def __str__(self):
        return self.Article_text
