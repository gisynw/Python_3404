def scores():
    student = [['John',83.],['Katty',65.],['Tommy',85.]]

   
    while True:
        try:
            options = int(input("""Please input an option:
                                1: print list,
                                2: append list,
                                3: quit
                                """))
            if options == 1:
                print(student)
            elif options == 2:
                student_name = input("Please input student's name  ")
                student_grade = int(input("Please input students' grade  "))
                student.append([student_name, student_grade])
            elif options == 3:
                break
        except ValueError:
            print('Pleae input a number to select the option  ')
            continue
    
if __name__ == "__main__":
    scores()
    