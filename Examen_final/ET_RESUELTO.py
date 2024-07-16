import csv
import random

salary_b = 800000
salary_a = 2000000
health_discount = 0.07
afp_discount = 0.12
workers = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
salaries = []


def random_salary(list = []):
    for worker in list:
        salary = random.randrange(300000,2500000,200000)
        print("Creando salario alaeatorio de", salary, "para el trabajador", worker)
        while len(worker) < 20:
            worker += " "
        salaries.append([worker, salary])

def salary_class(list=[]):
    salary_class_1 = []
    salary_class_2 = []
    salary_class_3 = []
    for salary in list:
        if salary[1] < salary_b:
            salary_class_3.append(salary)
        elif salary_b < salary[1] < salary_a:
            salary_class_2.append(salary)
        else: 
            salary_class_1.append(salary)

    print("Sueldos menores a", f"{salary_b:,}", "TOTAL:", len(salary_class_3))
    print("Nombre empleado", "\t", "Sueldo \n")
    for salary in salary_class_3:
        print(salary[0], "\t", "$" + str(salary[1]))
    print("\n")

    print("Sueldos entre", f"{salary_b:,}", "y", f"{salary_a:,}", "TOTAL:", len(salary_class_2))
    print("Nombre empleado", "\t", "Sueldo \n")
    for salary in salary_class_2:
        print(salary[0], "\t", "$" +str(salary[1]))
    print("\n")

    print("Sueldos superiores a", f"{salary_a:,}", "TOTAL:", len(salary_class_1))
    print("Nombre empleado","\t", "Sueldo \n")
    for salary in salary_class_1:
        print(salary[0], "\t", "$" + str(salary[1]))
    print("\n")

def statistics(list=[]):
    lower_salary = salary_a
    higher_salary = 0
    salary_sum = 0
    for salary in list:
        if salary[1] > higher_salary:
            higher_salary = salary[1]
        if salary[1] < lower_salary:
            lower_salary = salary[1]
        salary_sum += salary[1]
    mean = salary_sum / len(list)
    print("El sueldo más alto es de : $",higher_salary)
    print("El sueldo más bajo es de: $",lower_salary)
    print("El promedio de los sueldos es de: $",mean)
    print("\n")

def salary_report(list = []):
    header = ["Nombre empleado", "Sueldo base", "Descuento salud", "Descuanto AFP", "Sueldo líquido"]
    print(header[0], "\t",header[1], "\t",header[2], "\t",header[3], "\t",header[4])
    for salary in list:
        salary.append(int(salary[1] * health_discount))
        salary.append(int(salary[1] * afp_discount))
        salary.append(int(salary[1] * (1 - health_discount - afp_discount)))
        print(salary[0], "\t",salary[1], "\t\t",salary[2], "\t\t",salary[3], "\t\t",salary[4])
    list.insert(0, header)
    with open('liquidaciones.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(list)



while True:
    option = input("""
    ¿Qué desea hacer?
    1) Asignar sueldos aleatorios
    2) Clasificar sueldos
    3) Ver estadísticas
    4) Reporte de sueldos
    5) Salir del programa
    """)
    if option == "5":
        print("Finalizando programa ... \nDesarrollado por Óscar Badilla \n66.666.666-6")
        break
    elif option == "1":
        random_salary(workers)
    elif option == "2":
        salary_class(salaries)
    elif option == "3":
        statistics(salaries)
    elif option == "4":
        salary_report(salaries)
    else:
        print("Elija una opción válida. ")