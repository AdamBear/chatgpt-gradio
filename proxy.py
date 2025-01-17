import requests
from flask import Flask, request, Response

app = Flask(__name__)

# @app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE'])
# @app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
# def proxy(path):
#     url = f'https://api.openai.com/{path}'
#     #headers = {'User-Agent': request.headers.get('User-Agent')}
#     headers = request.headers
#     data = request.get_data()
#     resp = requests.request(
#         method=request.method,
#         url=url,
#         headers=headers,
#         data=data,
#         cookies=request.cookies,
#         allow_redirects=True,
#         verify=False
#     )
#     print("request", path)
#     # excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
#     # headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
#     response = Response(resp.content, resp.status_code, resp.raw.headers)
#     return response

@app.before_request
def proxy():
    headers = {h[0]: h[1] for h in request.headers}
    path = request.path
    print("request path", path)
    url = f'https://api.openai.com/{path}'
    # 一些自己的逻辑...
    return requests.request(
        request.method, url, data=request.data, headers=headers, cookies=request.cookies, json=request.json
    ).content


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=88, ssl_context="adhoc")