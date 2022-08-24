from django.urls import path
from core import views 

urlpatterns = [
    path('', views.addandshow, name='addandshow'),
    path('delete_data/<int:pk>', views.delete_data, name='delete_data'),
    path('<int:pk>', views.update_data, name='update_data'),

]
