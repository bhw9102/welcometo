from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from session.models import Session, Construction
from session import position


def session_list(request):
    #GET
    # test = ConstructionClass.objects.filter(pk=3).first()
    # print(test)
    return render(request, 'session/session_list.html', dict(session_list=Session.objects.all()))


def current_constructions(request, session_id):
    # GET
    session = Session.objects.filter(pk=session_id).first()
    turn = session.current
    open_cards = open_constructions(session=session, turn=turn)
    return render(request, 'session/construction.html', open_cards)


def turn_constructions(request, session_id, turn):
    # GET
    open_cards = open_constructions(session=session_id, turn=turn)
    return render(request, 'session/construction.html', open_cards)


def open_constructions(session, turn):
    # print_deck_list(session=session)
    # 턴에 해당하는 카드를 찾는다.
    left_num = Construction.objects.filter(session=session, order=turn, position=position.LEFT).first()
    center_num = Construction.objects.filter(session=session, order=turn, position=position.CENTER).first()
    right_num = Construction.objects.filter(session=session, order=turn, position=position.RIGHT).first()

    # 이펙트 효과를 가진 카드는 이전 턴 카드다.
    effect_order = turn - 1
    left_effect = Construction.objects.filter(session=session, order=effect_order, position=position.LEFT).first()
    center_effect = Construction.objects.filter(session=session, order=effect_order, position=position.CENTER).first()
    right_effect = Construction.objects.filter(session=session, order=effect_order, position=position.RIGHT).first()
    open_cards = dict(turn=turn, left_num=left_num, center_num=center_num, right_num=right_num,
                      left_effect=left_effect, center_effect=center_effect, right_effect=right_effect)
    # print(open_cards)
    return open_cards


def manager(request, session_id):
    # GET
    session = Session.objects.filter(pk=session_id).first()
    return render(request, 'session/manager.html', dict(session=session))


def change_turn(request, session_id, action):
    print(request)
    session = Session.objects.filter(pk=session_id).first()
    if action == 'increase':
        session.current += 1
    elif action == 'decrease':
        session.current -= 1
    session.save()
    return HttpResponseRedirect(reverse('manager', kwargs=dict(session_id=session_id)))


