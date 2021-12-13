

class Schedule:
    
    def __init__(self, courses=[]):
        self.courses = courses

    @property   # decorator for the getter
    def courses(self):
        return self._courses

    @courses.setter
    def courses(self, new_courses):
        # additional input validation
        # ex: limit max number of courses
        self._courses = new_courses

    # additional methods
    def add_course(self, course):
        "Take in a Course object. Adds it to the schedule."
        self._courses.append(course)

    def drop_course(self, course):
        if course in self._courses:
            self._courses.remove(course)

    def __str__(self):
        result = ''
        for course in self._courses:
            result += f"\n{course}"

        if result == '':
            return "No classes scheduled"

        return result

class Course:
    
    def __init__(self, subject, number):
        self.subject = subject
        self.number = str(number)

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value

    def __str__(self):
        return f"{self.subject} {self.number}"


class Person:
    current_id = 1

    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year
        self.schedule = Schedule()      # represents a "has a" relationship. A person has a schedule.
        self.id = Person.current_id
        Person.current_id += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def birth_year(self):
        return self._birth_year

    @birth_year.setter
    def birth_year(self, value):
        self._birth_year = value
    
    @property
    def schedule(self):
        return self._schedule

    @schedule.setter
    def schedule(self, value):
        self._schedule = value
    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    # additional methods
    def view_schedule(self):
        return f"{self.name}'s Schedule:\n{self.schedule.__str__()}"

# A student is a person (this is how we do inheritance)
# A student inherits all members (collectively state and behavior) of a person
# Person is the superclass for Student.
# Student is a subclass of Person
class Student(Person):
    pass


class Faculty(Person):
    pass






# Testing stuff
c1 = Course("CSC", 130)
c2 = Course("MATH", 240)
print(c1)
print(c2)

s1 = Schedule()
print(s1)
s1.add_course(c1)
s1.add_course(c2)
print(s1)