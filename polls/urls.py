from django.urls import path

from . import views


#app_name = "polls"


urlpatterns = [
    path("", views.cafe_category, name="category"),
    path('<int:question_id>/', views.category_detail, name='category_detail'),
]