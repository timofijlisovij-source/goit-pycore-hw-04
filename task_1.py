def total_salary  (path: str) -> tuple[float, float]:
    sum_salary = 0
    n = 0
    #n is the amount of workers for calculation of the average
    try:
        with open (path, "r", encoding= "utf-8") as salary_raw:
            for line in salary_raw :
                name, salary = line.strip().split(",")
                sum_salary += float(salary)
                n += 1
            if n>0:
                average_salary = sum_salary/n
            else:
                average_salary = 0
                print("The file os empty")
        return sum_salary, average_salary        
    except FileNotFoundError:
        print("File not found")
        return 0, 0
    except ValueError:
        print("Incorrect data format in the file")
        return 0, 0

total, average = total_salary(r"C:\games\New Text Document.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


