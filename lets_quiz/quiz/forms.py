from django import forms
from django.utils.translation import gettext as _
from .models import Question, Choice
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['html', 'is_published']
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
                return

            if form.cleaned_data and form.cleaned_data.get('is_correct') is True:
                correct_choices_count += 1

        try:
            assert correct_choices_count == Question.ALLOWED_NUMBER_OF_CORRECT_CHOICES
        except AssertionError:
            raise forms.ValidationError(_('Exactly one correct choice is allowed.'))


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display username"
        self.fields["email"].label = "Email address"
