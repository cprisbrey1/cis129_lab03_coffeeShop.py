coffee_price = 5 #price of coffee
muffin_price = 4 # price of muffins

amount_of_coffee = int(input("How many coffees will you be ordering:"))
amount_of_muffin = int(input("How many muffins will you be ordering:"))

tax = 6  #tax percentage of total product
tax_total = (coffee_price * amount_of_coffee+muffin_price * amount_of_muffin)*tax/100 #the amount of money owed on tax

c_plurality = "Coffee" #sets up whether the plural should be used when talking about product
m_plurality = "Muffins"


if amount_of_coffee > 1:        #if there is multiple of products add s to end
    c_plurality = "Coffees"
if amount_of_muffin > 1:
    m_plurality = "Muffins"

print("*************************")
print("My Coffee and Muffin Shop")
print("Number of coffees bought?")
print(amount_of_coffee)
print("Number of muffins bought?")
print(amount_of_muffin)

print("*************************")
print("")
print("*************************")
print("My Coffee and Muffin Shop Receipt")
print(f"{amount_of_coffee}  {c_plurality} at {coffee_price} each: {coffee_price * amount_of_coffee}")#price times amount to give total cost of one product
print(f"{amount_of_muffin}  {m_plurality} at {muffin_price} each: {muffin_price * amount_of_muffin}")
print(f"{tax} tax: {tax_total}")
print("-------")
print(f"Total: {tax_total*100/tax+tax_total}") # lists total money owed
print("*************************")
