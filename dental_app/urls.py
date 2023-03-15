from django.urls import path
from dental_app import views

urlpatterns = [
    path('index', views.index, name="home"),
    path('add_patient/', views.add_patient),
    path('display_big_table/', views.display_big_table),
    path('reports2/', views.reports2),
    path('remove/', views.remove),
    path('patient_view/', views.view_patient,name='patient_view'),
    path('reshon/', views.reshon),
    path('tel_aviv/', views.tel_aviv),
    path('results/', views.results),
    path('no_results/', views.results),
    path('analysis/', views.analysis),
    path('contact/', views.contact),
    path('', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register_user/', views.register_user, name="register_user"),

]
