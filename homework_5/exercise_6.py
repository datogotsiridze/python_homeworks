products = [ "bread", "butter", "cheese", "beer", "tomato", "beer", "bread", "iogurt", "bread"]

client = input("which product do you need? \n").strip().lower()

if client in products:
    print(f"yes, {client} we have {products.count(client)} times")
else:
    print(f" sorry, we have not this product. ")

