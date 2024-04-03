from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question, Choice
from django.template import loader

def cafe_category(request):
    all_questions = Question.objects.all()
    context = {"all_questions": all_questions}
    return render(request, "polls/category.html", context)

def category_detail(request, question_id):
    category = get_object_or_404(Question, pk=question_id)
    choices = category.choice_set.all()
    return render(request, 'polls/category_detail.html', {'category': category, 'choices': choices})