from django.urls import path
from .views import ArticlesListApiview, ArticlesDetailsApiveiw

urlpatterns = [
    path('list/', ArticlesListApiview.as_view()),
    path('detail/<slug:slug>', ArticlesDetailsApiveiw.as_view())
]
