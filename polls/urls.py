from django.urls import path

from . import views

# 教程项目只有一个应用程序，即 polls。
# 在真实的 Django 项目中，可能有 5 个、10 个、20 个应用或更多。
# Django 如何区分它们之间的 URL 名称？
# 例如，投票应用具有详细信息视图，同一项目上的应用也可能用于博客。
# 如何使 Django 在使用 {% url %} 模板标签时知道为 url 创建哪个应用视图？
# polls/urls.py里添加app_name设置命名空间
app_name = 'polls'

# urlpatterns = [
#     path('', views.index, name='index'),
#     # ex: /polls/5/
#     path("specifics/<int:question_id>/", views.detail, name="detail"),
#
#     # ex: /polls/5/results/
#     path("<int:question_id>/results/", views.results, name="results"),
#     # ex: /polls/5/vote/
#     path("<int:question_id>/vote/", views.vote, name="vote"),
# ]

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    # 第二个和第三个模式的路径字符串中匹配模式的名称已从 <question_id> 更改为 <pk>。
    # 这是必要的，因为我们将使用 DetailView 通用视图来替换 detail（） 和 results（） 视图，
    # 并且它期望从 URL 捕获的主键值称为“pk”。
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
