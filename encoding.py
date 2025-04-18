import base64 

# FILE NAME - encoding.py

# NAME - Oliver Doty
# DATE - 4/18/2025
# DESCRIPTION - 

  
file_path = input("File name? ")
file = open(file_path, 'r')
data = file.read()
encoded_data = base64.b64encode(data.encode('utf-8'))
print(encoded_data)
file.close()
