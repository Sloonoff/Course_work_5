from hh_parser import HeadHunterAPI
from superjob_parser import SuperJobAPI
from file_manager import CSVFileManager, JSONFileManager


def console_manager():
	menu = 'Меню:' \
		   '\n 1 - Вакансий из HH' \
		   '\n 2 - Ваканский из SuperJob'

	print(menu)
	user_enter = int(input('Введите номер необходимой операции\n\t>> '))

	if user_enter == 1:
		api = HeadHunterAPI()
	elif user_enter == 2:
		api = SuperJobAPI()
	else:
		raise ValueError('Недопустимый ввод')

	items = api.get_vacancies('Python')
	vacs = api.convert_vacancies(items)

	menu = 'Собрал вакансии. Выберите следующий шаг:' \
		   '\n 1 - Вывести вакансии без сортировки' \
		   '\n 2 - Отсортировать вакансии по зарплате'
	print(menu)
	user_enter = int(input('Введите номер необходимой операции\n\t>> '))
	vacs.sort(key=lambda vac: vac)

	if user_enter == 1:
		pass
	elif user_enter == 2:
		# api.sort()
		pass
	else:
		raise ValueError('Недопустимый ввод')

	menu = 'Сделано. Выберите следующий шаг:' \
		   '\n 1 - Сохранить вакансии в CSV' \
		   '\n 2 - Сохранить вакансии в JSON'
	print(menu)
	user_enter = int(input('Введите номер необходимой операции\n\t>> '))

	if user_enter == 1:
		fm = CSVFileManager()
	elif user_enter == 2:
		fm = JSONFileManager()
	else:
		raise ValueError('Недопустимый ввод')

	fm.load_to(vacs)

	print(f'Сохранено по пути {fm.path}')


if __name__ == '__main__':
	console_manager()
