from flask import Flask, request, Response
import requests
from playwright.sync_api import sync_playwright
app = Flask(__name__)





def fetch_page(url):

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-dev-shm-usage"
            ]
        )

        page = browser.new_page()

        page.goto(url, timeout=60000)

        html = page.content()

        browser.close()

        return html



@app.route("/proxy/<path:url>")
def proxy(url):

    if not url.startswith("http"):
        url = "https://" + url

    html = fetch_page(url)

    return Response(html, mimetype="text/html")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
