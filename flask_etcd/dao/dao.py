import etcd3
from flask_etcd.config import config


class flask_etcd:
    def __init__(self, host, port):
        self.etcd_client = etcd3.client(host=host, port=port)
        # 观察者
        self.watcher = ""

    def __get__(self, instance, owner):
        return self

    def callback(self, event):
        print("Event type:", event.event_type)
        print("Key:", event.key)
        print("Value:", event.value)

    def watch_stop(self):
        # 停止
        self.etcd_client.cancel_watch(self.watcher)

    def watch_callback(self, watch_key):
        self.watcher = self.etcd_client.add_watch_callback(watch_key, self.callback)

    def put(self, key: str, value):
        """
        push data to etcd
        :param key:
        :param value:
        :return:
        """
        r = self.etcd_client.put(key, value, prev_kv=True)
        print(r)
        return r

    def get(self, key: str, serializable: bool):
        """
        get etcd key-v
        :param key: etcd-key
        :param serializable: return data serializable
        :return: value
        """
        r = self.etcd_client.get(key, serializable)
        print(r)
        return r


f_etcd = flask_etcd(config.ETCD_HOST, config.ETCD_PORT)
