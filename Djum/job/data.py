""" Вакансии """

jobs = [
    {"title": "Разработчик на Python", "cat": "backend", "company": "staffingsmarter", "salary_from": "100000",
     "salary_to": "150000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Разработчик в проект на Django", "cat": "backend", "company": "swiftattack", "salary_from": "80000",
     "salary_to": "90000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Разработчик на Swift в аутсорс компанию", "cat": "backend", "company": "swiftattack",
     "salary_from": "120000", "salary_to": "150000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Мидл программист на Python", "cat": "backend", "company": "workiro", "salary_from": "80000",
     "salary_to": "90000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Питонист в стартап", "cat": "backend", "company": "primalassault", "salary_from": "120000",
     "salary_to": "150000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Разработчик на Python", "cat": "devops", "company": "staffingsmarter", "salary_from": "100000",
     "salary_to": "150000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Разработчик в проект на Django", "cat": "design", "company": "swiftattack", "salary_from": "80000",
     "salary_to": "90000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Разработчик на Swift в аутсорс компанию", "cat": "products", "company": "swiftattack",
     "salary_from": "120000", "salary_to": "150000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Менеджер", "cat": "management", "company": "hirey", "salary_from": "60000",
     "salary_to": "90000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "frontend в стартап", "cat": "frontend", "company": "hirey", "salary_from": "120000",
     "salary_to": "150000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Разработчик JS", "cat": "frontend", "company": "hirey", "salary_from": "100000",
     "salary_to": "150000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Тестеровщик", "cat": "testing", "company": "swiftattack", "salary_from": "80000",
     "salary_to": "90000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Разработчик игр", "cat": "gamedev", "company": "swiftattack",
     "salary_from": "125000", "salary_to": "150000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Мидл программист на Python", "cat": "backend", "company": "swiftattack", "salary_from": "80000",
     "salary_to": "100000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Питонист в стартап", "cat": "backend", "company": "troller", "salary_from": "120000",
     "salary_to": "135000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Разработчик", "cat": "devops", "company": "troller", "salary_from": "100000",
     "salary_to": "155000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Веб-дизайнер", "cat": "design", "company": "troller", "salary_from": "30000",
     "salary_to": "75000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Продуктовед", "cat": "products", "company": "primalassault",
     "salary_from": "125000", "salary_to": "150000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Менеджер", "cat": "management", "company": "primalassault", "salary_from": "40000",
     "salary_to": "70000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Питонист в стартап", "cat": "frontend", "company": "primalassault", "salary_from": "120000",
     "salary_to": "140000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Разработчик на Python", "cat": "backend", "company": "staffingsmarter", "salary_from": "100000",
     "salary_to": "150000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Разработчик в проект на Django", "cat": "backend", "company": "swiftattack", "salary_from": "80000",
     "salary_to": "90000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Разработчик на Swift в аутсорс компанию", "cat": "backend", "company": "evilthreath",
     "salary_from": "120000", "salary_to": "150000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Тестеровщик", "cat": "testing", "company": "evilthreath", "salary_from": "50000",
     "salary_to": "70000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Тестеровщик в стартап", "cat": "testing", "company": "evilthreath", "salary_from": "20000",
     "salary_to": "50000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Разработчик на Python", "cat": "devops", "company": "staffingsmarter", "salary_from": "100000",
     "salary_to": "150000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Разработчик в проект на Django", "cat": "design", "company": "swiftattack", "salary_from": "80000",
     "salary_to": "90000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Разработчик на Swift в аутсорс компанию", "cat": "products", "company": "staffingsmarter",
     "salary_from": "120000", "salary_to": "150000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Менеджер", "cat": "management", "company": "staffingsmarter", "salary_from": "16000",
     "salary_to": "50000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "frontend в стартап", "cat": "frontend", "company": "hirey", "salary_from": "120000",
     "salary_to": "150000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Разработчик JS", "cat": "frontend", "company": "hirey", "salary_from": "100000",
     "salary_to": "150000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Разработчик в проект на Django", "cat": "backend", "company": "swiftattack", "salary_from": "80000",
     "salary_to": "90000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Разработчик игр", "cat": "gamedev", "company": "rebelrage",
     "salary_from": "125000", "salary_to": "150000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Мидл программист на Python", "cat": "backend", "company": "rebelrage", "salary_from": "80000",
     "salary_to": "100000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Питонист в стартап", "cat": "backend", "company": "troller", "salary_from": "120000",
     "salary_to": "135000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Разработчик", "cat": "devops", "company": "troller", "salary_from": "100000",
     "salary_to": "155000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Веб-дизайнер", "cat": "design", "company": "workiro", "salary_from": "80000",
     "salary_to": "95000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Продуктовед", "cat": "products", "company": "workiro",
     "salary_from": "25000", "salary_to": "50000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Менеджер", "cat": "management", "company": "workiro", "salary_from": "80000",
     "salary_to": "70000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Питонист в стартап", "cat": "frontend", "company": "workiro", "salary_from": "120000",
     "salary_to": "140000", "posted": "2020-03-11", "desc": "Потом добавим"},
]

