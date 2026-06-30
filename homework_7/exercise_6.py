results = {"nino": 85 , "lado" : 93 , "gio" : 81 , "mari" : 75 , "soso": 72}
name = input("whose score? \n").lower()
      
try:
    answer = results[name]
    print(f"{name} has {answer} score")

except KeyError:
    print(f"no score for {name}")

      