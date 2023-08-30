class Person:
    # def __init__(self, name, age) -> None:
    #     self.name = name
    #     self.age = age

    def get_name(self):
        print(f"Name is {self.name}")

    def __repr__(self) -> str:
        return f"name={self.name}. {self.age=}"


team = [
    {"name": "John", "age": 12},
    {"names": "Marry", "age": 22},
]

# john = Person(name="John", age=12)
john = Person()
john.name = "John"
john.age = 12
marry = Person()
# marry = Person(name="Marry", age=22)

print(john.name)
marry.name

# john.get_name()
# marry.get_name()

print(john)


# # print(team[1]["name"])
# for i in range(10):
#     if not team[i].get("name"):
#         print(f"No name in {team[1]}")
#     else:
#         print(team[1]["name"])