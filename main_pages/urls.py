from django.urls import path
from .views.get_started import get_started
from .views.about import about
from .views.services import services
from .views.team import team
from .views.marketing import marketing
from .views.web_development import web_development
from .views.web_design import web_design
from .views.graphic_design import graphic_design
from .views.prices import pricing
from .views.product_management import product_management
from .views.privacy_policy import policy
from .views.terms import terms



urlpatterns = [
    path('get-started/', get_started, name='get-started'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('team/', team, name='team'),
    path('marketing/', marketing, name='marketing'),
    path('privacy-policy/', policy, name='privacy-policy'),
    path('web-design/', web_design, name='web-design'),
    path('web-development/', web_development, name='web-development'),
    path('product-management/', product_management, name='product-management'),
    path('graphic-design/', graphic_design, name='graphic-design'),
    path('terms/', terms, name='terms'),
    path('pricing/', pricing, name='pricing')
    
]



    
