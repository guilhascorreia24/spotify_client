from django.shortcuts import render
import requests
import utilis
import urlsAPI

def Profile(request):
    headers = {'Authorization': f'Bearer {request.session["access_token"]}'}
    response = requests.get(urlsAPI.URL_ME, headers=headers)
    user_data = response.json()
    print(user_data)
    if 'images' in user_data and user_data['images']:
        user_profile_image_url = user_data['images'][0]['url']
    else:
        user_profile_image_url = ''  # Set a default image URL or handle missing image

    context = {
            'user_name': user_data.get('display_name', ''),
            'user_email': user_data.get('email', ''),
            'user_profile_image_url':user_profile_image_url
            # Add more data to the context as needed
        }
    return render(request,'profile.html',context)