from flask import Flask, render_template, jsonify, request
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Метрики Prometheus
REQUESTS = Counter('app_requests_total', 'Total number of page requests')
WATERINGS = Counter('app_waterings_total', 'Total number of plant waterings')

total_views = 0
total_waterings = 0

@app.route('/')
def index():
    global total_views
    total_views += 1
    REQUESTS.inc()
    return render_template('index.html', waterings=total_waterings, views=total_views)

@app.route('/water', methods=['POST'])
def water():
    global total_waterings
    total_waterings += 1
    WATERINGS.inc()
    return jsonify({'waterings': total_waterings})

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)