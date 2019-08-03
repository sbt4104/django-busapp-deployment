from basicapp.views import Train, Predict
from django.conf.urls import url

app_name = 'basicapp'

urlpatterns = [
    url('train/', Train.as_view(), name="train"),
    url('predict/', Predict.as_view(), name="predict"),
]
