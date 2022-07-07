words=input()
words=words.split(',')
l=len(words)
for i in range(l-1):
    for j in range(l-i-1):
        if(words[j]>words[j+1]):
            words[j],words[j+1]=words[j+1],words[j]
for i in range(l):
     if(i<l-1):
         print(words[i],end=',')
     else:
         print(words[i])