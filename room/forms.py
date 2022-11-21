from django.forms import ModelForm
from core.models import room

class AddRoomForm(ModelForm):
    class Meta:
        model = room
        fields = [
            'room_no', 
            'floor', 
            'room_type',
            'appartment_name',
            'appartment_address'
        ]