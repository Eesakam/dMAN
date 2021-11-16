from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from .models import Leads
import csv
from django.contrib import messages

#deeeeeeeeeeen
#Lets see if this change happend over here
def index(request):
    lead = Leads.objects.all()
    lead_count = Leads.objects.all().count()
    paginator = Paginator(lead,1000)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,"index.html",{"lead":lead,"lead_count":lead_count,"page_obj":page_obj})


def upload_data(request):
    path = "C:/Users/user/Desktop/upload.csv"
    with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            objection = Leads.objects.get_or_create(
                 client_name=row[0],
                 surname=row[1],
                 ID_num=row[2],
                 alt_num=row[3],
                 BB_num=row[4],
                 )
        messages.success(request,messages.INFO,"added new records")
        return HttpResponseRedirect("/")
        
def delete_lead(request,id):
    messages.success(request, messages.INFO, 'succesfully deleted record.')
    delobj = get_object_or_404(Leads,id=id).delete()
    return HttpResponseRedirect("/")

# WE NEED TO FIX SEARCH FUNCTIONALITY
# def SearchItem(request):
#     if request.method == 'GET':
#         query= request.GET.get('q')

#         submitbutton= request.GET.get('submit')

#         if query is not None:
#             lookups= Q(description__icontains=query)

#             results= NewItem.objects.filter(lookups).distinct()

#             context={'results': results,
#                      'submitbutton': submitbutton}

#             return render(request, 'search.html', context)

#         else:
#             return render(request, 'search.html')

#     else:
#         return render(request, 'search.html')
