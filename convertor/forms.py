from django import forms
from convertor.models import DocxFile


class FileToConvertForm(forms.ModelForm):

    class Meta:
        model = DocxFile
        fields = ['file']
