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

    def prepare_session(self):
        # TODO: 이미 생성되어있을 경우 작동하지 않도록 한다.
        # 카드를 생성한다.
        prepare_session_card(self)
        # 전체를 섞는다.
        # 세개 덱으로 나눈다.
        # 덱 별로 섞는다.


def prepare_session_card(session: Session):
    card_list = ConstructionClass.objects.all()
    prepare_position = 0
    order = 0
    prepare_deck = list()
    for card in card_list:
        for i in range(0, card.count):
            card = Construction.create(session=session, card=card, position=prepare_position, order=order)
            prepare_deck.append(card)
            order += 1


DECK_POSITION = (
    ('PREPARE', 0),
    ('LEFT', 1),
    ('CENTER', 2),
    ('RIGHT', 3)
)


class Construction(models.Model):
    session = models.ForeignKey('Session', on_delete=models.CASCADE)
    card = models.ForeignKey('game.ConstructionClass', on_delete=models.CASCADE)
    position = models.PositiveSmallIntegerField(default=0, choices=DECK_POSITION, help_text='카드의 위치')
    order = models.PositiveSmallIntegerField(default=0, help_text='카드의 순서')

    @classmethod
    def create(cls, session, card, position, order):
        obj = cls(session=session, card=card, position=position, order=order)
        obj.save()
        return obj

    def __str__(self):
        return "{position}-order:{order}-{card}".format(position=DECK_POSITION[self.position][0], card=self.card, order=self.order)

