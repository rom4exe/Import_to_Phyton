from datetime import date

from colorama import Fore

from application.db.people import get_employees
from application.salary import calculate_salary

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    cur_date = str(date.today())
    print(Fore.GREEN + cur_date)








