
fp = open("C:\\bharat.bhushan\\python.txt","w+")
fp.write("Python is Fun")
fp.seek(0)
print(fp.read())
fp.close()