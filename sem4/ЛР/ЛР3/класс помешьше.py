class NewRegistration():
    
    def __init__(self, f_name='Ivan', l_name='Ivanov', email='sobaka@sobaka.ru', city='Saint-P', country='Russia', postal_code='460000'):
        self.__check_names(f_name, l_name)
        self.__check_email(email)
        self.__check_post(postal_code)

    
    def __check_names(self, f, l):
        if type(f) == str and type(l) == str and len(f) >= 3 and len(l) >= 3:
            self.f_name = f
            self.l_name = l
        else:
            raise ValueError('Name should be string and longer than 3 symbols ')  

    def __check_email(self, m):
        if type(m) == str and len(m.split('@')) == 2:
            self.email = m
        else:
            raise ValueError('Invalid email')

    def __check_post(self, code):
        if code.isdigit and len(code) == 6:
            self.postal_code = code
        else:
            raise ValueError('Invalid postal code')
    
    


a = NewRegistration()

print(a.f_name, a.l_name, a.email, a.postal_code) 