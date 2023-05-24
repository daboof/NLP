import re
pattern=r"\bcats\b"
replacement="dogs"

input_text=input("please tell us about your problem")
formatted_text=re.sub(pattern, replacement,input_text)
print(formatted_text)