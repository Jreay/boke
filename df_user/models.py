from django.db import models

'''
  用户信息
        Userinfo: username名字 password密码 useremail邮箱 userreceipt收货地址 useraddress地址 usercode uphone电话
        商品浏览：用户浏览过的商品
        GoodsBrowser: user用户名(UserInfo) good商品(GoodsInfo)
'''
# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=40)
    useremail = models.CharField(max_length=30)
    userreceipt = models.CharField(max_length=20,default="")
    useraddress = models.CharField(max_length=100,default="")
    usercode = models.CharField(max_length=6,default="")
    userphone = models.CharField(max_length=11,default="")
    # default,blank是python层面的约束，不影响数据库表结构，修改时不需要迁移 python manage.py makemigrations

class GoodsBrowser(models.Model):
    user = models.ForeignKey('UserInfo',on_delete=models.CASCADE)
    good = models.ForeignKey('df_goods.GoodsInfo',on_delete=models.CASCADE)



