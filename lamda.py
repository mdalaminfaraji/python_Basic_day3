
def doubled(x):
    return x*2
result=doubled(4)
print(result)
doubled=lambda x:x*2
print(doubled(45))
numbers=[12,34,54,56,45]
doubled_nums=map(doubled, numbers)
print(list(doubled_nums))

actors=[
    {'name':'sava', 'age':433},
    {'name':'sava', 'age':23},
    {'name':'sava', 'age':345},
    {'name':'sava', 'age':45},
    {'name':'sava', 'age':3},
]
juniors=filter(lambda actor:actor['age']<100, actors)
print(list(juniors))

person_info = {"name": "Sakib", "salary": 80000}
value = person_info.get("salary")
print(value)