def to_farenheit(celsius):
    return  round(celsius*9/5+32.1)

celsius = float(input(" ზუსტად რამდენი გრადუსია შეგიძლია მითხრა? "))

print(f"  ეხლა არის {celsius} გრადუსი ცელსიუსი, რაც უდრის {to_farenheit(celsius)} გრადუს ფარენჰეიტს. ")