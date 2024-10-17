from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = (
    "Produce the price of {product} per {measurement} in with no other text."
    "If the product is a fruit or vegtable give both an organic price and"
    "a conventional price. Still give no additional text"
)

model = OllamaLLM(model="llama3")


def checkPrice(product, measurement):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    parsed_results = []
    response = chain.invoke({"product": product, "measurement": measurement})

    parsed_results.append(response)

    return "\n".join(parsed_results)

template = (
    "Produce the price of {product} per {measurement} in {zipcode} with no other text."
    "If the product is a fruit or vegtable give both an organic price and"
    "a conventional price. Still give no additional text. provide the responce in json format like so:"
    "['name' : (product name), \n 'price' : (price)]"
)

def checkPriceZip(product, measurement, zipcode):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    parsed_results = []
    response = chain.invoke({"product": product, "measurement": measurement, "zipcode": zipcode})

    parsed_results.append(response)

    return "\n".join(parsed_results)

ingredients = ["Almond Meal", "Almonds", "Amaranth", "Apples", "Apricots", "Avocados", "Bananas", "Barley", "Beef",
                "Cheese", "Cherries", "Chia Seeds", "Chicken", "Chocolate", "Coconut", "Corn Flour", "Cornish Hens", 
                "Cornmeal", "Duck", "Flax Seeds", "Goat", "Ground Beef", "Ground Chicken", "Ground Pork", "Ground Turkey", 
                "Lamb", "Mangos", "Millet", "Mushroom", "Nectarines", "Oat Flour", "Oats", "Peaches", "Peanuts", "Pears",
                "Pineapples", "Plums", "Pomegranates", "Pork", "Quinoa", "Sausage", "Seafood", "Shellfish", "Sirloin",
                "Spelt", "Steak", "Tapioca Flour", "Turkey", "Veal", "Venison", "White Rice Flour", "Wild Game", "Wild Rice"]
for i in ingredients: 
    print(checkPriceZip(i, "pound", 98498))