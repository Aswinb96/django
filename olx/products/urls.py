from django.urls import path
from.import views
urlpatterns=[
    path('',views.about),
    path('aswin/',views.aswin)
]