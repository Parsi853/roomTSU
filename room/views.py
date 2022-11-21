from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from core.models import *
from .forms import AddRoomForm
# Create your views here.

@login_required(login_url='/login')
def newAddRoom(request):
    if request.method == 'POST':
        try:
            form = AddRoomForm(request.POST or None)
            if form.is_valid():

                new_room = room.objects.create(
                    added_by = request.user,
                    room_no = form.cleaned_data.get('room_no'),
                    floor = form.cleaned_data.get('floor'),
                    room_type = form.cleaned_data.get('room_type'),
                    appartment_name = form.cleaned_data.get('appartment_name'),
                    appartment_address = form.cleaned_data.get('appartment_address'),
                )

                if 'gender_preference' in request.POST and request.POST['gender_preference'] != '':
                    new_room.gender_preference = request.POST['gender_preference']

                if 'description' in request.POST and request.POST['description'] != '':
                    new_room.description = request.POST['description']

                if 'no_of_beds' in request.POST and request.POST['no_of_beds'] != '':
                    new_room.no_of_beds = request.POST['no_of_beds']

                if 'max_occupants' in request.POST and request.POST['max_occupants'] != '':
                    new_room.max_occupants = request.POST['max_occupants']

                if 'current_occupants' in request.POST and request.POST['current_occupants'] != '':
                    new_room.current_occupants = request.POST['current_occupants']

                if 'room_rent' in request.POST and request.POST['room_rent'] != '':
                    new_room.room_rent = request.POST['room_rent']

                if 'rent_type' in request.POST and request.POST['rent_type'] != '':
                    new_room.rent_type = request.POST['rent_type']

                if 'manager' in request.POST and request.POST['manager'] != '':
                    new_room.manager = request.POST['manager']                    

                if len(request.FILES) != 0:
                    for x in request.FILES.getlist('img') :
                        img_upload = room_image.objects.create(
                            room = new_room,
                            img = x
                        )
                        img_upload.save()
                new_room.save()
                messages.success(request, "Room added")
                return redirect('/add/room?room=True')
            messages.error(request, "Fill all fields")
        except Exception as err:
            print(err)                  
    return render(request, 'room/add-room.html')    