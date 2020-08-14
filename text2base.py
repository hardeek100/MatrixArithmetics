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
        print(c)
        for i in range(c, len(self.text)+c, c):
            t = int(self.text[i-c:i])
            d = p = 0
            while(t!= 0):
                    d += (t%10)*self.base**p
                    p += 1
                    t = t//10
            decryptedText += chr(d)
        return decryptedText
        
            
        

j = 2
for i in range(2, 1001):
    c = "A"
    j += 1
    x = text2base(c, i)
    y = text2base(c,j)
    print(f"Ascii of:{c}  Encrypted: {x.encrypt()} {i} {len(x.encrypt())}")
    if(x.encrypt() == y.encrypt()):
        break;
