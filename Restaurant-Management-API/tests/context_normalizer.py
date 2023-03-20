# """
# get all food names to scrape website -> https://yummly.com
# """

def normalized():
    with open("D:/Projects/Restaurant-Management-API/food_names.txt", "r") as file:
        content = file.read().split("\n")
    return content
import requests

# for i in range(10000):
#     print(f"Row {i} started")
#     client = requests.post(
#         url="http://127.0.0.1:8000/api/recipes/", 
#         json={
#             "food_name": f" {str(i)} Saasasasdasdlasd2",
#             "image_link": "https://www.youtube.com",
#             "description": "Fuck youidshajkdBAGSDGdgasdjkhgasdjgahjksdgfsgfjhagsdjfhgasjfgjkahsdgfjahsfbdnfbasfmasdf too",
#             "recipe": [
#                 {
#                     "ing": "Qweqwe", 
#                     "qua": "werwer"
#                 },
#                 {
#                     "ing": "Qweqwe", 
#                     "qua": "werwer"
#                 },
#                 {
#                     "ing": "Qweqwe", 
#                     "qua": "werwer"
#                 },
#                 {
#                     "ing": "Qweqwe", 
#                     "qua": "werwer"
#                 },
#                 {
#                     "ing": "Qweqwe", 
#                     "qua": "werwer"
#                 },
#                 {
#                     "ing": "Qweqwe", 
#                     "qua": "werwer"
#                 },
#                 {
#                     "ing": "Qweqwe", 
#                     "qua": "werwer"
#                 }
#             ]
#         },
#         headers={
#             "Authorization": "Token 98cdc132bf9467c211882d4dba1769e95a6a01d7"
#         },
#     )
# print(client.status_code)
# print(client.text)

import bs4




def get_list_of_foods(food_name):
    link = f"https://www.yummly.com/recipes?q={food_name}"
    html = requests.get(link).text
    soup = bs4.BeautifulSoup(html, "html.parser")
    links = soup.find_all("a", class_="link-overlay")
    scraping_list = []
    for i in links:
        scraping_list.append("https://www.yummly.com" + str(i.get("href")))
    return scraping_list

def food_name(link):
    prefix = '<h1 class="recipe-title font-bold h2-text primary-dark">'
    html = requests.get(link).text
    soup2 = bs4.BeautifulSoup(html, "html.parser")
    food_name = str(soup2.find_all("h1")[0])[len(prefix):].split("<")[0]
    open("index.html", "ab").write(str(soup2.find("div", class_="recipe-details-image")).encode("utf-8"))
    return food_name

def food_recipe(link):
    returnal_list = []
    request = requests.get(link).text
    soup = bs4.BeautifulSoup(request)
    recipe = soup.find_all("span", class_="ingredient")
    for i in recipe:
        recipe = (str(i)[len('<span class="ingredient">'):].split("<")[0]).encode("utf-8")
        returnal_list.append(recipe) 
    returnal_list = [n.decode() for n in returnal_list]
    return returnal_list

def food_amount(link):
    request = requests.get(link).text
    soup = bs4.BeautifulSoup(request)
    amounts = soup.find_all("span", class_="amount")
    returnal_list = []
    for i in amounts:
        amount = (str(i.findChildren("span", recursive=False)[0].string)).encode("utf-8")
        if i.findChildren("span", recursive=False)[0].string is None:
            data = ""
            for j in i.findChildren("span", recursive=False)[0]:
                data += j.string
            amount = data.encode("utf-8")
            returnal_list.append(amount)
        returnal_list.append(amount)
    returnal_list = [k.decode() for k in returnal_list]
    return returnal_list

def food_unit(link):
    request = requests.get(link)
    soup = bs4.BeautifulSoup(request.text)
    units = soup.find_all("li", class_="IngredientLine")
    lst = []
    for unit in units:
        check = unit.find("span", class_="unit")
        if check is not None:
            lst.append(str(check)[len('<span class="unit">'):].split("<")[0])
        else:
            lst.append("")
    return lst

# Token 98cdc132bf9467c211882d4dba1769e95a6a01d7
def recipes(link):
    recipes_list = []
    for _ in range(len(food_recipe(link))):
        recipes_list.append(f"{food_amount(link)} {food_unit(link)}")
    return recipes_list

print(recipes("https://www.yummly.com/recipe/Israeli-Salad-1228656"))
# print(food_unit("https://www.yummly.com/recipe/Israeli-Salad-1228656"))
