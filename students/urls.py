from django.urls import path

from rest_framework import routers

# from .views import index
from students.views import StudentsViewSet

router = routers.DefaultRouter()
router.register('students', StudentsViewSet)

urlpatterns = router.urls

"""
urlpatterns = [
    path('students/', index)
]
"""

