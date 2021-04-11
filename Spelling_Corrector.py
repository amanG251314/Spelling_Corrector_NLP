from textblob import TextBlob
words=input('Enter words seperated by space \n').split(' ')
corrected_words = []
for i in words:
    corrected_words.append(TextBlob(i))
print("Wrong words :", words)
print("Corrected Words may be :")
for i in corrected_words:
    print(i.correct(), end=" ")