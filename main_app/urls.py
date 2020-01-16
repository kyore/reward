from django.urls import path

from main_app.views.user import UserHomeView, user_create_rating, UserOwnRatingList
from main_app.views.supervisor import SupervisorHomeView, supervisor_rating_view, DivisionUserList, \
    SupervisorUserRatingList
from main_app.views.hr import HrHomeView, hr_rating_view

app_name = 'main'

urlpatterns = [
    path('', UserHomeView.as_view(), name='home'),
    path('sp/', SupervisorHomeView.as_view(), name='home-sp'),
    path('hr/', HrHomeView.as_view(), name='home-hr'),

    path('rating/create/', user_create_rating, name='user-rating'),
    path('rating/list/', UserOwnRatingList.as_view(), name='user-rating-list'),
    path('sp/rating/create/', supervisor_rating_view, name='supervisor-rating'),
    path('sp/rating/users/', SupervisorUserRatingList.as_view(), name='supervisor-rating-users'),
    path('hr/rating/create/', hr_rating_view, name='hr-rating'),

    path('sp/users/', DivisionUserList.as_view(), name='supervisor-users'),
]
