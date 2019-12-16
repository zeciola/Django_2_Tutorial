from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import render, get_object_or_404

from .models import Question


def index(request: HttpRequest) -> HttpResponse:
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request=request, template_name='polls/index.html', context=context)


def detail(request: HttpRequest, question_id: int) -> HttpResponse:
    question = get_object_or_404(Question, pk=question_id)

    return render(
        request=request,
        template_name='polls/detail.html',
        context=dict(question=question)
    )


def results(request: HttpRequest, question_id: int) -> HttpResponse:
    response = f"Você está vendo os resultados da pesquisa de número: {question_id}"

    return HttpResponse(response)


def vote(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse(
        f'Você votou na pesquisa de número: {question_id}'
    )
