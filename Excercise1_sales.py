print("****** Python Foundation Lab Started ******") # print function
 
# Step 2 - Create variables and data types
product = "Laptop" # string variable
quantity = 3 # int variable
unit_price = 1200.50 # float variable
in_stock = True # boolean variable
 
print("****** Variable values ******")
print("Product:", product)
print("Quantity:", quantity)
print("Unit Price:", unit_price)
print("In Stock:", in_stock)
 
print("****** Variable data types ******")
print(type(product))
print(type(quantity))
print(type(unit_price))
print(type(in_stock))

# Step 3 - Perform a sales calculation
total_sales = quantity * unit_price # calculate total sales
print("****** Sales Calculation ******")
print("Product:", product)
print("Quantity:", quantity)
print("Unit Price:", unit_price)
print("Total Sales:", total_sales)

#Step 4 - Apply Conditional Statements
if total_sales >= 2000:
    print("Sales target achieved!")
else:
    print("Sales target not achieved. Keep trying!")

# Step 5 - Process Multiple Sales using loop
sales = [1200, 850, 2400, 1750, 3200] # list of sales amounts
print("****** Processing Multiple Sales ******")
for sale in sales:
    if sale >= 2000:
        print(f"Sale amount {sale} - Target achieved!")
    else:
        print(f"Sale amount {sale} - Target not achieved. Keep trying!")