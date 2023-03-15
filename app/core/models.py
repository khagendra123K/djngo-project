from django.db import models



class Category(models.Model):
    Category=models.CharField(max_length=50)

    def __str__(self):
        return self.Category
    

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=200, default=0)
    category=models.ForeignKey(Category,on_delete= models.CASCADE,blank = True, null = True)
    created= models.DateTimeField(auto_now = True, blank = True)
    update= models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.title
    
