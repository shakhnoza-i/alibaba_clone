from django.urls import path, include

from review.views import ReviewCreate, ReviewList, ReviewDetail


urlpatterns = [
    path('<int:pk>/review/create/',  ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/',  ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/',  ReviewDetail.as_view(), name='review-details'),
]
