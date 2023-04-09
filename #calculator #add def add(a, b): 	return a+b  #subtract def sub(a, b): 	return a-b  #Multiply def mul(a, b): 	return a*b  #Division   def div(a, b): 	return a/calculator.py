#calculator
#add
def add(a, b):
	return a+b

#subtract
def sub(a, b):
	return a-b

#Multiply
def mul(a, b):
	return a*b

#Division  
def div(a, b):
	return a/b;

operators ={ 
	"+":add,
	"-":sub,
	"*":mul,
	"/":div,
}

num1=int(input("What's the first number:"))
num2=int(input("What's the second number:"))

for symbol in operators:
	print(symbol)

operation_symbol=input("Pick an operation from the above:")

calculation_function=operators[operation_symbol]
result=calculation_function(num1 , num2)

print(f"{num1} {operation_symbol} {num2} = {result}")

