from django import forms
from .models import Question, Choice
from django.utils.translation import gettext as _


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['html', ]
        widgets = {
            'html': forms.Textarea(attrs={'rows': 3, 'cols': 80}),
        }


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['html', 'is_correct']
        widgets = {
            'html': forms.Textarea(attrs={'rows': 2, 'cols': 80}),
        }


class ChoiceInlineFormset(forms.BaseInlineFormSet):
    def clean(self):
        super(ChoiceInlineFormset, self).clean()

        correct_choices_count = 0
        for form in self.forms:
            if not form.is_valid():
                return  # other error exist, so don't bother
            if form.cleaned_data and form.cleaned_data.get('is_correct') is True:
                correct_choices_count += 1
        try:
            assert correct_choices_count == 1
        except AssertionError:
            raise forms.ValidationError(_('Exactly one correct answer is allowed.'))
