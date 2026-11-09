# Practice - Transaction processing

# Identify duplicate transaction IDs.
# Retain only the first occurrence.
# Calculate total transaction value.
# Calculate customer-wise transaction totals.

transactions = [
    {"id": 101, "customer": "A", "amount": 500},
    {"id": 102, "customer": "B", "amount": 700},
    {"id": 103, "customer": "A", "amount": 300},
    {"id": 101, "customer": "A", "amount": 500},
    {"id": 104, "customer": "C", "amount": 900}
]

unique_transactions = {}
customer_totals = {}

for transaction in transactions:

    # print ("one", transaction["id"])

    transaction_id = transaction["id"]

    if transaction_id not in unique_transactions:
        # print ("transaction_id", transaction_id)

        unique_transactions[transaction_id] = transaction

        customer = transaction["customer"]
        amount = transaction["amount"]
        
        customer_totals[customer] = (
            customer_totals.get(customer,0) + amount
        )

      # print(customer)   
      # print(amount)
      # print (customer_totals)        

total_amount = sum(
    item["amount"] 
    for item in unique_transactions.values()
)

print("unique transactions:", len(unique_transactions))
print("Total amount: ", total_amount)
print("Customer totals:", customer_totals)


# this example combines:
#- Lists.
#- Dictionaries.
#- Loops.
#- Conditional logic.
#- Dictionary lookups.
#- Comprehensions.
#- Aggregation.
