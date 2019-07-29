from django.db import models

#每个模型有一些类变量，它们都表示模型里的一个数据库字段。

class Question(models.Model):
    question_text=models.CharField(max_length=200)#问题的名字
    pub_date = models.DateTimeField('date published')#发布的时间
    def __str__(self):
        return self.question_text


# Create your models here.

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)#该选项属于哪个问题
    choice_text = models.CharField(max_length=200)#该选项的文字
    votes = models.IntegerField(default=0)#获得的票数
    def __str__(self):
        return self.choice_text