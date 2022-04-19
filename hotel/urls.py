from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
	path('create', views.create, name='create'),
    path('create_guest', views.create_guest, name='create_guest'),
    path('detail/<int:room_id>', views.detail, name='detail'),
    # path('edit/<int:room_id>', views.edit, name='edit'),
    # path('delete/<int:room_id>', views.delete, name='delete'),
    path('__debug__/', include('debug_toolbar.urls')),
]