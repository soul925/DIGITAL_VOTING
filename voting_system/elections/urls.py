from django.urls import path
from .views import (
    RegisterView, LoginView,
    ElectionListCreateView, ElectionDetailView,
    CandidateListCreateView, CandidateDetailView,
    VoteCreateView
)
from django.contrib.auth import views as auth_views
from .views import (
    voterpage, managerpage, adminpage,ladminpage, lmanagerpage, lvoterpage  
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),

    path('elections/', ElectionListCreateView.as_view(), name='election-list-create'),
    path('elections/<int:pk>/', ElectionDetailView.as_view(), name='election-detail'),

    path('candidates/', CandidateListCreateView.as_view(), name='candidate-list-create'),
    path('candidates/<int:pk>/', CandidateDetailView.as_view(), name='candidate-detail'),

    path('vote/', VoteCreateView.as_view(), name='vote'),
    path('voter/', voterpage, name='voter'),
    path('manager/', managerpage, name='manager'),
    path('admin/', adminpage, name='admin'),
    path('ladmin/', ladminpage, name='ladmin'),
    path('lmanager/', lmanagerpage, name='lmanager'),
    path('lvoter/', lvoterpage, name='lvoter'),
]
