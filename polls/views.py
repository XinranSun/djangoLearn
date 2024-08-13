from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


# 每个通用视图都需要知道它将对哪个模型执行操作。
# 这是使用 model 属性（在本例中为 model = DetailView 和
# ResultsView 的 Question）或通过定义 get_queryset（） 方法
# （如 IndexView 中所示）提供的。
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


# 默认情况下，DetailView 通用视图使用名为
# <app name>/<model name>_detail.html 的模板。
# 在我们的例子中，它将使用模板“polls/question_detail.html”。
# template_name 属性用于告诉 Django 使用特定的模板名称，
# 而不是自动生成的默认模板名称。
# 我们还指定了结果列表视图的template_name -
# 这可确保结果视图和详细信息视图在呈现时具有不同的外观，
# 即使它们都是幕后的 DetailView。
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
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
