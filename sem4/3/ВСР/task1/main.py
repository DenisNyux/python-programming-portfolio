class NewRegistration():
    """"Класс, описывающий поля формы регистрации и проверяющий эти поля на валидность"""

    def __init__(self, f_name='Ivan', l_name='Ivanov', email='sobaka@sobaka.ru', city='Saint-P', country='Russia',
                 postal_code='460000'):
        # checkers
        self.__check_names(f_name, l_name, city, country)
        self.__check_email(email)
        self.__check_post(postal_code)
        # setting
        self.__f_name = f_name
        self.__l_name = l_name
        self.__city = city
        self.__country = country
        self.__email = email
        self.__postal_code = postal_code

    def __check_names(self, *args):
        """"
        Проверка названий городов, имен и стран (значение должно быть >3 символов,
        быть строкой и начинаться с большой буквы)
        """
        for each in args:
            if not (type(each) == str and len(each) >= 3 and each[0].isupper()):
                raise ValueError('Invalid name or city. It should be string and longer than 3 symbols ')

    def __check_email(self, m):
        """
        Поверка email (должен быть строкой, а также разделяться знаком @)
        """
        if not (type(m) == str and len(m.split('@')) == 2):
            raise ValueError('Invalid email')

    def __check_post(self, code):
        """"Проверка почтового кода (должен быть цифрой из 6 символов)"""
        if not (code.isdigit() and len(code) == 6):
            raise ValueError('Invalid postal code')

    # f_name prop
    @property
    def f_name(self):
        return self.__f_name

    @f_name.setter
    def f_name(self, new_name):
        self.__check_names(new_name)
        self.__f_name = new_name

    # l_name prop
    @property
    def l_name(self):
        return self.__l_name

    @l_name.setter
    def l_name(self, new_name):
        self.__check_names(new_name)
        self.__l_name = new_name

    # email prop
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_mail):
        self.__check_email(new_mail)
        self.__l_name = new_mail

    # postal prop
    @property
    def postal_code(self):
        return self.__postal_code

    @postal_code.setter
    def postal_code(self, new_code):
        self.__check_post(new_code)
        self.__postal_code = new_code

    # city prop
    @property
    def city(self):
        return self.__city

    @l_name.setter
    def city(self, new_name):
        self.__check_names(new_name)
        self.__city = new_name

    # city prop
    @property
    def country(self):
        return self.__country

    @l_name.setter
    def city(self, new_name):
        self.__check_names(new_name)
        self.__country = new_name


a = NewRegistration()

print(a.f_name, a.l_name, a.email, a.postal_code, a.city, a.country)

# Проверка работы сеттеров
# a.f_name = 'puk'
# a.email = 'sas123'
# a.postal_code = 1455
