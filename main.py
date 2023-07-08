from aplication.db.people import get_employees
from aplication.salary import calculate_salary
from datetime import date

def main():
    get_employees()
    calculate_salary()
    print(f'Дата выгрузки: {date.today()}')

if __name__ == '__main__':
    main()