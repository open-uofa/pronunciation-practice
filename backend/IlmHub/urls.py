"""IlmHub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ilmhub_app.views import ContentView
# api doc packages
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from django.conf import settings
from django.conf.urls.static import static

# set up for documentation
schema_view = get_schema_view(
   openapi.Info(
      title="IlmHub API",
      default_version='v1',
      description="API for IlmHub platform",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email=""),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), 
        name='schema-swagger-ui'),
    
    path('', include('ilmhub_app.urls')),

    path('lessontabs/student/<uuid:pk>/', ContentView.as_view({
    "get": "get_student_lesson_tabs",
    }), name="student_lesson_tabs"),

    path('lessontabs/parentchildren/<uuid:pk>/', ContentView.as_view({
    "get": "get_parent_children",
    }), name="parent_children"),


    path('lessontabs/', ContentView.as_view({
    "get": "get_all_lesson_tabs",
    "post": "create_lesson_tab"
    }), name="lesson_tabs"),

    path('lessontabs/<uuid:id>/', ContentView.as_view({
    "post": "create_chapter",
    }), name="one_lesson_tab"),

    path('lessons/<uuid:pk>/', ContentView.as_view({
    "get": "get_all_lesson_tabs",
    }), name='get_all_lesson_tabs'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
