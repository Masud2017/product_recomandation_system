from pymongo import MongoClient

class ProductRecommander:
    def __init__(self,collection_one,collection_two,db_client):
        self.collection_one = collection_one
        self.collection_two = collection_two
        self.db_client = db_client

    def get_restaurant_data(self):
       
        return list(self.collection_one.find())

    # existing user stuff
    def get_recommandation_list_for_new_user(self):
        pipeline = [
            {
                "$lookup": {
                    "from": "cusine_and_type",
                    "localField": "placeID",
                    "foreignField": "placeID",
                    "as": "cuisine"
                }
            },
            {
                "$unwind": "$cuisine"
            },
            {
                "$group": {
                    "_id": "$cuisine.Rcuisine",
                    "occurrences": { "$sum": 1 },
                    "restaurants": { "$push": "$$ROOT" }
                }
            },
            {
                "$sort": { "occurrences": -1 }
            },
            {
                "$project": {
                    "_id": 0,
                    "cuisine": "$_id",
                    "occurrences": 1,
                    "restaurants": {
                        "$slice": [ "$restaurants", 10 ]
                    }
                }
            }
        ]

        return list(self.collection_one.aggregate(pipeline))
        
    def get_recommandation_list_for_existing_user(self,result_count):
        restaurant_list = self.get_restaurant_data()
        avg_rating_list = []

        for restaurant_item in restaurant_list:
            sum_item = (int(restaurant_item["rating"]) + int(restaurant_item["food_rating"]) + int(restaurant_item["service_rating"])) // 3
            
            avg_rating_list.append({"placeID":restaurant_item["placeID"], "avg_rating": sum_item})

        print(avg_rating_list)


# test code
if __name__ == "__main__":
    mongoClient = MongoClient("localhost",27017)

    db = mongoClient.recomandation_system
    restaurants_visited_collection = db.restaurants_visited
    cusine_and_type_collection = db.cusine_and_type
    recommander = ProductRecommander(restaurants_visited_collection,cusine_and_type_collection,mongoClient)

    # recommander.get_recommandation_list_for_existing_user(10)

    for x in recommander.get_recommandation_list_for_new_user():
        # print(x)
        print(x["cuisine"])

