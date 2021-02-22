import requests
import json

if __name__ == '__main__':
    url = 'https://httpbin.org/post'
    payload = {
        'nombre': 'ivan',
        'curso': 'python',
    }

    response = requests.post(url, data= json.dumps(payload))
    print(response.url)
    print(response.status_code)

    if response.status_code == 200:
        print(response.content)
        
        # response_json = json.loads(response.text)
        # origin = response_json['origin']
        # print(origin)
        # print(response_json)
        # print(response_json['args']['curso'])  