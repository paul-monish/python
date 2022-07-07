try:
    fp=open('file1.txt','r')
    str1=fp.readlines()
    print(str1)
except:
    print("File not exist!!")
finally:
    fp.close()
