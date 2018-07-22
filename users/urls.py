from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'index/$',views.BookView.as_view()),
    url(r'test/$',views.TemplateView.as_view())
]