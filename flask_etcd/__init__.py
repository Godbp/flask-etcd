from flask import Flask
from flask_etcd.views import config, request_grpc

app = Flask(__name__)

app.add_url_rule("/config", "config", config, methods=["GET", "PUT"])
app.add_url_rule("/grpc", "grpc", request_grpc, methods=["POST"])
