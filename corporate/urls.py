from django.urls import path
from django.urls.conf import include
from .views.index import  detail, index
from .views.prices import PlanPricing
from .views.contact import contact
from .views.sent_email import sent_email

urlpatterns = [
    path('', index, name='index'),
    # path('inner', inner, name='inner'),
    path('detail',detail, name='detail'),
    path('contact/', contact, name='contact'),
    path('sent-email/', sent_email, name='sent-email'),
]
