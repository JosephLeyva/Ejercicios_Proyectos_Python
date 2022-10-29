class Student:
    def __init__(self, name, list_of_marks=[]) -> None:
        self.name = name
        self.marks = list_of_marks

    def get_number_of_marks(self):
        return len(self.marks)

    def get_total_sum_of_marks(self):
        return sum(self.marks)

    def determine_maximum_mark(self):
        return max(self.marks)

    def determine_minimum_mark(self):
        return min(self.marks)

    def determine_average(self):
        return self.get_total_sum_of_marks() / self.get_number_of_marks()

    def add_new_mark(self, new_mark):
        self.marks.append(new_mark)

    def remove_mark_at_index(self, index):
        # self.marks.pop(index)
        del self.marks[index]


student = Student("Joseph", [23, 45, 56, 75])
number = student.get_number_of_marks()
sum_ = student.get_total_sum_of_marks()
maximum_mark = student.determine_maximum_mark()
minimumm_mark = student.determine_minimum_mark()
average = student.determine_average()
student.add_new_mark(35)
student.remove_mark_at_index(2)

print(student.marks)
