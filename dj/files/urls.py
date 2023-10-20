from django.urls import path
from django.conf.urls.static import static

from files.views import UploadFile, FileList

from dj.settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path('upload/', UploadFile.as_view()),
    path('files/', FileList.as_view()),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)