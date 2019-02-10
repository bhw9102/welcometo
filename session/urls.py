from django.urls import path
from session.views import session_list, current_constructions, turn_constructions, manager, change_turn

urlpatterns = [
    path('', session_list, name='session_list'),
    path('<int:session_id>/', current_constructions, name='current_constructions'),
    path('<int:session_id>/turn/<int:turn>/', turn_constructions, name='turn_constructions'),
    path('<int:session_id>/manager/', manager, name='manager'),
    path('<int:session_id>/manager/<str:action>', change_turn, name='change_turn'),
]


