from xmlrpc.server import SimpleXMLRPCServer

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    
server=SimpleXMLRPCServer(('localhost',8000))
server.register_function(factorial,'calculate_factorial')
server.server_forever()
####
import xmlrpc.client

def main():
    server=xmlrpc.client.ServerProxy('http://localhost:8000')
    n=int(input("Enter the number : "))
    result=server.calculate_factorial(n)
    print(result)
if __name__=="__main__":
    main()


***Arithmetic***

from xmlrpc.server import SimpleXMLRPCServer

# Arithmetic operation functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Start XML-RPC server
server = SimpleXMLRPCServer(("localhost", 8000))
print("Server is running on port 8000...")

# Register functions
server.register_function(add, "add")
server.register_function(subtract, "subtract")
server.register_function(multiply, "multiply")
server.register_function(divide, "divide")
server.register_function(factorial, "factorial")

server.serve_forever()



import xmlrpc.client

def main():
    server = xmlrpc.client.ServerProxy("http://localhost:8000")
    print("Choose operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Factorial")

    choice = int(input("Enter your choice (1-5): "))

    if choice in [1, 2, 3, 4]:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        if choice == 1:
            result = server.add(a, b)
        elif choice == 2:
            result = server.subtract(a, b)
        elif choice == 3:
            result = server.multiply(a, b)
        elif choice == 4:
            result = server.divide(a, b)

    elif choice == 5:
        n = int(input("Enter a number: "))
        result = server.factorial(n)
    else:
        result = "Invalid choice!"

    print("Result:", result)

if __name__ == "__main__":
    main()


