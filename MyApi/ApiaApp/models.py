from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class tbl_topics(models.Model):
    topic_id = models.AutoField(primary_key=True)
    topic_name = models.CharField(max_length=50)
    topic_desc = models.CharField(max_length=200)
    topic_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topic_name

class tbl_comments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    topic_id = models.ForeignKey(tbl_topics, on_delete=models.CASCADE, related_name='comment')
    comment_name = models.CharField(max_length=50)
    comment_desc = models.CharField(max_length=200)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_name