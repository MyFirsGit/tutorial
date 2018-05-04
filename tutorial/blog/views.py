# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
import datetime
# Create your views here.

def Test(request):
	return render(request,'blog/test.html',{'current_time':datetime.date.today()})
