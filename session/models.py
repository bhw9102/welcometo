import datetime
from django.db import models
import random
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
        deck = prepare_creating_card(self)
        # 전체를 섞는다.
        prepare_shuffling_card(deck)
        # 세개 덱으로 나눈다.
        prepare_dividing_deck(deck=deck)
        # 덱이 잘 생성됐는지 확인한다.
        print_deck_list(session=self)


def prepare_creating_card(session: Session):
    card_list = ConstructionClass.objects.all()
    prepare_position = 0
    order = 0
    prepare_deck = list()
    for card_class in card_list:
        for i in range(0, card_class.count):
            card = Construction.create(session=session, card=card_class, position=prepare_position, order=order)
            prepare_deck.append(card)
            order += 1
    return prepare_deck


def prepare_shuffling_card(deck):
    order_list = shuffle_ordering(count=len(deck))
    for i, obj in enumerate(deck):
        obj.order = order_list[i]
        obj.save()


def shuffle_ordering(count: int):
    order_list = list(range(0, count))
    random.shuffle(order_list)
    return order_list


def prepare_dividing_deck(deck: list):
    for card in deck:
        card.position = (card.order % 3) + 1
        card.order = card.order // 3
        card.save()


def print_deck_list(session: Session):
    deck = Construction.objects.filter(session=session, position=pos_left).order_by('order').all()
    print("왼쪽 카드 뭉치")
    for card in deck:
        print(card.__str__())
    deck = Construction.objects.filter(session=session, position=pos_center).order_by('order').all()
    print("중앙 카드 뭉치")
    for card in deck:
        print(card.__str__())
    deck = Construction.objects.filter(session=session, position=pos_right).order_by('order').all()
    for card in deck:
        print(card.__str__())


pos_prepare = 0
pos_left = 1
pos_center = 2
pos_right = 3

DECK_POSITION = (
    ('PREPARE', pos_prepare),
    ('LEFT', pos_left),
    ('CENTER', pos_center),
    ('RIGHT', pos_right)
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

