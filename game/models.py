from django.db import models
# TODO: media url을 지역 설정으로 변경한다.
from django.conf.global_settings import MEDIA_URL
from functools import partial
from game.tools import combine_file_path


class ImageMixin(models.Model):
    image = models.ImageField(blank=True, null=True, default=None, upload_to=partial(combine_file_path))

    class Meta:
        abstract = True

    def image_url(self):
        if bool(self.image):
            return MEDIA_URL + self.image.url
        else:
            return 'about:blank'


class NumberClass(models.Model):
    value = models.PositiveSmallIntegerField(default=0, help_text="숫자")


class EffectClass(ImageMixin, models.Model):
    title = models.CharField(max_length=32, unique=True, help_text="효과명")
    desc = models.TextField(help_text="설명", null=True, blank=True)


class ConstructionClass(ImageMixin, models.Model):
    number = models.ForeignKey('NumberClass', on_delete=models.CASCADE, help_text='카드 숫자')
    effect = models.ForeignKey('EffectClass', on_delete=models.CASCADE, help_text='카드 효과')
    count = models.PositiveSmallIntegerField(default=0, help_text="게임에 포함된 매수")


