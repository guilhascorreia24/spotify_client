from django.shortcuts import render
# Create your views here.
def home(request):
    context={'logged':('access_token' in request.session)}
    print(context['logged'])
    return render(request,'home.html',context)