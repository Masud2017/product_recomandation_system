import openai
from pymongo import MongoClient
import time
from concurrent.futures import ThreadPoolExecutor

class ImageGeneratorBasedOnCusineName:
    def __init__(self,cusine_name):
        self.mongoClient = MongoClient("localhost",27017)
        self.db = self.mongoClient.recomandation_system
        self.image_collection = self.db.cusine_images

        self.cusine_name = "A restaurant dish image for the cusine name : "+cusine_name+". The image should look like it is from dish menu"
        
        # self.image_dir = "../storage"

        self.token_list = [""]

        openai.api_key = "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"
        response = openai.Completion.create(model="text-davinci-003", prompt="Say this is a test", temperature=0, max_tokens=7)

        response = openai.Image.create(
        prompt=self.cusine_name,
        n=1,
        size="1024x1024"
        )
        image_url = response['data'][0]['url']
        print(image_url)

    '''
    Generates image from openai api.
    @param cusine_name
    '''
    def generate_image(self,cusine_name):
        response = openai.Image.create(
        prompt="A restaurant dish image for the cusine name : "+cusine_name+". The image should look like it is from dish menu",
        n=1,
        size="1024x1024"
        )
        image_url = response['data'][0]['url']

        return image_url


    def generate_images_for_mongo_data(self,cusine_and_type_collection):
        future_list = []

        counter = 0

        with ThreadPoolExecutor(max_workers=10) as executor:
            for cusine_item in cusine_and_type_collection:
                if (counter == 49):
                    time.sleep(60)
                    counter = 0
                print(cusine_item["Rcuisine"])
                future_list.append(executor.submit(self.generate_image,cusine_item["Rcuisine"]))
                counter = counter + 1


            for x in future_list:
                print(x.result())


if __name__ == "__main__":
    generator = ImageGeneratorBasedOnCusineName("chinese")

    client = MongoClient("localhost",27017)
    db = client.recomandation_system
    cusine_type = db.cusine_and_type

    generator.generate_images_for_mongo_data(cusine_type.find())