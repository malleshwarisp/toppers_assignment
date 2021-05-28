"""
This module calculates the topper among all the students for each subject also it calculates the top three rankers in the class using csv module.
"""
import csv
import sys

class SubjectTopper:
    """
    Create a new Topper object with subject, name, and marks attributes.
    """
    def __init__(self, sub, name='', marks=0):
        self.subject = sub
        self.name = name
        self.marks = marks

    def __str__(self):
        return f'Topper in {self.subject} is {self.name}'

SUBJECT_NAMES = ['Maths', 'Biology', 'English', 'Physics', 'Chemistry', 'Hindi']

def calc_marks(csv_file):
    """
    Summary or description of the function

    Parameters:
    csv_file

    Returns:
    Prints topper of each subject in the class
    Prints top three rankers in the class
    """  
    # Create SubjectTopper object for each subject and Initialize.
    subjects = [SubjectTopper(sub) for sub in SUBJECT_NAMES]

    first_ranker = SubjectTopper('total')
    second_ranker = SubjectTopper('total')
    third_ranker = SubjectTopper('total')
    try:
        # Read input csv file contents.
        with open(csv_file, newline='') as file:
            file_contents = csv.DictReader(file, delimiter=',')
            for row in file_contents:
                total = 0
                for i, sub in enumerate(SUBJECT_NAMES):
                    marks = int(row[sub])
                    total += marks
                    # Compare marks
                    if marks > subjects[i].marks:
                        subjects[i] = SubjectTopper(sub, row['Name'], marks)

                # Compare total marks of each student with top three rankers.
                if total < third_ranker.marks:
                    continue
                if total > first_ranker.marks:
                    third_ranker = second_ranker
                    second_ranker = first_ranker
                    first_ranker = SubjectTopper('total', row['Name'], total)
                elif total > second_ranker.marks:
                    third_ranker = second_ranker
                    second_ranker = SubjectTopper('total', row['Name'], total)
                else:
                    third_ranker =  SubjectTopper('total', row['Name'], total)

        # Print the topper in each subject.
        for sub_topper in subjects:
            print(sub_topper)
        # Print the top three students in the class rank wise.
        print(f'''Best students in the class are {first_ranker.name}, {second_ranker.name} and {third_ranker.name}''')

    except (csv.Error, FileNotFoundError, SyntaxError, NameError, ValueError) as exception_error:
        sys.exit(f'exited with error: {exception_error}')


if __name__ == '__main__':
    CSV_FILE = "C:\\Users\\malle\\python-tutus\\Student_marks_list.csv"
    calc_marks(CSV_FILE)
