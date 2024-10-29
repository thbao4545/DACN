# import the existing word and sentence tokenizing  
# libraries 
from nltk.tokenize import sent_tokenize, word_tokenize 

text = "Ngã tư Thủ Đức trên đường Xa lộ Hà Nội đang kẹt xe!"

print(sent_tokenize(text)) 

print(word_tokenize(text)) 
