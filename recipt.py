coffee_price = 5 #price of coffee
muffin_price = 4 # price of muffins
cookie_price = 2
milk_price = 3

amount_of_milk = int(input("How much milk will you be ordering:"))
amount_of_cookie = int(input("How many cookies will you be ordering:"))
amount_of_coffee = int(input("How many coffees will you be ordering:"))
amount_of_muffin = int(input("How many muffins will you be ordering:"))

tax = 6  #tax percentage of total product
tax_total = (cookie_price * amount_of_cookie+milk_price * amount_of_milk+coffee_price * amount_of_coffee+muffin_price * amount_of_muffin)*tax/100 #the amount of money owed on tax

c_plurality = "Coffee" #sets up whether the plural should be used when talking about product
m_plurality = "Muffin" # m for muffin
ck_plurality = "Cookie" #ck for cookie :)
mk_plurality = "Milk" # mk for milk

if amount_of_coffee > 1:        #if there is multiple of products add s to end
    c_plurality = "Coffees"
if amount_of_muffin > 1:
    m_plurality = "Muffins"
if amount_of_milk > 1:
    mk_plurality = "Milks"
if amount_of_cookie > 1:
    ck_plurality = "Cookies"

print("*************************")
print("My Coffee and Muffin Shop")
print("Number of coffees bought?")
print(amount_of_coffee)
print("Number of muffins bought?")
print(amount_of_muffin)
print("Number of cookies bought?")
print(amount_of_cookie)
print("Number of milks bought?")
print(amount_of_milk)

print("*************************")
print("")
print("*************************")
print("My Coffee and Muffin Shop Receipt")
print(f"{amount_of_coffee}  {c_plurality} at {coffee_price} each: {coffee_price * amount_of_coffee}")#price times amount to give total cost of one product
print(f"{amount_of_muffin}  {m_plurality} at {muffin_price} each: {muffin_price * amount_of_muffin}")
print(f"{amount_of_cookie}  {ck_plurality} at {cookie_price} each: {cookie_price * amount_of_cookie}")#price times amount to give total cost of one product
print(f"{amount_of_milk}  {mk_plurality} at {milk_price} each: {milk_price * amount_of_milk}")#price times amount to give total cost of one product
print(f"{tax} tax: {tax_total}")
print("-------")
print(f"Total: {tax_total*100/tax+tax_total}") # lists total money owed
print("*************************")
print("thank you for your purchase")