""" Компании """


""" Компании """
companies = [
    {"title": "workiro"},
    {"title": "rebelrage"},
    {"title": "staffingsmarter"},
    {"title": "evilthreath"},
    {"title": "hirey"},
    {"title": "swiftattack"},
    {"title": "troller"},
    {"title": "primalassault"}
]

cities = ['Пермь', 'Санкт-Петербург', 'Екатеринбург', 'Нижний Новгород',
          'Новосибирск', 'Красноярск', 'Казань', 'Москва']


""" Категории """
specialties = [
    {"code": "frontend", "title": "Фронтенд"},
    {"code": "backend", "title": "Бэкенд"},
    {"code": "gamedev", "title": "Геймдев"},
    {"code": "devops", "title": "Девопс"},
    {"code": "design", "title": "Дизайн"},
    {"code": "products", "title": "Продукты"},
    {"code": "management", "title": "Менеджмент"},
    {"code": "testing", "title": "Тестирование"},
]


level = 'Intern', 'Junior', 'Middle', 'Senior', 'Lead',

""" Статусы в формате Enum """

#
#
# class EducationChoices(Enum):
#     missing = 'Отсутствует'
#     secondary = 'Среднее'
#     vocational = 'Средне-специальное'
#     incomplete_higher = 'Неполное высшее'
#     higher = 'Высшее'
#
#
# class GradeChoices(Enum):
#     intern = 'intern'
#     junior = 'junior'
#     middle = 'middle'
#     senior = 'senior'
#     lead = 'lead'
#
#
# class SpecialtyChoices(Enum):
#     frontend = 'Фронтенд'
#     backend = 'Бэкенд'
#     gamedev = 'Геймдев'
#     devops = 'Девопс'
#     design = 'Дизайн'
#     products = 'Продукты'
#     management = 'Менеджмент'
#     testing = 'Тестирование'
#
#
# class WorkStatusChoices(Enum):
#     not_in_search = 'Не ищу работу'
#     consideration = 'Рассматриваю предложения'
#     in_search = 'Ищу работу'


promises = [
    'Оформление по ТК РФ',
    'ДМС со стоматологией',
    'Достойную зарплату, уровень которой можно обсудить по телефону с рекрутером',
    'Гибкое начало дня, отдельные дни удаленной работы обсуждаются',
    'Современный офис',
    'Демократичную корпоративную культуру',
    'Работу в команде по Scrum',
]

waiting = [
    'Написание бизнес-логики по ТЗ от аналитиков',
    'Вынесение общий логики в базовые сервисы',
    'Интеграция с внешними системами, рефкторинг.',
    'Верстка',
    'коддинг',
    'хрен угадаешь',
]

serching = [
    'Опытного разработчика на C# (от 3х лет)',
    'Опытного разработчика на C++ (от 2х лет)',
    'Опытного разработчика на C (от 5и лет)',
    'стажора на JS (без опыта)',
    'Опытного разработчика на Python (от 4х лет)',
    'Опытного разработчика на Java (от 3х лет)',
    'Хорошие знания: ASP.Net MVC, EF CodeFirst, MS SQL, AutoFac (или другой IoC), RabbitMq',
    'Навыки проектирования и рефакторинга доменной модели',
    'git, gitflow, bitBucket, youTrack (или альтернативы)',
]

skillist = ['Python', 'Django', 'Flask', 'PHP', 'JS', 'Node', 'Vue', 'React', 'Git', 'SQL', 'CSS', 'HTML',
            'Ruby', 'Rails', 'Laravel', 'Spring', 'Angular', 'Ember', 'правапессанее', 'и чтоб человек хороший',
            'C++', 'C#', 'C', 'Java', 'Kotlin', 'Pandas', 'Numpy', 'MySQL', 'Symfony', 'CodeIgniter', 'Yii 2',
            'Phalcon', 'Swift', 'ML', 'Паринг', 'BS4',
            'Grails', 'Vaadin', 'Spark', 'Bootstrap', 'Poco', 'Asio C++', 'WebSocket++',]