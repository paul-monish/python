import os
fp=open('file1.txt','r')
l=list(fp.read())
print("file size: ",len(l),"bytes")
print("file size: ",os.stat('file1.txt').st_size,"bytes")
fp.close()
