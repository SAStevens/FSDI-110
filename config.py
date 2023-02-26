import pymongo
import certifi

con_str = "mongodb+srv://saseaa37:test1234@cluster0.ua72xem.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())
db = client.get_database("onlinestore")
