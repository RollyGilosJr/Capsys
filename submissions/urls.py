from django.urls import path, include
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('submissions/', views.submissions, name = "submissions"),
    path('submit/<int:id>/', views.submit, name="Submit"),
]
