from django.urls import path
from session.views import session_list, current_construction, turn_constructions

urlpatterns = [
    path('', session_list, name='session_list'),
    path('<int:session_id>/', current_construction, name='current_constructions'),
    path('<int:session_id>/turn/<int:turn>/', turn_constructions, name='turn_constructions'),
]


