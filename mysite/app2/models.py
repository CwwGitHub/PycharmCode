from django.db import models

# Create your models here.
class Defect(models.Model):
    #小括号，用来创建元组
    bug_state_choice=(('New','新建'),('Open','打开'),('Fixed','已修复'),('Closed','已关闭'))


    bug_no=models.CharField(null=False,max_length=50,verbose_name='缺陷编号')
    bug_name=models.CharField(null=False, max_length=50, verbose_name='缺陷标题')
    bug_desc=models.CharField(max_length=500, verbose_name='缺陷描述')
    bug_state=models.CharField(max_length=10, default="New",choices=bug_state_choice,verbose_name='缺陷编号')

    class Meta:
        verbose_name='缺陷报告'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.bug_name
    