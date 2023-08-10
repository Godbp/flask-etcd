
ENV = "dev"

if "dev" == ENV:
    ETCD_HOST = "localhost"
    ETCD_PORT = 2379
if "test" == ENV:
    pass

if "release" == ENV:
    pass

