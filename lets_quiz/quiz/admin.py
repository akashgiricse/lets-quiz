from django.contrib import admin

from .models import Question, Choice
from .forms import QuestionForm, ChoiceForm, ChoiceInlineFormset
# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice

    can_delete = False
    max_num = Choice.MAX_CHOICES_COUNT
    min_num = Choice.MAX_CHOICES_COUNT
    form = ChoiceForm
    formset = ChoiceInlineFormset


class QuestionAdmin(admin.ModelAdmin):
    model = Question
    inlines = (ChoiceInline, )
    actions = None

    form = QuestionForm

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Question, QuestionAdmin)
