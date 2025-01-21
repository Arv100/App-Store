from django.urls import path, include
import rest_framework.urls
from .views import user_login, user_logout, register, dashboard, admin_view, index, admin_add_app, admin_home, update_app, admin_delete_app, admin_delete_vew, update_points
from .api_view import AppListAPI, CreateUserView, AppDetailAPI
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
import rest_framework
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('',index,name='Index'),
    path('login/',user_login,name='Login'),
    path('register/',register,name='Register'),
    path('logout/',user_logout,name='Logout'),
    path('dashboard/',dashboard,name='Dashboard'),
    path('dashboard/<str:app_name>',update_app,name='Update'),
    path('dashboard/update-points/<str:app_name>',update_points,name='Update-points'),

    path('app-admin/',admin_home,name='Admin'),
    path('app-admin/add-app/', admin_add_app, name='add_app'),
    path('app-admin/admin-view',admin_view,name='Admin view'),
    path('app-admin/<str:app_name>',admin_delete_vew,name='A-Update'),
    path('app-admin/delete/<str:app_name>',admin_delete_app,name='Delete'),
]

urlpatterns += [
    path('api/user/register/', CreateUserView.as_view(), name='register_user'),
    path('api/token/',TokenObtainPairView.as_view(), name='get_token'),
    path('api/token/refresh',TokenRefreshView.as_view(), name='refresh_token'),
    path('api-auth',include(rest_framework.urls)),
    path('api/apps/', AppListAPI.as_view(), name='app-list-api'),
    path('api/apps/<int:pk>/', AppDetailAPI.as_view(), name='retrieve_update_delete_app')
]

urlpatterns += [
    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]