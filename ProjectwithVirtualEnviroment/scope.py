import json

def myfunc():
  x = 300
  def myinnerfunc():
    x = 200
    print(x)
  myinnerfunc()

myfunc()


# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])