from django.urls import path
from subhub import views


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
 
  
 
    
   
    
]


    
 
    




