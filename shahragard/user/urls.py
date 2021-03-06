from . import views
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

urlpatterns = [
    path('apiv1/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('apiv1/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('apiv1/token/verify/', TokenVerifyView.as_view(),
         name='token_verify'),
    path('apiv1/user/', views.UserHandler.as_view()),
    path('apiv1/verification/<str:token>/', views.validation),
    path('apiv1/edit/', views.Edit.as_view()),
    path('apiv1/suggestion/', views.SuggestionHandler.as_view()),
    path('apiv1/notif/', views.NotificationHandler.as_view()),
    path('apiv1/history/', views.HistoryHnadler.as_view()),
]
