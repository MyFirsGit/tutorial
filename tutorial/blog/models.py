# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from DjangoUeditor.models import UEditorField
# Create your models here.

class Article(models.Model):
	title = models.CharField(u"简历标题",max_length = 100)
	
	pub_date = models.DateTimeField(u"发布日期",auto_now_add = True, editable= True)
	update_time = models.DateTimeField(u"更新时间",auto_now = True,null = True)
	content = UEditorField(u"简历内容",height = 300,width=1000,default=u'',blank=True,imagePath="uploads/blog/images",toolbars='besttome',filePath='uploads/blog/files')
# models.TextField(blank = True, null = True)	



	def __unicode__(self):
		return self.title
	
	class Meta:
		ordering = ['-update_time']
		verbose_name = "简历"
		verbose_name_plural = "简历"
