import random
from django.db import models
from django.utils.translation import gettext as _
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import User

# Create your models here.


class Question(TimeStampedModel):
    ALLOWED_NUMBER_OF_CORRECT_CHOICES = 1
    html = models.TextField(_('Question Text'))
    is_published = models.BooleanField(_('Has been published?'), default=False, null=False)

    def __str__(self):
        return self.html


class Choice(TimeStampedModel):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    html = models.TextField(_('Choice text'))
    is_correct = models.BooleanField(_('Is this choice correct?'), default=False, null=False)
    MAX_CHOICES_COUNT = 4

    def __str__(self):
        return self.html


class QuizProfile(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_score = models.DecimalField(_('Total Score'), default=0, decimal_places=2, max_digits=10)

    def __str__(self):
        return f'<QuizProfile: user={self.user}>'

    def get_new_question(self):
        used_question_pk = AttemptedQuestion.objects.filter(quiz_profile=self).values_list('question__pk', flat=True)
        remaining_questions = Question.objects.exclude(pk__in=used_question_pk)
        if not remaining_questions.exists():
            return
        return random.choice(remaining_questions)


class AttemptedQuestion(TimeStampedModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    quiz_profile = models.ForeignKey(QuizProfile, on_delete=models.CASCADE, related_name='attempts')
    selected_choice = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True)
    is_correct = models.BooleanField(_('Was this attempt correct?'), default=False, null=False)
    marks_obtained = models.DecimalField(_('Marks Obtained'), default=0, decimal_places=2, max_digits=6)
