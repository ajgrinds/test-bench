import datetime

arr = [1,2,3,4,5,6,7,8,9,10] * 122

start_time = datetime.datetime.now()
filt = filter(lambda x: x % 2, arr)
second_time = datetime.datetime.now()
[x for x in arr if x % 2][0]
third_time = datetime.datetime.now()
list(filter(lambda x: x % 2, arr))[0]
fourth_time = datetime.datetime.now()

print(len(arr))
print(f"Filter time: {second_time - start_time}")
print(f"List comprehension time: {third_time - second_time}")
print(f"Filter and convert time: {fourth_time - third_time}")
print(next(filt))
print(next(filt))
print(next(filt))


class Student:
    def __init__(self, student_ID, scores):
        self.__ID = student_ID
        self.__scores = scores
        self.average = self.get_average_scores()

    def __str__(self):
        output = ''
        output += f'Student ID: {self.__ID}'
        output += f'Student Grades: {self.__scores}'
        output += f'Final Grade: {self.average + self.get_final_grade()}'
        return output

    def get_ID(self):
        return self.__ID

    def get_scores(self):
        return self.__scores

    def get_average_scores(self):
        total = sum(self.__scores)
        self.average = total / 5
        return self.average

    def get_final_grade(self):
        if self.average < 60:
            return ('F')
        elif self.average < 70:
            return ('D')
        elif self.average == 70 or self.average < 80:
            return ('C')
        elif self.average == 80 or self.average < 90:
            return ('B')
        elif self.average == 90 or self.average <= 100:
            return ('A')


def main():
    print('Student Information')
    Student_info = Student(14587, [85, 98, 100, 45, 88])
    print(Student_info, end='\n\n')


main()