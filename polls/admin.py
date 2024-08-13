from django.contrib import admin

# Register your models here.
from .models import Question

admin.site.register(Question)
# 我们的投票应用程序在哪里？它不会显示在管理员索引页面上。
# 我们需要告诉管理员 Question 对象有一个管理员界面。
