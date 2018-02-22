from django.db import models
from django.utils.translation import gettext as _
from model_utils.models import TimeStampedModel

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
