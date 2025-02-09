from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from tinymce import models as tinymce_models
from django.utils.safestring import mark_safe


ACHIEVEMENT_CHOICES = [
    ('license', _('Litsensiya')),
    ('achievement', _('Yutuq')),
]

class SocialMedia(models.Model):

    icon = models.CharField(
        max_length=200,
        verbose_name=_("Nomi"),
        help_text=_("fa-brands fa-telegram")
    )
    link = models.CharField(max_length=500, verbose_name=_("Havola"))

    def __str__(self):
        return self.link

    class Meta:
        verbose_name = _("Ijtimoiy tarmoqlar")
        verbose_name_plural = _("Ijtimoiy tarmoqlar")
        abstract = True



class News(models.Model):
    image = models.ImageField(upload_to='assets/images/news_images/', verbose_name=_("Rasm"))
    
    title = models.CharField(max_length=200, verbose_name=_("Sarlavha"))
    slug = models.SlugField(default="", verbose_name=_("Qisqa link"), unique=True)
    content = tinymce_models.HTMLField(verbose_name=_("Matn"))
    views = models.IntegerField(default=0, verbose_name=_("Ko'rishlar soni"), editable=False)
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan vaqti"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Yangilangan vaqti"))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news-detail", kwargs={"slug": self.slug})
    
    class Meta:
        verbose_name = _("Yangiliklar")
        verbose_name_plural = _("Yangiliklar")


class SiteSettings(models.Model):
    phone = models.CharField(max_length=200, verbose_name=_("Telefon raqam"))
    email = models.CharField(max_length=200, verbose_name=_("Elektron pochta"))
    address = models.CharField(max_length=200, verbose_name=_("Manzil"))
    about_us = tinymce_models.HTMLField(verbose_name=_("Biz haqimizda"))

    lat_long = models.CharField(max_length=200, verbose_name=_("Xaritadagi koordinatalar"), blank=True, null=True, help_text=_("Masalan: 41.311081, 69.289632"))


    def __str__(self):
        return str(_("Sayt sozlamalari"))


    class Meta:
        verbose_name = _("Sayt sozlamalari")
        verbose_name_plural = _("Sayt sozlamalari")


class ContactPerson(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("Nomi"))
    full_name = models.CharField(max_length=200, verbose_name=_("F.I.SH"), blank=True, null=True)
    phone = models.CharField(max_length=200, verbose_name=_("Telefon raqam"), blank=True, null=True)
    email = models.CharField(max_length=200, verbose_name=_("Elektron pochta"), blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Kontakt persona")
        verbose_name_plural = _("Kontakt personalari")
        

class Team(models.Model):
    image = models.ImageField(upload_to='uploads/team/%Y/%m/%d/', verbose_name=_("Rasm"))
    full_name = models.CharField(max_length=200, verbose_name=_("F.I.SH"))
    position = models.CharField(max_length=200, verbose_name=_("Lavozimi"))
    description = models.TextField(verbose_name=_("Kichik izoh"))
    contact_url = models.CharField(max_length=200, verbose_name=_("Bog'lanish URL"), blank=True, null=True, default="#contact")


    def __str__(self):
        return self.full_name
    
    def image_tag(self):
        return mark_safe('<img src="%s" width ="50" height="50"/>'%(self.image.url))
    
    image_tag.short_description = _('Rasm')

    class Meta:
        verbose_name = _("Jamoa")
        verbose_name_plural = _("Jamoa")
    

class LicenseAchievement(models.Model):
    image = models.ImageField(upload_to='uploads/license_achievement/%Y/%m/%d/', verbose_name=_("Rasm"))
    title = models.CharField(max_length=200, verbose_name=_("Sarlavha"))
    achievement_type = models.CharField(max_length=200, verbose_name=_("Turi"), choices=ACHIEVEMENT_CHOICES)


    def image_tag(self):
        return mark_safe('<img src="%s" width ="50" height="50"/>'%(self.image.url))
    
    image_tag.short_description = _('Rasm')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _("Litsensiya va yutuqlar")
        verbose_name_plural = _("Litsensiya va yutuqlar")


class Service(models.Model):
    image = models.ImageField(upload_to='uploads/service/%Y/%m/%d/', verbose_name=_("Fon rasmi"))
    icon = models.ImageField(upload_to='uploads/service/%Y/%m/%d/', verbose_name=_("Ikonka rasmi"))
    title = models.CharField(max_length=200, verbose_name=_("Sarlavha"))
    slug = models.SlugField(default="", verbose_name=_("Qisqa link"), unique=True)
    content = tinymce_models.HTMLField(verbose_name=_("Matn"))

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("service-detail", kwargs={"slug": self.slug})
    
    class Meta:
        verbose_name = _("Xizmat")
        verbose_name_plural = _("Xizmatlar")


class Event(models.Model):
    image = models.ImageField(upload_to='uploads/event/%Y/%m/%d/', verbose_name=_("Rasm"))
    title = models.CharField(max_length=200, verbose_name=_("Sarlavha"))
    slug = models.SlugField(default="", verbose_name=_("Qisqa link"), unique=True)
    content = tinymce_models.HTMLField(verbose_name=_("Matn"))
    active = models.BooleanField(default=True, verbose_name=_("Faol"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan vaqti"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Yangilangan vaqti"))
    
    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse("event-detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = _("Tadbir")
        verbose_name_plural = _("Tadbirlar")


class EventImage(models.Model):
    image = models.ImageField(upload_to='uploads/event_images/%Y/%m/%d/', verbose_name=_("Rasm"))
    def __str__(self):
        return self.image.url

    def image_tag(self):
        return mark_safe('<img src="%s" width ="50" height="50"/>'%(self.image.url))
    
    image_tag.short_description = _('Rasm')

    class Meta:
        verbose_name = _("Tadbir lavhalari")
        verbose_name_plural = _("Tadbir lavhalari")


class Partner(models.Model):
    image = models.ImageField(upload_to='uploads/partner/%Y/%m/%d/', verbose_name=_("Rasm"))
    title = models.CharField(max_length=200, verbose_name=_("Nomi"))

    def __str__(self):
        return self.title
    
    def image_tag(self):
        return mark_safe('<img src="%s" width ="50" height="50"/>'%(self.image.url))
    
    image_tag.short_description = _('Rasm')

    class Meta:
        verbose_name = _("Hamkor")
        verbose_name_plural = _("Hamkorlar")


class Gallery(models.Model):
    image = models.ImageField(upload_to='uploads/gallery/%Y/%m/%d/', verbose_name=_("Rasm"))

    def __str__(self):
        return self.image.url
    
    def image_tag(self):
        return mark_safe('<img src="%s" width ="50" height="50"/>'%(self.image.url))
    
    image_tag.short_description = _('Rasm')

    class Meta:
        verbose_name = _("Galereya")
        verbose_name_plural = _("Galereya")


class TeamSocialMedia(SocialMedia):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="social_media")


class ContactPersonSocialMedia(SocialMedia):
    contact_person = models.ForeignKey(ContactPerson, on_delete=models.CASCADE, related_name="social_media")
    
    
class SiteSocialMedia(SocialMedia):
    site_settings = models.ForeignKey(SiteSettings, on_delete=models.CASCADE, related_name="social_media")