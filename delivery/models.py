from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
from django_recaptcha.fields import ReCaptchaField


class qr(models.Model):
    name = models.CharField(max_length=255)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.name)
        canvas = Image.new('RGB', (290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.name}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)


class Receiver(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    home_number = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Contract(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.TextField()
    size = models.IntegerField(default=0)

    def __str__(self):
        return self.name
