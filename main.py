import requests
url = 'https://duckduckgo.com/?q=presidents+of+the+united+states&format=json'
response = requests.get(url)

my_json = response.json()

for key in my_json['RelatedTopics']:
    print(key['Text'])



