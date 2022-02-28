from django.urls import path
from .views.skill_views import SkillsView, SkillDetailView
from .views.practice_views import PracticesView, PracticeDetailView

urlpatterns = [
    # Restful routing
    path('skills/', SkillsView.as_view(), name='skills'),
    path('skills/<int:pk>/', SkillDetailView.as_view(), name='skill_detail'),

    path('practices/', PracticesView.as_view(), name='practices'),
    path('practices/<int:pk>/', PracticeDetailView.as_view(), name='practice_detail'),
]
