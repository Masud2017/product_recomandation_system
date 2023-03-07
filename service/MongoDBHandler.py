from pymongo import MongoClient

mongoClient = MongoClient("localhost",27017)

db = mongoClient.recomandation_system
restaurants_visited_collection = db.restaurants_visited
cusine_and_type_collection = db.cusine_and_type

# handler functions

def update_existing_dataset_with_openapi_images():
    pass

def get_all_restaurant_visited_data():
    pass

def get_all_cusine_and_type_data():
    pass

