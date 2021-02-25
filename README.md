# shopping-cart

[Project Description]
(https://github.com/prof-rossetti/intro-to-python/tree/master/projects/shopping-cart)

## Installation

Clone or download from [GitHub source] then navigate into the project repository 

```sh
cd shoppingcart
```
## Usage 

Run the program 

```py
python shopping_cart.py
```

## email receipt & flexible tax rate
Obtain an API Key from [SendGrid](https://app.sendgrid.com/settings/api_keys) services. Create a new file called ".env" in the root directory of this repo, and paste the following contents inside, using your own values as appropriate:

```sh
# .env example

SENDGRID_API_KEY="_______________"
MY_EMAIL_ADDRESS="hello@example.com"

tax_rate = "0.0875" # your respective state's tax rate 