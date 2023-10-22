import os
from PIL import Image, ImageFilter
import fitz

from dj.celery import app

from dj.settings import MEDIA_ROOT
from files.models import File


@app.task
def process_file(file_id):
    """
    Обработка изображений и pdf-файлов
    """
    file = File.objects.get(id=file_id)
    file_path = file.file.path
    file_ext = os.path.splitext(file_path)[1]
    try:
        if file_ext in ['.jpg', '.png', '.jpeg']:
            # Блюр и чб изображения
            with Image.open(file_path) as img:
                img.load()
            blured_img = img.filter(ImageFilter.BoxBlur(5))
            gray_scaled = blured_img.convert("CMYK").convert("L")
            gray_scaled.save(file_path)
        elif file_ext == '.pdf':
            # Считывание текста в txt файл под именем filename.pdf.txt

            text = ''
            with fitz.open(file_path) as doc:
                for num, page in enumerate(doc.pages()):
                    text += page.get_text()
            text_file_path = os.path.join(MEDIA_ROOT, file.file.name+'.txt')
            with open(text_file_path, "w", encoding='utf-8') as f:
                f.write(text)
        else:
            return
        file.processed = True
        file.save()
    except Exception as e:
        print(e)