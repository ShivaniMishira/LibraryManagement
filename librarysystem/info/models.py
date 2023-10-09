from django.db import models
# Create your models here.
class Books(models.Model):
   
    name=models.CharField(max_length=30)
    publish=models.CharField(max_length=20)
    author=models.CharField(max_length=40)
    category=models.CharField(max_length=30,)
    language=models.CharField(max_length=30,)
    stock=models.IntegerField(default=0)
    class Meta:
        db_table = "Books"


class Issue (models.Model):
    Sname =  models.CharField(max_length=50)
    Sid = models.IntegerField(default=0)
    Bname = models.CharField(max_length=50)
    Bid =  models.IntegerField(default=0)
    date = models.DateField(null=True)
    expiry = models.DateField(null=True)
    class Meta:
        db_table = "Issue"


class Sub (models.Model):
    Stu = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    plan = models.CharField(max_length=20)
    Duration = models.DurationField()
    class Meta:
        db_table = "Sub"

#parent model
class Student(models.Model):
    name=models.CharField(max_length=200,default="anonymous" )
    email=models.CharField(max_length=200,null=True)
    password = models.CharField(max_length=20, unique=True)
    stock = models.IntegerField(default=0)
    issue = models.IntegerField(default=0)
    bname = models.CharField(max_length=50, default=0)
    subscrib = models.ForeignKey(Sub,null=True,on_delete=models.CASCADE)
    class Meta:
        db_table = "Student"
    
    
class Post(models.Model):
    name_user = models.CharField(max_length=200)
    post_id = models.AutoField
    post_content = models.CharField(max_length=5000)
    timestamp= models.DateTimeField(auto_now_add=True)
    #image = models.ImageField(upload_to="images",default="")
    class Meta:
        db_table = "Post"
    
class Replie(models.Model):
    name_user = models.CharField(max_length=200)
    reply_id = models.AutoField
    reply_content = models.CharField(max_length=5000) 
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default='')
    timestamp= models.DateTimeField(auto_now_add=True)
    #image = models.ImageField(upload_to="images",default="")
    class Meta:
        db_table = "Replie"

