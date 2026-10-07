from abc import ABC, abstractmethod


class Employee(ABC):

    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def get_salary(self):
        pass


class Developer(Employee):

    def work(self):
        print("Developer is writing code.")

    def get_salary(self):
        print("Salary: 30,000")


class Teacher(Employee):

    def work(self):
        print("Teacher is teaching.")

    def get_salary(self):
        print("Salary: 25,000")

developer = Developer()
teacher = Teacher()

developer.work()
developer.get_salary()

teacher.work()
teacher.get_salary()