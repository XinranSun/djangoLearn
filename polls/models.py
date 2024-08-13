from django.db import models
from django.utils import timezone
import datetime


# Create your models here.

# 在这里，每个模型都由一个类表示，该类是 django.db.models.Model 的子类。
# 每个模型都有许多类变量，每个类变量都表示模型中的一个数据库字段。
class Question(models.Model):
    question_text = models.CharField(max_length=200)  # 某些 Field 类具有必需的参数。例如，CharField 要求您为其提供max_length。
    # 每个字段都由 Field 类的一个实例表示，
    # 例如，CharField 用于字符字段，DateTimeField 用于日期时间。
    # 这告诉 Django 每个字段包含什么类型的数据。
    pub_date = models.DateTimeField('date published')  # 可以对 Field 使用可选的第一个位置参数来指定人类可读的名称。

    # 每个字段实例的名称（例如question_text或pub_date）是字段的名称，
    # 采用机器友好的格式。
    # 您将在 Python 代码中使用此值，您的数据库将使用它作为列名。
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now()


datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 使用 ForeignKey 定义了关系。
    # 这告诉 Django 每个选择都与一个问题有关。
    # Django 支持所有常见的数据库关系：多对一、多对多和一对一。
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)  # 字段还可以有各种可选参数

    # 要将应用程序包含在我们的项目中，
    # 我们需要在INSTALLED_APPS设置中添加对其配置类的引用。
    # PollsConfig 类位于 polls/apps.py 文件中，因此其虚线路径为 'polls.apps.PollsConfig'。
    # 编辑 mysite/settings.py 文件，并将该虚线路径添加到INSTALLED_APPS设置中。
    def __str__(self):
        return self.choice_text
