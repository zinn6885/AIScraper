import json
import sys
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field


model = OllamaLLM(model="llama3")

template = (
    "Produce the price of {product} per {measurement} in {location} with no other text."
    "Return as a JSON object with a product field and price field and a measurement field"
    "Again. no other text. I do not care about any error or issues you have with the question."
    "I do not care about where you got the ingformation from. follow the format"
)

def checkPrice(product, measurement, location):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    parsed_results = []
    response = chain.invoke({"product": product})

    parsed_results.append(response)

    return "\n".join(parsed_results)

def jsonObject (product, measurement, location):
    bWorked = True
    
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    response = chain.invoke({"product": product, "measurement": measurement, "location": location})
    jstring = (response)
    while (bWorked):
        try:
            jobject = json.loads(jstring)
            bWorked = False
        except:
            response = chain.invoke({"product": product, "measurement": measurement, "location": location})

    return jobject
            
def checkPriceZip(product, measurement, zipcode):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    parsed_results = []
    response = chain.invoke({"product": product, "measurement": measurement, "zipcode": zipcode})

    parsed_results.append(response)

    return "\n".join(parsed_results)

# ingredients = ["Almond Meal", "Almonds", "Amaranth", "Apples", "Apricots", "Avocados", "Bananas", "Barley", "Beef",
#                 "Cheese", "Cherries", "Chia Seeds", "Chicken", "Chocolate", "Coconut", "Corn Flour", "Cornish Hens", 
#                 "Cornmeal", "Duck", "Flax Seeds", "Goat", "Ground Beef", "Ground Chicken", "Ground Pork", "Ground Turkey", 
#                 "Lamb", "Mangos", "Millet", "Mushroom", "Nectarines", "Oat Flour", "Oats", "Peaches", "Peanuts", "Pears",
#                 "Pineapples", "Plums", "Pomegranates", "Pork", "Quinoa", "Sausage", "Seafood", "Shellfish", "Sirloin",
#                 "Spelt", "Steak", "Tapioca Flour", "Turkey", "Veal", "Venison", "White Rice Flour", "Wild Game", "Wild Rice"]
# for i in ingredients: 
#     print(checkPrice(i, "pound"))


print(jsonObject("Fuji Apple", "Pound", "Tacoma, WA"))