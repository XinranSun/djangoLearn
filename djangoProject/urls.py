"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# include 配置全局URLconf,以包含polls.urls 中定义的 URLconf。
from django.urls import path, include

# 在包含其他 URL 模式时，应始终使用 include（）。


urlpatterns = [
    # path(route,view,kwargs,name)

    # 每当 Django 遇到 include（） 时，
    # 它会切断到该点匹配的 URL 的任何部分，
    # 并将剩余的字符串发送到包含的 URLconf 进行进一步处理。
    path('polls/', include('polls.urls')),

    # admin.site.urls 是唯一的例外。
    # include（） 函数允许引用其他 URLconf。
    path('admin/', admin.site.urls),

]
