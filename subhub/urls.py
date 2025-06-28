from django.urls import path
from subhub import views
from .views import add_quizzes

urlpatterns=[
    path("",views.home,name="home"),
    path("signup/",views.signup,name="signup"),
    path("login/",views.login,name="login"),
    path("about/", views.about,name="about"),
     path("kandas/", views.kandas,name="kandas"),
      path("explore/", views.explore,name="explore"),
      path('logout/', views.logout, name='logout'),
    path('quizzes/', views.quizzes, name='quizzes'),
   path('quizzes/', views.quizzes_list, name='quizzess'),
    path('quizzes/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('add-quizzes/', add_quizzes),
    
   
    
]


    
 
    




