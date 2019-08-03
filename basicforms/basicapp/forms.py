from django import forms
from basicapp.models import User
from basicapp.models import Bar
from basicapp.models import ML_data
from basicapp.models import Notifi
#from basicapp.models import check


class NewUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('start_stop','end_stop','amount',)

class make_data(forms.ModelForm):
    class Meta():
        model = Bar
        fields = ('bus_no','total_no_of_stops','enter_stop_price_time_with_commas','enter_time',)

class Research_data(forms.ModelForm):
    class Meta():
        model = ML_data
        fields = ( 'accidents','vechile_breakdown' , 'weather' , 'Traffic','route','density','delay',)

class notificat(forms.ModelForm):
    class Meta():
        model = Notifi
        fields = '__all__'

'''
class check_data(forms.ModelForm):
    class Meta():
        model = Bar
        fields = '__all__'
'''
