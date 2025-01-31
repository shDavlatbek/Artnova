from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field

class News(models.Model):
    image = models.ImageField(upload_to='assets/images/news_images/', help_text=_("1:1 Nisbatdagi rasm yuklang"), verbose_name=_("Rasm"))
    
    title = models.CharField(max_length=200, verbose_name=_("Sarlavha"))
    slug = models.SlugField(default="", verbose_name=_("Qisqa link"))
    content = models.TextField(verbose_name=_("Matn"))
    views = models.IntegerField(default=0, verbose_name=_("Ko'rishlar soni"))
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan vaqti"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Yangilangan vaqti"))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news-detail", kwargs={"slug": self.slug})
    
    class Meta:
        verbose_name = _("Yangiliklar")
        verbose_name_plural = _("Yangiliklar")

class Medicine(models.Model):
    image = models.ImageField(upload_to='assets/images/medicine_images/', verbose_name=_("Rasm"))
    name_uz = models.CharField(max_length=200, verbose_name=_("Nomi")+" [uz]")
    name_ru = models.CharField(max_length=200, verbose_name=_("Nomi")+" [ru]")
    name_en = models.CharField(max_length=200, verbose_name=_("Nomi")+" [en]")
    description_sm_uz = CKEditor5Field(config_name='extends', verbose_name=_("Tavsif kichik")+" [uz]")
    description_sm_ru = CKEditor5Field(config_name='extends', verbose_name=_("Tavsif kichik")+" [ru]")
    description_sm_en = CKEditor5Field(config_name='extends', verbose_name=_("Tavsif kichik")+" [en]")
    description_uz = CKEditor5Field(config_name='extends', verbose_name=_("Tavsif")+" [uz]")
    description_ru = CKEditor5Field(config_name='extends', verbose_name=_("Tavsif")+" [ru]")
    description_en = CKEditor5Field(config_name='extends', verbose_name=_("Tavsif")+" [en]")

    def __str__(self):
        return self.name_uz
    
    def get_absolute_url(self):
        return reverse("medicine-detail", kwargs={"pk": self.pk})
    
    class Meta:
        verbose_name = _("Dorilar")
        verbose_name_plural = _("Dorilar")