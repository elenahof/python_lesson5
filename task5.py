def summa():
    try:
        with open('tsk5.txt', 'w+') as my_file:
            line = input("Enter the numbers separated by space:\n")
            my_file.writelines(line)
            num_str = line.split()
            print(sum(map(int, num_str)))
    except IOError:
        print("Error in the file!")
    except ValueError:
        print("Error in entering format!")
summa()