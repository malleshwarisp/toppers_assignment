"""
This module calculates the topper among all the students for each subject also it calculates the top three rankers in the class using csv module.
"""
import csv
import sys

class SubjectTopper:
    """
    Create a new Topper object with subject, name, and marks properties.
    """
    def __init__(self, sub='', name='', marks=0):
        self.subject = sub
        self.name = name
        self.marks = marks
    
    def __str__(self):
        return f"Topper in {self.subject} is {self.name}"

class TotalMarks:
    """Create a new TotalMarks object with name and total as properties"""
    def __init__(self, name = '', total=0):
        self.name = name
        self.total = total

    def __str__(self):
        return self.name

def calc_marks(csv_file):
    """
    Parameters:
    csv_file

    Returns:
    Prints topper of each subject in the class
    Prints top three rankers in the class
    """  
    try:
        # Read input csv file contents.
        with open(csv_file, newline='') as file:
            file_contents = csv.reader(file, delimiter=',')
            # Read the first row and store the subjects.
            SUBJECT_NAMES = next(file_contents)[1:]
            # Create SubjectTopper object for each subject and Initialize.
            subjects = [SubjectTopper(sub) for sub in SUBJECT_NAMES]
            first_ranker = TotalMarks()
            second_ranker = TotalMarks()
            third_ranker = TotalMarks()
            
            for row in file_contents:
                total = 0
                for i, sub in enumerate(SUBJECT_NAMES):
                    marks = int(row[i+1])
                    total += marks
                    # Compare marks
                    if marks > subjects[i].marks:
                        subjects[i] = SubjectTopper(sub, row[0], marks)

                # Compare total marks of each student with top three rankers.
                if total < third_ranker.total:
                    continue
                if total > first_ranker.total:
                    third_ranker = second_ranker
                    second_ranker = first_ranker
                    first_ranker = TotalMarks(name=row[0], total=total)
                elif total > second_ranker.total:
                    third_ranker = second_ranker
                    second_ranker = TotalMarks(name=row[0], total=total)
                else:
                    third_ranker =  TotalMarks(name=row[0], total=total)

        # Print the topper in each subject.
        for sub_topper in subjects:
            print(sub_topper)
        # Print the top three students in the class rank wise.
        print(f"Best students in the class are {first_ranker}, {second_ranker} and {third_ranker}")
        
    except (csv.Error, FileNotFoundError, SyntaxError, NameError, ValueError) as exception_error:
        sys.exit(f'exited with error: {exception_error}')
    

if __name__ == '__main__':
    CSV_FILE = "C:\\Users\\malle\\python-tutus\\Student_marks_list.csv"
    calc_marks(CSV_FILE)
