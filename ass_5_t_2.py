import re
# create a list
original_list = list(range (1, 11))  

# covert list to  string
list_str = str(original_list)

#use regular expression
pat = r"\[(\d+,\s\d+,\s\d+,\s\d+,\s\d+)" # pat for find frist five number
match = re.search(pat, list_str)
 
if match:
    extr_str = match.group(1) # matchh str and covert into back list of integer
    extr_list = [int(x) for x in extr_str.split(", ")]

    rev_list = extr_list[::-1] #reverse the extracted element
print(f" original list: {original_list}")
print(f"extracted frist five element: {extr_list}")
print(f"reversal extracted element : {rev_list}")