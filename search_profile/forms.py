from django.forms import ModelForm
from .models import SearcUser


class SearchForm(ModelForm):
    class Meta:
        # эта форма будет работать с моделью Book
        model = SearcUser
        # на странице формы будут отображаться поля 'name', 'isbn' и `pages`
        fields = ['name']