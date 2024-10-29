# import the existing word and sentence tokenizing  
# libraries 
from nltk.tokenize import sent_tokenize, word_tokenize 
  
text = "Đường Nguyễn Thái Bình đang kẹt xe"
  
print(sent_tokenize(text)) 
print(word_tokenize(text)) 
