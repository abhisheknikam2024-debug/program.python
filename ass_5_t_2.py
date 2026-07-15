import re
# create a list
original_list = [1,2,3,4,5,6,7,8,9,10]
          
extr_str = original_list[ :5] # matchh str and covert into back list of integer

rev_list = extr_str[::-1] #reverse the extracted 

print(f" original list: {original_list}")
print(f"extracted frist five element: {extr_str}")
print(f"reversal extracted element : {rev_list}")
