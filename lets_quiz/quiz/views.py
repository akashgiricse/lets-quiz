from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from .models import QuizProfile, Question
# Create your views here.


def home(request):
    context = {}
    return render(request, 'quiz/home.html', context=context)


@login_required
def play(request):
    quiz_profile, created = QuizProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        question_pk = request.POST.get('question_pk')
        question = get_object_or_404(Question, question_pk)
        choice_pk = request.POST.get('choice_pk')

        try:
            selected_choice = question.choices.get(pk=choice_pk)
        except ObjectDoesNotExist:
            raise Http404

        if selected_choice.is_correct:
            pass
    else:
        question = quiz_profile.get_new_question()

        context = {
            'question': question,
        }

        return render(request, 'quiz/play.html', context=context)
