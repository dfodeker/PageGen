from flask import Flask,render_template
import requests
import json


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/create")
def create_page():

    headers = {
        'X-Shopify-Access-Token': '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',
        'Content-Type': 'application/json'
    }

    data = {
        "page": {
            "title": "New Page",
            "body_html": "Test 9",
        }
    }

    page = {}
    response = requests.get('https://derekstoreapps.myshopify.com/admin/api/2022-07/pages.json', headers=headers)
    pages = response.json()
    print(pages['pages'][0])
    if pages != None:
        for i in pages['pages']:
            print(i['title'])
            
            if data['page']['title'] == i['title']:
                page['title'] = i['title']
                page['id'] = i['id']
                break

    print(page)
    if page:
        print('https://derekstoreapps.myshopify.com/admin/api/2022-07/pages.json'+str(page['id'])+'.json')
        response = requests.put('https://derekstoreapps.myshopify.com/admin/api/2022-07/pages.json'+str(page['id'])+'.json', headers=headers, data=json.dumps({"page": {"body_html": "Test 9",}}))
        print("updated")
    else:
        response = requests.post('https://derekstoreapps.myshopify.com/admin/api/2022-07/pages.json', headers=headers, data=json.dumps(data))
        # response.raise_for_status
        print("Added")

    return "Created"


