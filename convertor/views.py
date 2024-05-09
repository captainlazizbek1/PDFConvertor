from django.shortcuts import render
from django import views
from convertor.forms import FileToConvertForm
from convertor.models import DocxFile
import docx2pdf
from django.http import HttpResponse, FileResponse
from django.conf import settings
import pythoncom
import os
from django.utils.encoding import smart_str


class ConvertorView(views.View):

    def post(self, request):
        form = FileToConvertForm(request.POST, request.FILES)
        if form.is_valid():
            pythoncom.CoInitialize()
            file = form.cleaned_data['file']
            docx_file = DocxFile.objects.create(file=file)
            docx_file.save()
            file_path = os.path.basename(docx_file.file.path)
            file_path = file_path.replace('.docx', '.pdf')
            output_path = settings.MEDIA_ROOT + file_path
            docx2pdf.convert(docx_file.file.path, output_path)
            converted_file = DocxFile.objects.create(file=output_path)
            converted_file.save()
            # print(converted_file.file.url)
            # context = {
            #     'form': form,
            #     'converted_file': converted_file,
            #     'file_path': file_path
            # }
            # return render(request, 'convertor.html', context)
            response = FileResponse(open(output_path, 'rb'))
            response['Content-Disposition'] = f'attachment; filename="{smart_str(output_path)}"'
            return response
        else:
            return HttpResponse('File is not valid')

    def get(self, request):
        pythoncom.CoInitialize()
        form = FileToConvertForm()
        return render(request, 'convertor.html', {'form': form})


