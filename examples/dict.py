# This is particularly important for data engineering and API development.
customer = {
            "id":1,
            "name": "senthil",
            "city": "chennai"
            }
print(customer["name"])
# customer["email"] raises KeyError if the key does not exist.
print(customer.get("email"))

#Other methods used frequently 
print (f"keys : {customer.keys()}")
print (f"values: {customer.values()}")
print (f"items: {customer.items()}")
print (f"id value: {customer.get("id")}")
#update dict item value
customer.update({"city": "Bengaluru"})
print (f"items update: {customer.items()}")
#remove dict item
customer.pop("id")
print (f"items remove: {customer.items()}")
