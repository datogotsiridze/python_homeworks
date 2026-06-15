picnic_products = ["beer", "cigarette", "pork", "bread", "cheese", "tomato"]
for i in range(len(picnic_products)):
    print(f"{i+1} {picnic_products[i]}" )
print(f"you have {len(picnic_products)} products. first prodact is {picnic_products[0]} and last prodact is {picnic_products[-1]}. ")
if picnic_products[0] == "beer":
    print("you are my man bro :d")
