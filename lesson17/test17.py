class Person():
    def __init__(self, name, age=18, weight=68, hieght=170):
        self.name = name
        self.age = age
        self.weight = weight
        self.hieght = hieght

    def describe(self):
        print(f"姓名:{self.name}")
        print(f"AGE:{self.age}")
        print(f"Weight:{self.weight}")
        print(f"Hieght:{self.hieght}")


p1 = Person('天母米樂金')

p1.describe()


class Student(Person):
    def __init__(self, name, id):
        kwargs = {'age': 25, 'weight': 78, 'hieght': 189}
        super().__init__(name, **kwargs)
        self.id = id

    def describe(self):
        print(f"id:{self.id}")
        print()
        super().describe()


stud1 = Student(name="米樂金", id="668899")
stud1.describe()
