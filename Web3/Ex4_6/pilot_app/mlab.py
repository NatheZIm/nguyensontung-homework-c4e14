import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds161306.mlab.com:61306/leauge  #database của mình

host = "ds161306.mlab.com"
port = 61306
db_name = "leauge"
user_name = "admin"
password = "admin"


def mlab_connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
