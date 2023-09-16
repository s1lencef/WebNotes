from .models import Review,TaskName,Inter_Task
from django.forms import ModelForm, FileInput,TextInput,HiddenInput,CheckboxInput
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class AddReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['text']
        widgets = {
            'text': TextInput(),
        }
        help_texts = {
            'text':None
        }

    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        super().__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.instance.author = self.author
        return super().save(*args, **kwargs)

class NewGlobalTaskForm(ModelForm):
    class Meta:
        model = TaskName
        fields = ['name']
        widgets = {
            'name':TextInput(attrs={'class': 'global_form'})
        }
        help_texts = {
            'name':None
        }

    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        super().__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.instance.author = self.author
        return super().save(*args, **kwargs)

class NewInterTaskForm(ModelForm):
    class Meta:
        model = Inter_Task
        fields = ['task_text']
        widgets = {
            'task_text':TextInput(attrs={'placeholder': 'Enter intermediate task'})
        }
        help_texts = {
            'task_text':None
        }

    def __init__(self, *args, **kwargs):
        self.global_task_id= kwargs.pop('global_task_id', None)
        super().__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.instance.global_task_id = self.global_task_id
        return super().save(*args, **kwargs)