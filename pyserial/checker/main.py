from _csv import reader
import os

DATASET_FILE_DIRECTORY = "C:/Users/jvgcalites/Documents/GitHub/Testing/pyserial/checker/e01/"

def load_csv(filename, name_of_student):
    dataset = list()
    student = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
        student.append(name_of_student.replace(".txt", ""))
        student.append(dataset)
    return student


def get_all_files():
    student_list = list()
    student = list()
    entries = os.listdir(DATASET_FILE_DIRECTORY)
    for entry in entries:
        student = load_csv(DATASET_FILE_DIRECTORY + entry, entry)
        student_list.append(student)
    return student_list


def checker(students_answers, solution):
    scores = list()
    for student in students_answers: # student[0] = ['Antaran', [ [0,1,01], [0,1,01] ] ]
        for paper in student: # paper[1] =  [0,1,01]
            points = 0
            stud_name = paper[0]
            for answers in paper[1]:
                for rows in answers:
                    for columns in range(10):
                        if rows[columns] == solution[rows, columns]:
                            points += 1
            scores.append(stud_name)
            scores.append(points)
        scores_list =
    return scores


def write_scores(scores):
    f = open("scores.txt", "a+")
    for score in scores:
        f.write("%s" % score)
    f.close()


if __name__ == '__main__':
#    e01 = load_csv("e01.txt")
    e01 = get_all_files()
    print(e01)
    solution = [['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '00'],
                ['0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '00'],
                ['0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '00'],
                ['0', '0', '0', '0', '0', '0', '1', '0', '1', '0', '00'],
                ['1', '0', '0', '0', '0', '1', '1', '0', '1', '0', '00'],
                ['1', '0', '0', '1', '1', '1', '1', '0', '1', '0', '00'],
                ['1', '0', '0', '1', '1', '1', '1', '0', '0', '1', '00'],
                ['1', '0', '0', '1', '1', '1', '1', '0', '0', '1', '10'],
                ['1', '0', '0', '1', '1', '1', '1', '0', '0', '1', '10'],
                ['1', '0', '0', '1', '1', '1', '1', '1', '0', '1', '10'],
                ['1', '1', '0', '1', '1', '1', '1', '1', '0', '1', '10'],
                ['1', '1', '0', '1', '1', '1', '1', '0', '0', '1', '10']]
    print(solution)
    scores = checker(e01, solution)
    write_scores(scores)


# read the file and store it in a 2d array
# initialize the solution array
# loop in all contents of 2d array
# loop in all contents of the user array
# check if user is correct
# store the name and the score in an array list
# write the array that contains the name and the score in a text file.
# for answer in student:
#     print(str(student.index(answer)) + ". " + answer + " " + solution[student.index(answer)])
#     if answer == solution[student.index(answer)]:
#         points += 1