from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route("/code/<statuscode>")
@metrics.histogram('requests_by_status', 'Requests by status codes',
                   labels={'status': lambda r: r.status_code})
def code(statuscode):
    return { "statuscode": statuscode}, statuscode

if __name__ == "__main__":
    app.run()