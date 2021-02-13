x = input("enter your message here")
print("message 1")
for i in range(26):
    for j in x:
         k = (ord(j) + i)
         if k > 122:
             k = k - 26
         print(chr(k))
    print("message", i + 2)
    #zkc