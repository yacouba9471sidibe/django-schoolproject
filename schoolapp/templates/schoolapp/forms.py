from django import forms
from .models import Women, Category, TagPost

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Women
        fields = ['title', 'slug', 'content', 'is_published', 'cat', 'tags', 'photo']
        labels = {
            'title': 'Заголовок',
            'slug': 'URL',
            'content': 'Контент',
            'is_published': 'Статус',
            'cat': 'Категория',
            'tags': 'Теги',
            'photo': 'Фото',
        }
        widgets = {
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
            'tags': forms.CheckboxSelectMultiple(),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 3:
            raise forms.ValidationError("Заголовок должен содержать минимум 3 символа.")
        if "спам" in title.lower():
            raise forms.ValidationError("Заголовок не должен содержать слово 'спам'.")
        return title

    def clean_slug(self):
        slug = self.cleaned_data['slug']
        if slug.isdigit():
            raise forms.ValidationError("URL не может состоять только из цифр.")
        return slug

class UploadFileForm(forms.Form):
    file = forms.FileField(label="Выберите файл")