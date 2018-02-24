import random
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import QuizProfile
# Create your views here.


def home(request):
    context = {}
    return render(request, 'quiz/home.html', context=context)


@login_required
def play(request):
    quiz_profile, created = QuizProfile.objects.get_or_create(user=request.user)
    question = quiz_profile.get_new_question()

    context = {
        'question': question,
    }
    return render(request, 'quiz/play.html', context=context)
