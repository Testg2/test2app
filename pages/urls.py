from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    # path('<int:id>/', views.about, name='about'),
    path('search/', views.search, name='search'),

    path('', views.IndexListView.as_view(), name='index'),
    path('<int:pk>/', views.AboutDetailView.as_view(), name='about'),

    # update frontend url
    path('add/', views.AddNewView.as_view(), name='add'),

    # always user id to update this value
    path('update/<int:pk>/', views.UpdateDetailView.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeleteDetailView.as_view(), name='delete'),

    # signup pages
    path('signup', views.SignupView.as_view(), name='signup')
]