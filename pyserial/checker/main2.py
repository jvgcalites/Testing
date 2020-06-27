from _csv import reader

def load_csv(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset


def checker(students_answers, solution):
    scores = list()
    score_list = list()
    for answer in students_answers:
        points = 0
        for i in range(1, len(answer)):
            if answer[i] == solution[i-1]:
                points += 1
        scores.append(answer[0])
        scores.append(points)
        print(answer[0] + "," + str(points))
        score_list.append(scores)
        scores = []

    return score_list


def write_scores(scores):
    f = open("scores.txt", "a+")
    for score in scores:
        f.write("%s,%s/132\n" % (score[0], score[1]))
    f.close()


if __name__ == '__main__':
    e01 = load_csv("e01.txt")
    solution = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '00',
                '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '00',
                '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '00',
                '0', '0', '0', '0', '0', '0', '1', '0', '1', '0', '00',
                '1', '0', '0', '0', '0', '1', '1', '0', '1', '0', '00',
                '1', '0', '0', '1', '1', '1', '1', '0', '1', '0', '00',
                '1', '0', '0', '1', '1', '1', '1', '0', '0', '1', '00',
                '1', '0', '0', '1', '1', '1', '1', '0', '0', '1', '10',
                '1', '0', '0', '1', '1', '1', '1', '0', '0', '1', '10',
                '1', '0', '0', '1', '1', '1', '1', '1', '0', '1', '10',
                '1', '1', '0', '1', '1', '1', '1', '1', '0', '1', '10',
                '1', '1', '0', '1', '1', '1', '1', '0', '0', '1', '10']
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