from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/proxy/<path:url>')
def proxy(url):
    target_url = f"https://{url}" if not url.startswith('http') else url
    head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
    resp = requests.get(target_url, stream=True, headers=head)
    

    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.raw.headers.items()
               if name.lower() not in excluded_headers]

    return Response(resp.content, resp.status_code, headers) #teoretycznie tego statuscode i headers mogłoby nie być ale lepiej jak jest ------ tylko jest problem bo nie mam tam połączenia z internetem(jest to na render.com)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
