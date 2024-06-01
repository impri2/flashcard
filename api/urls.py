from django.urls import path
from api import views

urlpatterns = [
    path('cards', views.all_cards),
    path('card', views.add_card),
    path('card/<int:pk>',views.delete_card),
    path('today',views.today_cards),
    path('should-study',views.should_study),
    path('answer',views.answer_card),
    path('settings/get',views.get_settings),
    path('settings/set',views.set_settings)
]
