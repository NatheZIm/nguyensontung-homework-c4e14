from mongoengine import Document, StringField , IntField

class Champ(Document):
    image = StringField()
    name = StringField()
    role = StringField()
    lore = StringField()
    money = IntField()
