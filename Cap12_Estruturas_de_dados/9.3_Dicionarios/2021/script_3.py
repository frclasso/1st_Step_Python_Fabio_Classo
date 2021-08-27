# USING FROMKEYS() METHOD

# initializing sequence 
seq = { 'a', 'b', 'c', 'd', 'e' }
  
# using fromkeys() to convert sequence to dict 
# initializing with None
res_dict = dict.fromkeys(seq)
  
# Printing created dict
print (res_dict)
  
  
# using fromkeys() to convert sequence to dict 
# inserting the value 1 for all keys
res_dict2 = dict.fromkeys(seq, 1)
  
# Printing created dict
print (res_dict2)