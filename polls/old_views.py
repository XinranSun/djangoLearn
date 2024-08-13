from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from polls.models import Question, Choice


# Create your views here.
# 每个视图负责执行以下两项操作之一：
# 返回包含所请求页面内容的 HttpResponse 对象，
# 或引发异常（如 Http404）。剩下的就看你了。


# 您的视图可以从数据库中读取记录，也可以不读取。
# 它可以使用模板系统，例如 Django 的模板系统，
# 也可以使用第三方 Python 模板系统，也可以不使用。
# 它可以生成 PDF 文件、输出 XML、动态创建 ZIP 文件、
# 任何您想要的内容、使用您想要的任何 Python 库。

# All Django wants is that HttpResponse.
# Or an exception.
def index(request):
    # return HttpResponse("Hello, wo123rld. You're at the polls index.")
    latest_question_list = Question.objects.order_by("-pub_date")[:5]

    context = {"latest_question_list": latest_question_list}

    # output = ", ".join([q.question_text for q in latest_question_list])

    # 页面的设计在视图中是硬编码的。
    # 如果要更改页面的外观，则必须编辑此 Python 代码。
    # 因此，让我们使用 Django 的模板系统，
    # 通过创建一个视图可以使用的模板，将设计与 Python 分开。

    # 该代码加载名为 polls/index.html 的模板，并向其传递上下文。
    # 上下文是一个字典，将模板变量名称映射到 Python 对象。

    # template = loader.get_template("polls/index.html")
    # return HttpResponse(template.render(context, request))

    # render()快捷方式->常用习惯(common idiom)
    # 请注意，一旦我们在所有这些视图中都完成了此操作，
    # 就不再需要导入 loader 和 HttpResponse
    # （如果您仍然有用于详细信息、结果和投票的存根方法，您将需要保留 HttpResponse）。

    return render(request, "polls/index.html", context)
    #  render()函数将请求对象作为其第一个参数，模板名称作为其第二个参数，
    #  一个字典作为其可选的第三个参数。
    #  它返回使用给定上下文呈现的给定模板的 HttpResponse 对象。


def detail(request, question_id):
    # return HttpResponse("You're looking at question %s." % question_id)

    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    # get_object_or_404（） 函数将 Django 模型作为其第一个参数和任意数量的关键字参数，
    # 并将其传递给模型管理器的 get（） 函数。如果对象不存在，它将引发 Http404。

    # 还有一个 get_list_or_404（） 函数，它的工作原理与 get_object_or_404（） 一样
    # ——除了使用 filter（） 而不是 get（）。如果列表为空，则引发 Http404。
    return render(request, "polls/detail.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # 是一个类似字典的对象，允许您按键名称访问提交的数据。
        # 在本例中，请求。POST['choice'] 以字符串形式返回所选选项的 ID.请求。
        # POST 值始终是字符串
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
        # 如果 POST 数据中未提供选择，则会引发 KeyError。
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
        # 在成功处理 POST 数据后，您应该始终返回 HttpResponseRedirect。


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})
