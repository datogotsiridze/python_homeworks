phone = {"giorgi": "599123456", "mariami": "555123456", "dato": "551123456", "nino": "593123456", "sos": "112"}
name = input("say name, whose number you need: ").strip().lower()
if name in phone:
    print(f"{name} has number: {phone[name]} ")
else:
    print(f"sorry, we have person {name} not.")