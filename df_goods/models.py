from django.db import models

# Create your models here.
'''
     商品分类信息  水果 海鲜等
        TypeInfo：title名称
        具体商品信息
        GoodsInfo：gtitle名称 gpic图片 gprice价格 gunit商品单位 
                   gclick点击量 gjianjie简介 gkucun库存 gcontent介绍 
                   gtype分类(TypeInfo)
'''
#商品分类信息
class TypeInfo(models.Model):
    isDelete = models.BooleanField(default=False)  #逻辑
    title = models.CharField(max_length=20)
    def __str__(self):
        return self.title



class GoodsInfo(models.Model):
    isDelete = models.BooleanField(default=False)
    gtitle = models.CharField(max_length=20)
    gpic = models.ImageField(upload_to='df_goods') #关联图片目录
    gprice = models.DecimalField(max_digits=5,decimal_places=2) #商品价格总共五位数，两位小数
    gunit = models.CharField(max_length=20,default='500g') #商品单位kg或个数
    gclick = models.IntegerField() #商品点击量
    gjianjie = models.CharField(max_length=200)#商品简介
    gkucun = models.IntegerField() #商品库存
    gcontent = models.CharField(max_length=200)#商品介绍（与案例不同）
    gtype = models.ForeignKey(TypeInfo,on_delete=models.CASCADE)

    def __str__(self):
        return self.gtitle