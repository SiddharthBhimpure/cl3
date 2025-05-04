import Pyro4

@Pyro.expose
class StringConcatenator():
    def concatenator(self,str1,str2):
        return str1+str2
daemon=Pyro4.Daemon()
uri=daemon.register(StringConcatenator())
print(uri)
daemon.requestLoop()

import Pyro4
uri=input("Enter the URI")
concatenator=Pyro4.Proxy(uri)
str1=input("Enter string 1")
str2=input("Enter string 2")
result=concatenator.concatenate(str1,str2)
print(result)



####PALINDROM#####


import Pyro4

@Pyro4.expose
class PalindromeChecker():
    def is_palindrome(self, text):
        cleaned = text.lower().replace(" ", "")  # Optional: remove spaces and lowercase
        return cleaned == cleaned[::-1]

daemon = Pyro4.Daemon()
uri = daemon.register(PalindromeChecker)
print("Server is ready. URI is:", uri)
daemon.requestLoop()



import Pyro4

uri = input("Enter the URI shown by the server: ")
checker = Pyro4.Proxy(uri)

user_input = input("Enter a string to check if it's a palindrome: ")
result = checker.is_palindrome(user_input)

if result:
    print("Yes, it's a palindrome!")
else:
    print("No, it's not a palindrome.")
