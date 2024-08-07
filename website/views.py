from django.shortcuts import render
from .models import mainContent
# Create your views here.
def index(request):
    contentList = mainContent.objects.order_by('-pub_date')
    context = {'contentList': contentList}
    return render(request, 'website/contentList.html', context)