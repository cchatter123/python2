import base64 

# FILE NAME - decoding.py

# NAME - Oliver Doty
# DATE - 4/18/2025
# DESCRIPTION - 




file_path = input("File name? ")
file = open(file_path, 'r')
data = file.read()
decoded_data = base64.b64decode(data)
print(decoded_data)
file.close()
# GET DATA

    
    
    
    # OUTPUT DECODED DATA