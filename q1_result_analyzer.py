
def analyze_result(name, roll_no, marks):
    
    print(f"Student:{name} (Roll: {roll_no})")

    total = sum(marks)
    average = total / 5

    print(f"Total: {total}, Average: {average}")

    if average >= 90:
        print("Grade A")
    elif average >= 75:
        print("Grade B")
    elif average >= 60:
        print("Grade C")
    elif average>=40:
        print("Grade D")
    else:
        print("Fail")

    print("Subjects below 40:",end=" ")
    for i in range(len(marks)):
        if marks[i]<40.0:
            print(f"Subject {i+1}")
  

name = "Aarav" 
roll_no = 101
marks = [88.5, 35.0, 76.0, 92.5, 48.0]

analyze_result(name, roll_no, marks)