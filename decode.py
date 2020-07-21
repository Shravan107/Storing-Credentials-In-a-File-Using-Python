def decode(key,string):
  s = string[:key]
  print(s[::-1])
  
key =  int(input("enter key:"))
string = input("Enter string:")
decode(key,string)