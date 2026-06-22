product_price_2016 = {"bread": 1, "egg": 0.3, "cooking_oil": 2.5,  }
product_price_2026 = {"bread": 2, "egg": 0.5, "cooking_oil": 4.5,  }
print(f"last decade we have big inflation. for this three product : bread= {product_price_2026['bread']/product_price_2016['bread']*100}% egg={round(product_price_2026['egg']/product_price_2016['egg']*100)}% and cooking oil={round(product_price_2026['cooking_oil']/product_price_2016['cooking_oil']*100)}% ")
product_price_2016["cigarette"] = 3
product_price_2026["cigarette"] = 7.5
print(f"for example, when last time I quit smoking, cigarette was cheaper {product_price_2026['cigarette']/product_price_2016['cigarette']} times")