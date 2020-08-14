class text2base:
    def __init__(self, text:str, base:int):
        self.text = text
        self.base = base
        
    def encrypt(self)->str:
        encryptedText = ""        
        for j in range(len(self.text)-1, -1, -1):
            i = ord(self.text[j])            
            while(i!=0):
                if(self.base > 15 and i%16 > 9):
                    encryptedText += chr(i%self.base+55)
                else:
                    encryptedText += str(i%self.base)
                i = i//self.base
            if(ord(self.text[j]) < 63):
                encryptedText += '0'
        return encryptedText[::-1]
    
    def decrypt(self)->str:
        decryptedText = ""
        if self.base == 2:
            c = 7
        elif self.base == 4 or self.base == 3:
            c = 4
        elif (self.base >= 5 or self.base <= 8 or self.base == 11 or self.base == 17 or self.base == 18 or self.base >= 22 or
              self.base <=27 or self.base >= 33 or self.base <=55):
            c = 3
        else:
            c = 2
            
        for i in range(c, len(self.text)+c, c):
            t = int(self.text[i-c:i])
            d = p = 0
            while(t!= 0):
                    d += (t%10)*self.base**p
                    p += 1
                    t = t//10
            decryptedText += chr(d)
        return decryptedText


x = text2base("Hello World!", 2)
print(x.encrypt())
# Output: 100100011001011101100110110011011110100000101011111011111110010110110011001000100001

print()

y = text2base(x.encrypt(), 2)
print(y.decrypt())
#Output: Hello World!
        
