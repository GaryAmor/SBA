max=1000
no_of_student=0
answer=['']
sid=['']*max
responese=['']*max




f=open("sampledata1.txt","r")
content=f.readline()
while len(content)>0:
   print(content)
   content=f.readline()
   
correct_answers = ""
student_answers = {}

while len(content) > 0:
    content = content.strip()
    if content.startswith("ANSWER:"):
        correct_answers = content.split(":")[1]
    else:
        student_id, answers = content.split(":")
        student_answers[student_id] = answers
    content = f.readline()

f.close()
