from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/proxy/<path:url>')
def proxy(url):
    target_url = f"https://{url}" if not url.startswith('http') else url
    
    resp = requests.get(target_url, stream=True)
    

    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.raw.headers.items()
               if name.lower() not in excluded_headers]

    return Response(resp.content, resp.status_code, headers) #teoretycznie tego statuscode i headers mogłoby nie być ale lepiej jak jest

