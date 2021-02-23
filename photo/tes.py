import requests
import json

#photo.image.url
url = "https://api.cloudinary.com/v1_1/dysntklpm/image/upload"
payload = {
           'file': 'https://ivanportafolio.herokuapp.com/static/images/not.png',
            'upload_preset': 'capama',
            'cloud_name': 'dysntklpm',
            'folder': 'reportes_usuario',
        }
response = requests.post(url, data=payload)
response_json = json.loads(response.text)
print(response_json['secure_url']) 



# CONEXIÓN CON POST A UNA API
#---------------------------------------------------------------
# if __name__ == '__main__':
#     url = 'https://httpbin.org/post'
#     payload = {
#         'nombre': 'ivan',
#         'curso': 'python',
#     }

#     response = requests.post(url, data= json.dumps(payload))
#     print(response.url)
#     print(response.status_code)

#     if response.status_code == 200:
#         print(response.content)
        
#         # response_json = json.loads(response.text)
#         # origin = response_json['origin']
#         # print(origin)
#         # print(response_json)
#         # print(response_json['args']['curso'])  
#---------------------------------------------------------------