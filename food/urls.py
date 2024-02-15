
from django.contrib import admin
from django.urls import path
from .views import OrganizationViewSet, ItemViewSet, PricingViewSet, home, CalculateDeliveryCost
from rest_framework.routers import DefaultRouter
from django.urls import include, re_path

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Food Delivery Price Calculator API')

# urlpatterns = [
#     re_path(r'^$', schema_view)
# ]

router = DefaultRouter()
router.register(r'organizations', OrganizationViewSet, basename= 'organization')
router.register(r'items', ItemViewSet, basename='item')
router.register(r'pricing', PricingViewSet, basename='pricing')
router.register(r'calculate_delivery_cost', CalculateDeliveryCost, basename='calculate_delivery_cost')


urlpatterns = [
    re_path(r'^$', schema_view),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/calculate_delivery_cost/', CalculateDeliveryCost.as_view(), name='calculate_delivery_cost'),

]
