from flask import request, jsonify

from flask_etcd.dao.dao import f_etcd


def config():
    if "GET" == request.method:
        data = request.get_json()
        r = f_etcd.get(data.get("etcd_key", ""), True)
        return jsonify({'message': r})

    if "PUT" == request.method:
        data = request.get_json()
        etcd_key = data.get("etcd_key", "")
        etcd_value = data.get("etcd_value", "")
        watch = data.get("watch", False)
        if 0 == len(etcd_key) or 0 == len(etcd_value):
            return jsonify({})
        r = f_etcd.put(etcd_key, str(etcd_value))
        if watch:
            f_etcd.watch_callback(etcd_key)
        return jsonify({'message': str(r)})


def request_grpc():
    data = request.get_json()
    func = data.get("func", "")
    param = data.get("param", "")
    if 0 == len(func):
        return jsonify({})
    ff = globals()[func]
    res = ff(param)
    return jsonify({"message": res})


