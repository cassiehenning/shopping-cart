# shopping_cart.py

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


# TODO: write some Python code here to produce the desired output

#print(products)
total_price = 0 
selected_ids = []
import datetime

while True: 
    selected_id = input("Please input a product identifier (type DONE when you're done):")
    if selected_id == "DONE": 
        break
    else:   
         #matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
         #matching_product = matching_products[0]
         #total_price = total_price + matching_product["price"]
         #print("SELECTED PRODUCT: " + str(matching_product["name"]) + " " + str(matching_product["price"])) 
         selected_ids.append(selected_id)
#print(matching_product)
#print(type(matching_product))

#print(selected_ids)
print("---------------------------------")
print("CASSIE'S GROCERY EXTRAVAGANZA")
print("---------------------------------")

# EMAIL 

print("Please visit our website at:")
print("WWW.CASSIES-GROCERY-EXTRAVANGANZA.COM")
print("---------------------------------")

#PHONE NUMBER 

print("Contact us at:")
print("+1-678-999-8212")
print("---------------------------------")

# DATE / TIME HERE 

import datetime #https://www.w3resource.com/python-exercises/python-basic-exercise-3.php
now = datetime.datetime.now()
print("Current Date & Time: ")
print(now.strftime("%Y-%m-%d %I:%M %p"))

print("---------------------------------")

for selected_id in selected_ids:
    matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
    matching_product = matching_products[0]
    total_price = total_price + matching_product["price"]
    print("SELECTED PRODUCT: " + str(matching_product["name"]) + " " + to_usd(matching_product["price"])) 
    
# PRICES & TAX 

import os
from dotenv import load_dotenv 
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

tax_rate= os.getenv("tax_rate", default = 0.0875)
tax= total_price * float(tax_rate)
final_total = total_price + tax


print("---------------------------------")
print("SUBTOTAL: " + to_usd(total_price)) 
print("TAX: " + to_usd(tax))
print("TOTAL: " + to_usd(final_total)) 


print("---------------------------------")
print("Thanks for shopping at Cassie's Grocery Extravaganza!")
print("We hope to see you soon!")
print("---------------------------------")

#send email receipt

#TRY THIS IN EMAIL_RECIEPT

email = input ("Email receipt? y/n: ")

if email == "y":

    import os
    from dotenv import load_dotenv 
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail

    load_dotenv()

    SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
    SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")

    client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
    print("CLIENT:", type(client))

    subject = "Your Receipt from Cassie's Grocery Extravaganza"

    #html_list_item = "<li>You ordered: Product 2</li>"
    #html_list_items += "<li>You ordered: Product 3</li>"


    html_content = f"""
    <body style="background-color:powderblue;">
    <h3>Hello this is your receipt!</h3>
    <p>Date: {now.strftime('%A, %B %d, %Y')}</p>
    <p>Subtotal: {to_usd(total_price)}</p>
    <p>Tax: {to_usd(tax)}</p>
    <p>Total: {to_usd(final_total)}</p>
    <p>Have a good day!<p>
    <p>Thanks for shopping at CASSIE'S GROCERY EXTRAVAGANZA<p>
    """
    print(html_content)

    # FYI: we'll need to use our verified SENDER_ADDRESS as the `from_email` param
    # ... but we can customize the `to_emails` param to send to other addresses
    message = Mail(from_email=SENDER_ADDRESS, to_emails=SENDER_ADDRESS, subject=subject, html_content=html_content)

    try:
        response = client.send(message)

        print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
        print(response.status_code) #> 202 indicates SUCCESS
        print(response.body)
        print(response.headers)

    except Exception as err:
        print(type(err))
        print(err)
else:
    print("Have a good day.")







