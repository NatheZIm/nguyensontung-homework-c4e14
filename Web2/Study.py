1. "There's no  duplicate because it's like an identity card, it only have one id per record.
    "The ID helps you to tell the difference between variants that have the same name"

2. # to find document based on id
Docs.objects.get(id='4f4381f4e779897a2c000009')
#or
import bson
Doc.objects.get(id=bson.objectid.ObjectId('4f4381f4e779897a2c000009'))
3. # to delete the record
# You can either delete an single Document instance by calling its delete method:
x = Service.objects.first() // Get a single 'Food' instance
x.delete() // Delete it!
# Or you can delete all items matching a query like so:
service.objects(type="snacks").delete()
