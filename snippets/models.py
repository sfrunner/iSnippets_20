from django.db import models

# Create your models here.
class Snippet(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 80,null = False,blank = False)
    language = models.CharField(max_length = 50,null = False,blank = False)
    codeSnippet = models.TextField(max_length = 2000,null = False,blank = False)
    description = models.TextField(max_length = 2000)
    author = models.CharField(max_length = 100,null = False,blank = False)
    dateCreated = models.DateField(auto_now_add=True)

    def __str__(self):
        return self. title + " " + (self.language) + " by "  + self.author