# both letter grades  and grade points:

def pointsletter():
    marks = {
        (90, 100): 'A+',
        (80, 90): 'A',
        (70, 80): 'B+',
        (60, 70): 'B',
        (50, 60): 'C',
        (40, 50): 'D',
        (0, 40): 'F'
    }

    try:
        points = int(input('Enter the points: '))
        for grade_range, grade in marks.items():
            if grade_range[0] <= points <= grade_range[1]:
                print("Letter Grade:", grade)
                break
    except ValueError:
        grade = input('Enter the grade: ') .lower()
        for grade_range, g in marks.items():
            if grade == g.lower():
                print("Points:", grade_range[0], "-", grade_range[1])
                break
    except:
        print("Invalid input.")

pointsletter()


    

