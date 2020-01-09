import os
import json
import requests
import base64


#  curl --location --request POST "https://api.imgur.com/3/image" \
#   --header "Authorization: Client-ID {{clientId}}" \
#   --form "image=R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"
def upload(img_b64):
    app_id = 'f7bce5ff873c8f8'

    request_body = {
        'image': img_b64,
        'name': 'numbers.jpg',
        'type': 'base64',
        'title': 'Biryani',
        'description': 'Awesome Briyani 5 Stars -- Fun!!!'
    }

    url = "https://api.imgur.com/3/upload"
    headers = {
        'Authorization': 'Client-ID ' + app_id
    }

    response = requests.post(url, data=request_body, headers=headers)
    resp = response.json()

    assert response.status_code == 200
    image_url = resp['data']['link']
    return image_url

def file_path_to_img64(image_path):
    f = open(image_path, 'rb')
    img = f.read()
    f.close()
    img_b64 = base64.b64encode(img)
    return img_b64

