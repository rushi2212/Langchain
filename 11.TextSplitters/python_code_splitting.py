from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

text = """
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0 

    student1 = Student("Alice", 20,8.2)
    student1.add_grade(85)
    student1.add_grade(90)

    if student1.get_average() > 80:
        print(f"{student1.name} is doing well in school.")
    else:
        print(f"{student1.name} needs to improve.")
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language = Language.PYTHON, 
    chunk_size=300, 
    chunk_overlap=0
)

chunks = splitter.split_text(text)
print(chunks[0])
print(len(chunks))
