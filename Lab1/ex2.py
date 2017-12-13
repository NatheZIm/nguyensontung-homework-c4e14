from pymongo import MongoClient


client = MongoClient("mongodb://admin:admin@ds021182.mlab.com:21182/c4e")

db = client.get_default_database()

base = db['posts']

new_post = {
    'title' : 'Nguyễn Sơn Tùng',
    'author' : 'Internet',
    'content' : '''Roses are red
    Violet are blue
    When i take a shit
    I'm thingking about you  :)))
            
'''
}

base.insert_one(new_post)
