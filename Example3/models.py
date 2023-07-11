from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

user = User(name='Ivan', age=17) 

print(user) # вывести User
print(user.json()) # вывести в формате json
print(user.json(exclude={'name'})) # вывести всего User но исключить поле name
print(user.json(include={'name'})) # вывести User но включить только поле name
