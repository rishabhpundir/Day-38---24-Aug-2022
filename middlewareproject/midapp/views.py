from django.shortcuts import render, HttpResponse
from django.template.response import TemplateResponse

# Create your views here.
def home(request):
    print('**********************************')
    print('***This is the Home view executing***')
    print('**********************************')
    return HttpResponse('***********View executed***********')

def exception_view(request):
    print('**********************************')
    print('***This is the Exception view executing***')
    print('**********************************')
    a=10/0
    return HttpResponse('***********Exception View executed***********')

def user_info(request):
    print('**********************************')
    print('***This is the User Info View executing***')
    print('**********************************')
    context = {'name':'Rishabh Pundir'}
    return TemplateResponse(request, 'user.html', context)