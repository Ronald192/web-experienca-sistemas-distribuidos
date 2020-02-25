from django.urls import path
from . import views
from .views import ExperienceListView, ExperienceCreate, ExperienceUpdate, ExperienceDelete, ExperienceListUser
from django.contrib.auth.decorators import login_required

experiences_patterns = ([
                            path('', ExperienceListView.as_view(), name='experiences'),
                            path('<int:experience_id>/<slug:experience_slug>/', views.experience_detail,
                                 name='experience'),
                            path('create/', login_required(ExperienceCreate.as_view()), name='create'),
                            path('update/<int:pk>/', login_required(ExperienceUpdate.as_view()), name='update'),
                            path('delete/<int:pk>/', login_required(ExperienceDelete.as_view()), name='delete'),
                            path('listUser', login_required(ExperienceListUser.as_view()), name='listUser'),
                            path('like', views.like_experience, name='like_experience')
                        ], 'experience')
