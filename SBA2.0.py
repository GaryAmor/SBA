import statistics

def calculateMarks(answerKey, studentAnswers):
    marks = []
    for student in studentAnswers:
        mark = 0
        for i in range(len(answerKey)):
            if answerKey[i] == student[1][i]:
                mark += 1
        marks.append([student[0], mark])
    return marks

def passingPercentage(marks, passingMark):
    passed = 0
    for student in marks:
        if student[1] >= passingMark:
            passed += 1
    return (passed / len(marks)) * 100

def markStatistics(marks):
    mark_values = []
    for student in marks:
        mark_values.append(student[1])
    
    avg = sum(mark_values) / len(mark_values) # average mark
    maxMark = max(mark_values) # highest
    minMark = min(mark_values) # lowest
    stdDev = statistics.stdev(mark_values) # S.D.
    
    return avg, maxMark, minMark, stdDev

def questionCorrectness(answerKey, studentAnswers):
    totalStudents = len(studentAnswers)
    correctness = [0] * len(answerKey)
    
    for student in studentAnswers:
        for i in range(len(answerKey)):
            if answerKey[i] == student[1][i]:
                correctness[i] += 1
    
    for i in range(len(correctness)):
        correctness[i] = (correctness[i] / totalStudents) * 100
    
    return correctness

def lowCorrectnessQuestions(correctness, threshold=50):
    lowCorrect = []
    for i in range(len(correctness)):
        if correctness[i] < threshold:
            lowCorrect.append(i + 1)
    return lowCorrect

def lowest_marks_student(marks): # lowest :(
    lowest_student = marks[0]
    for student in marks:
        if student[1] < lowest_student[1]:
            lowest_student = student
    return lowest_student

def highest_marks_student(marks): # highest good student :)
    highest_student = marks[0]
    for student in marks:
        if student[1] > highest_student[1]:
            highest_student = student
    return highest_student

def generateReport(marks, avg, maxMark, minMark, stdDev, correctness, lowCorrectness, lowest_student, highest_student):
    report = "MCMAS Analysis Report\n"
    report += "=====================\n\n"
    
    report += "Mark List:\n"
    for student in marks:
        report += f"{student[0]}: {student[1]}\n"
    report += "\n"
    
    report += f"Passing Percentage: {passingPercentage(marks, 15):.2f}%\n"
    report += f"Average Mark: {avg:.2f}\n"
    report += f"Maximum Mark: {maxMark}\n"
    report += f"Minimum Mark: {minMark}\n"
    report += f"Standard Deviation: {stdDev:.2f}\n\n"
    
    report += "Question Correctness:\n"
    for i in range(len(correctness)):
        report += f"Question {i + 1}: {correctness[i]:.2f}%\n"
    report += "\n"
    
    report += "Questions with Low Correctness (<50%):\n"
    for q in lowCorrectness:
        report += str(q) + ", "
    report += "\n\n"
    
    report += f"Lowest Mark Student: {lowest_student[0]} with mark {lowest_student[1]}\n"
    report += f"Highest Mark Student: {highest_student[0]} with mark {highest_student[1]}\n"
    
    return report

def main():
    # ans
    answerFilename = "sample_answer.txt"
    file = open(answerFilename, 'r')
    answerKey = file.read().strip()
    file.close()
    # student ans
    stuAnswerFilename = "sample_student.txt"
    file = open(stuAnswerFilename, 'r')
    studentAnswers = []
    for line in file:
        studentAnswers.append(line.strip().split(','))
    file.close()
    # 计算part
    marks = calculateMarks(answerKey, studentAnswers)
   
    avg, maxMark, minMark, stdDev = markStatistics(marks)

    correctness = questionCorrectness(answerKey, studentAnswers)

    lowCorrectness = lowCorrectnessQuestions(correctness)

    lowest_student = lowest_marks_student(marks)
    
    highest_student = highest_marks_student(marks)
    
    # generate the report
    report = generateReport(marks, avg, maxMark, minMark, stdDev, correctness, lowCorrectness, lowest_student, highest_student)
    
    file = open('report.txt', 'w')
    file.write(report)
    file.close()
    
    print("Report generated in 'report.txt'")

if __name__ == "__main__":
    main()
