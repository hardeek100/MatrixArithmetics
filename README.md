# Python-Scripts
Python scripts that I wrote in my free time.


Text2Base:
This python script encrypts a text message to base. Here's how it works:
For eg, If we have a text, "AB CD", we take each character in the string and get its ASCII value which is a decimal number. Then convert that decimal to desired base number
and append its value in a encrypted string.
A = (65)10  ==> (1000001)2
B = (66)10  ==> (1000010)2
  = (32)10  ==> (0100000)2  (Adding a 0 in front because all the letters are 7 bits)
C = (67)10  ==> (1000011)2
D = (68)10  ==> (1000100)2

So, the resulting encrypted string becomes '10000011000010010000010000111000100'
