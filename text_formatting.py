import re
pattern=r'[\"]'
replacement=' '

input_text='"whoa"he said when he saw me I replied with"whatsup my dude""nothing as such"'
formatted_text=re.sub(pattern, replacement,input_text)
print(formatted_text)