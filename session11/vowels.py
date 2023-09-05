text=(input('give me a word or text: '))
vowels=['a', 'e', 'i', 'o', 'u']
new_text=[]
for i in text:
    if i in vowels:
        i=i.replace(i,'!')
    new_text.append(i)
    text="".join(new_text)
print(text)