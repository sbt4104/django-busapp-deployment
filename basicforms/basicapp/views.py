from django.shortcuts import render
from django.http import HttpResponse
from basicapp.models import Bar
from basicapp.models import User
from basicapp.models import Notifi
from basicapp.forms import NewUserForm
from basicapp.forms import notificat
from basicapp.forms import make_data
from basicapp.models import ML_data
from basicapp.forms import Research_data
#from basicapp.forms import check_data
from django.template import RequestContext
from django.shortcuts import render_to_response


import os
import pickle
import numpy as np
import pandas as pd
from sklearn import datasets
from django.conf import settings
from rest_framework import views
from rest_framework import status
from rest_framework.response import Response
from sklearn.ensemble import RandomForestClassifier



# Create your views here.

def note(request):
    return render(request,'basicapp/noti.html')

def index(request):
    return render(request,'basicapp/index.html')

def check1(request):
    return render(request,'basicapp/search.html')

def search(request):
    query1 = request.GET.get("p")
    query2 = request.GET.get("q")
    print(query1)
    print(query1)
    try:
        query1 = str(query1)
        query2 = str(query2)
    except ValueError:
        query1 = None
        query2 = None
        results = None
    if query1 and query2:
        results = Bar.objects.all()
    context1= RequestContext(request)
    print(results)
    my_dict = {}
    my_dict3 = {}
    piv1=0
    piv2=0
    for val in results:
        piv1=0
        piv2=0
        my_dict2 = {}
        string=val.enter_stop_price_time_with_commas
        string2=val.enter_time
        print(string2)
        mylist = string.split(',')
        print(mylist)
        mylist2 = string2.split(',')
        #print(mylist[0])


        for k in mylist:
            if k==query1:
                piv1=1
            if k==query2:
                piv2=1
        if piv1==1 and piv2==1:
            for i in range(val.total_no_of_stops):
                my_dict2[mylist[i]] = mylist2[i]
            #my_dict[val.bus_no]=mylist
            #my_dict2[val.bus_no]=mylist2
            my_dict[val.bus_no] =my_dict2
            #my_dict3[my_dict].append(my_dict2)
    print(my_dict)
    #my_dict[val.bus_no] =my_dict2
    return render_to_response('basicapp/results.html',{"results":my_dict,"results2":my_dict2})

def users(request):

    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            model_instance = form.save(commit=False)
            #model_instance.timec = Time.now()
            results = User.objects.all()
            m_time = model_instance.timec
            #print(m_time)
            k = results.count()
            #print(k)
            if k == 0:
                model_instance.total_peo = 1
                model_instance.seats = 20
            else:
                pivot = results[k-1]
                if (pivot.seats-pivot.total_peo <=0):
                    model_instance.seats = pivot.seats
                else:
                    model_instance.seats = pivot.seats-1
                model_instance.total_peo = pivot.total_peo+1
            model_instance.save()
            return render(request,'basicapp/forms_index.html',{'form':form})
        else:
            print('ERROR FORM INVALID')

    return render(request,'basicapp/forms_index.html',{'form':form})

def update_n(request):
    query1 = request.GET.get("p")
    print(query1)
    form = notificat()
    form1 = NewUserForm()
    model_instance = form.save(commit=False)
    m_instsave = form1.save(commit=False)
    #model_instance.timec = Time.now()
    results1 = User.objects.all()
    results2 = Bar.objects.all()
    #m_time = model_instance.timec
    #print(m_time)
    total = results1.count()
    print(total)
    #print(total)
    for k in results1:
        #print(k.end_stop)
        if (k.end_stop==query1):
            print(k.end_stop)
            print(results1[total-1].seats)
            if k.seats<21:
                results1[total-1].seats=results1[total-1].seats+1
            results1[total-1].total_peo=results1[total-1].total_peo-1
            print(results1[total-1].seats)
    model_instance.save()
    results1[total-1].save()
    return index(request)

    #return render(request,'basicapp/forms_index.html',{'form':form})


def official_data(request):

    form = make_data()

    if request.method == "POST":
        form = make_data(request.POST)

        if form.is_valid():
            model_instance = form.save(commit=True)
            return index(request)
        else:
            print("ERROR")

    return render(request,'basicapp/forms_index.html',{'form':form})

def research(request):

    form = Research_data()

    if request.method == "POST":
        form = Research_data(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request,'basicapp/forms_index.html',{'form':form})
            #return index(request)
        else:
            print("ERROR")

    return render(request,'basicapp/forms_index.html',{'form':form})

'''def check_request(request):
    form = check()

    if request.method == "POST":
        form = make_data(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR")

    return render(request,'basicapp/forms_index.html',{'form':form})
'''

def new_user_table(request):
    list = User.objects.order_by('timec')
    my_dict = {'access_records':list}
    return render(request,'basicapp/newuse.html',context=my_dict)

def research_table(request):
    list = ML_data.objects.order_by('delay')
    my_dict = {'access_records':list}
    return render(request,'basicapp/index_research.html',context=my_dict)




class Train(views.APIView):
    def post(self, request):
        iris = datasets.load_iris()
        mapping = dict(zip(np.unique(iris.target), iris.target_names))

        X = pd.DataFrame(iris.data, columns=iris.feature_names)
        y = pd.DataFrame(iris.target).replace(mapping)
        model_name = request.data.pop('model_name')

        try:
            clf = RandomForestClassifier(**request.data)
            clf.fit(X, y)
        except Exception as err:
            return Response(str(err), status=status.HTTP_400_BAD_REQUEST)

        path = os.path.join(settings.MODEL_ROOT, model_name)
        with open(path, 'wb') as file:
            pickle.dump(clf, file)
        return Response(status=status.HTTP_200_OK)


class Predict(views.APIView):
    def post(self, request):
        predictions = []
        for entry in request.data:
            print(entry)
            model_name = entry.pop('model_name')
            path = os.path.join(settings.MODEL_ROOT, model_name)
            with open(path, 'rb') as file:
                model = pickle.load(file)
            try:
                print(entry)
                result = model.predict(pd.DataFrame([entry]))
                predictions.append(result[0])

            except Exception as err:
                return Response(str(err), status=status.HTTP_400_BAD_REQUEST)

        return Response(predictions, status=status.HTTP_200_OK)
