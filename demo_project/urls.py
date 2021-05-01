from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from rest_framework.authtoken.views import obtain_auth_token

from apps.core.schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'graphql/',
        csrf_exempt(
            GraphQLView.as_view(graphiql=True, schema=schema)
        )
    ),
    path('api/login/', obtain_auth_token),
]
