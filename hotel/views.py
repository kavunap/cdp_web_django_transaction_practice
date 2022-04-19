from django.shortcuts import render
from django.shortcuts import redirect
from .models import Room,Guest
from .forms import RoomForm
from .forms import GuestForm
# Transaction
from django.db import IntegrityError, transaction
# validation
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from django.db import connection


def index(request):
    rooms = Room.objects.all()
    params = {
        'rooms': rooms,
    }
    return render(request, 'hotel/index.html', params)


def create(request):
    if (request.method == 'POST'):
        obj = Room()   # 1
        room = RoomForm(request.POST, instance=obj)   # 2
        room.save()   # 3
        return redirect('index')
    else:
        params = {
            'form': RoomForm(),
        }
        return render(request, 'hotel/create.html', params)
# @transaction.atomic

def detail(request, room_id): # --- 1
    room = Room.objects.get(id=room_id) # --- 2
    params = {
        'room': room,
    }
    return render(request, 'hotel/details.html', params)


# @transaction.atomic
def create_guest(request):
    if (request.method == 'POST'): 
        with transaction.atomic():
            name = request.POST['name']
            if name=="":
                name=None
            email = request.POST['email']
            if email=="":
                email=None 
            room_id=request.POST['room_id']
            guest = Guest(name=name, email=email,room_id=room_id)
            room = Room.objects.get(id=guest.room_id)
            room.available=False
            room.save()
            if name is None or email is None:
                t=transaction.set_rollback(True)
            else:
                guest.save()
            print(connection.queries)
        return redirect('index')
    else:
        params = {
            'form': GuestForm(),
        }
        return render(request, 'guest/create.html', params)

# def create_guest(request):
#     if (request.method == 'POST'):
#         with transaction.atomic():
#             name = request.POST['name']
#             if name=="":
#                 name=None
#             email = request.POST['email']
#             if email=="":
#                 email=None 
#             room_id=request.POST['room_id']
#             guest = Guest(name=name, email=email,room_id=room_id)
#             room = Room.objects.get(id=guest.room_id)
#             room.available=False
#             room.save()
#             guest.save()
#         return redirect('index')
#     else:
#         params = {
#             'form': GuestForm(),
#         }
#         return render(request, 'guest/create.html', params)