from django.http import JsonResponse
from django.shortcuts import render
import requests
import urlsAPI

# Create your views here.
def getHistory(request,after=None,before=None):
    headers = {'Authorization': f'Bearer {request.session["access_token"]}'}
    response = requests.get(urlsAPI.URL_HISTORY(after,before), headers=headers)
    data = response.json()
    data={"history":data}
    return JsonResponse(data)
