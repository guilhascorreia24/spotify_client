from django.shortcuts import render
import requests

URL_ME="https://api.spotify.com/v1/me"
def Profile(request):
    headers = {'Authorization': f'Bearer {request.session["access_token"]}'}
    response = requests.get(URL_ME, headers=headers)
    user_data = response.json()
    print(user_data)
    context = {
            'user_name': user_data.get('display_name', ''),
            'user_email': user_data.get('email', ''),
            # Add more data to the context as needed
        }
    return render(request,'profile.html',context)