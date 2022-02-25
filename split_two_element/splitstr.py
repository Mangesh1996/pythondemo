from operator import ne
import re



value = "\r\n\r\n\r\nValidation cost: 0.001250\r\nMean average_precision (in %): 77.1507\r\n\r\nclass name average precision (in %)\r\n------------ --------------------------\r\napple 94.4444\r\nbanana 81.8056\r\ngrapes 44.7712\r\nwatermelon 87.5817\r\nmango 56.11\r\n\r\nMedian Inference Time: 0.024507\r\n"

# print(value)
new_value = value.split("--------------------------\r\n")[1]
sec_value=new_value.split("\r\n\r\nMedian Inference Time:",1)[0]
thi=sec_value.split("\n")
lst=[i.replace("\r","") for i in thi]
tes=" ".join(lst)
result=tes.split(" ")
print(result)

#['apple','94.4444','banana','81.8056','grapes','44.7712','watermelon','87.5817']