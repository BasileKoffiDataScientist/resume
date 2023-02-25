from django.shortcuts import render

# Create your views here.
from django.http import FileResponse
from django.conf import settings
import os

import os
from django.conf import settings
from django.http import FileResponse


def download_cv(request):
    # Obtenez le chemin d'accès complet au fichier PDF
    cv_path = os.path.join(settings.MEDIA_ROOT, 'CV_BasileKoffi_DataScientist_en.pdf')

    # Ouvrez le fichier PDF en mode binaire
    cv_file = open(cv_path, 'rb')

    # Créez une réponse HTTP en utilisant la méthode FileResponse
    response = FileResponse(cv_file, content_type='application/pdf')

    # Définissez le nom de fichier pour la réponse
    response['Content-Disposition'] = 'attachment; filename="cv_BasileKoffi.pdf"'

    return response


# def download_cv(request):
#     cv_path = os.path.join(settings.BASE_DIR, 'path', 'to', 'cv.pdf')
#     cv_file = open(cv_path, 'rb')
#     response = FileResponse(cv_file, content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="cv.pdf"'
#     return response


def index_view(request):
    return render(request, 'cvApp/index.html')


def contact_view(request):
    return render(request, 'cvApp/contact.html')


def resume_view(request):
    return render(request, 'cvApp/resume.html')


def about_view(request):
    return render(request, 'cvApp/about.html')