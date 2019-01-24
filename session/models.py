import datetime
from django.db import models
from game.models import ConstructionClass


class CreatedUpdatedMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False, help_text='생성 시간')
    updated_at = models.DateTimeField(auto_now=True, editable=False, help_text='갱신 시간')

    class Meta:
        abstract = True

    def save(self, **kwargs):
        if not self.id:
            self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        super(CreatedUpdatedMixin, self).save()


class Session(CreatedUpdatedMixin, models.Model):
    title = models.CharField(max_length=32, help_text='세션 이름')
    current = models.PositiveSmallIntegerField(default=0, help_text='현재 턴')


DECK_POSITION = (
    ('LEFT', 0),
    ('CENTER', 1),
    ('RIGHT', 2)
)


class Construction(models.Model):
    session = models.ForeignKey('Session', on_delete=models.CASCADE)
    card = models.ForeignKey('game.ConstructionClass', on_delete=models.CASCADE)
    position = models.PositiveSmallIntegerField(default=0, choices=DECK_POSITION, help_text='카드의 위치')
    order = models.PositiveSmallIntegerField(default=0, help_text='카드의 순서')



