from django.urls import path
from . import views

app_name = 'basic'

urlpatterns=[
    path('',views.index.as_view(),name='index'),
    path('list/',views.SchoolListView.as_view(),name='list'),
    path('list/<int:pk>/',views.SchoolDetailView.as_view(),name='detail'),
    path('create/',views.SchoolCreateView.as_view(),name='create'),
    path('update/<int:pk>/',views.SchoolUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',views.SchoolDeleteView.as_view(),name='delete')
    
    # path('register/',views.register,name='register'),
    # path('user_login/',views.user_login,name='user_login'),
]
