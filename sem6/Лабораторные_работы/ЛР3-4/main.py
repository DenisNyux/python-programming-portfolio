# Программирование (Python)
# 6 семестр, тема 1

# Лабораторная работа 1

"""
Используя обучающий набор данных о пассажирах Титаника, находящийся в проекте (оригинал: https://www.kaggle.com/c/titanic/data), найдите ответы на следующие вопросы: 

1. Какое количество мужчин и женщин ехало на параходе? Приведите два числа через пробел.

2. Подсчитайте сколько пассажиров загрузилось на борт в различных портах? Приведите три числа через пробел.

3. Посчитайте долю (процент) погибших на параходе (число и процент)?

4. Какие доли составляли пассажиры первого, второго, третьего класса?

5. Вычислите коэффициент корреляции Пирсона между количеством супругов (SibSp) и количеством детей (Parch).

6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
1) возрастом и параметром survival;
2) полом человека и параметром survival;
3) классом, в котором пассажир ехал, и параметром survival.

7. Посчитайте средний возраст пассажиров и медиану.
8. Посчитайте среднюю цену за билет и медиану.

9. Какое самое популярное мужское имя на корабле?
10. Какие самые популярные мужское и женские имена людей, старше 15 лет на корабле?


Для вычисления 3, 4, 5, 6, 7, 8 используйте тип данных float с точностью два знака в дробной части. 


"""
import numpy
import pandas  # импортирование библиотеки для считывания данных

# считаем данных из файла, в качестве столбца индексов используем PassengerId
data = pandas.read_csv('train.csv', index_col="PassengerId")
cheloveki = len(data)

# TODO #1
def get_sex_distrib(data):
    """
    1. Какое количество мужчин и женщин ехало на параходе? Приведите два числа через пробел.
    """
    n_male, n_female = 0, 0
    res = data['Sex'].value_counts()
    n_male, n_female = res['male'], res['female']
    return n_male, n_female


# TODO #2
def get_port_distrib(data):
    """  
    2. Подсчитайте сколько пассажиров загрузилось на борт в различных портах? Приведите три числа через пробел.
    """

    port_S, port_C, port_Q = 0, 0, 0
    res = data['Embarked'].value_counts()
    port_S, port_C, port_Q = res['S'], res['C'], res['Q']
    return port_S, port_C, port_Q


# TODO #3
def get_surv_percent(data):
    """
    3. Посчитайте долю погибших на параходе (число и процент)?
    """

    n_died, perc_died = 0, 0
    res = data['Survived'].value_counts()
    n_died = res[0]
    perc_died = n_died / (res[0] + res[1]) 
    return n_died, perc_died


# TODO #4
def get_class_distrib(data):
    """
    4. Какие доли составляли пассажиры первого, второго, третьего класса?    
    """
    n_pas_f_cl, n_pas_s_cl, n_pas_t_cl = 0, 0, 0
    res = data['Pclass'].value_counts()
    n_pas_f_cl = res[1] / cheloveki
    n_pas_s_cl = res[2] / cheloveki
    n_pas_t_cl = res[3] / cheloveki
    return n_pas_f_cl, n_pas_s_cl, n_pas_t_cl


# TODO #5
def find_corr_sibsp_parch(data):
    """
    5. Вычислите коэффициент корреляции Пирсона между количеством супругов (SibSp) и количеством детей (Parch).
    """
    corr_val = -1
    # print(data['SibSp'], data['Parch'])
    corr_val = numpy.corrcoef(data['SibSp'], data['Parch'])[1,0]
   
    return corr_val


# TODO #6-1
def find_corr_age_survival(data):
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
    
    - возрастом и параметром survival;

    """

    corr_val = -1
    corr_val = data['Age'].corr(data['Survived'])
    return corr_val


# TODO #6-2
def find_corr_sex_survival(data):
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
    
    - полом человека и параметром survival;
    """

    corr_val = -1
    sex = data['Sex']
    for each in sex:
      if (each == 'male'): 
        each = 0 
      else: 
        each = 1
    corr_val = sex.corr(data['Survived'])
    return corr_val


# TODO #6-3
def find_corr_class_survival(data):
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:

    - классом, в котором пассажир ехал, и параметром survival.
    """

    corr_val = -1
    corr_val = data['Pclass'].corr(data['Survived'])
    return corr_val


# TODO #7
def find_pass_mean_median(data):
    """
    7. Посчитайте средний возраст пассажиров и медиану.
    """
    mean_age, median = None, None
    age = data['Age']
    mean_age = age.mean()
    median = age.median()
    return mean_age, median


# TODO #8
def find_ticket_mean_median(data):
    """
    8. Посчитайте среднюю цену за билет и медиану.
    """
    mean_price, median = None, None
    fare = data['Fare']
    mean_price = fare.mean()
    median = fare.median()
    return mean_price, median


# TODO #9
def find_popular_name(data):
    """
    9. Какое самое популярное мужское имя на корабле?
    """

    is_male = data["Sex"] == "male"
    return data[is_male].mode().at[0, "Name"]



# TODO #10
def find_popular_adult_names(data):
    """
    10. Какие самые популярные мужское и женские имена людей, старше 15 лет на корабле?
    """
    is_15_yo = data["Age"] > 15
    is_male = data["Sex"] == "male"
    is_female = data["Sex"] == "female"

    male_name = data[is_15_yo & is_male].mode().at[0, "Name"]
    female_name = data[is_15_yo & is_female].mode().at[0, "Name"]

    return male_name, female_name


# ------------------------------

# Реализуем вычисление количества пассажиров на параходе и опишем предварительные действия с данными (считывание)

# После загрузки данных с помощью метода read_csv и индексации его по первому столбцу данных (PassangerId) становится доступно выборка данных по индексу. 
# С помощью запроса ниже мы можем получить имя сотого пассажира
# print((data.iloc[100]['Name']))
# print(get_sex_distrib(data))
# print(get_port_distrib(data))
# print(get_surv_percent(data))
# print(get_class_distrib(data))
# print(find_corr_sibsp_parch(data))
# print(find_corr_age_survival(data))
# print(find_corr_class_survival(data))
# print(find_pass_mean_median(data))
# print(find_ticket_mean_median(data))
# print(find_ticket_mean_median(data))
# print(find_popular_name(data))
# print(find_popular_adult_names(data))


# print(find_corr_sex_survival(data))

def get_number_of_pass(data_file):
    """
        Подсчет количества пассажиров. 
        data_file - str
        В качестве аргумента удобнее всего использовать строковую переменную, куда будет передаваться название файла (т. к. далее, возможно, потребуется подсчитать параметры для другого набора данных test.csv)
    """
    male_int, female_int = 0, 0
    # считывание и обработка данных
    data = pandas.read_csv(data_file, index_col="PassengerId")

    # считать данных из столбца возможно с помощью метода value_counts()
    res = data['Sex'].value_counts()
    # res будет содержать ассоциативный массив, ключами в котором являются значения столбца sex, а целочисленные значениями - количества пассажиров обоих полов
    male_int, female_int = res['male'], res['female']
    return male_int, female_int


def test_get_number_of_pass():
    assert get_number_of_pass('train.csv') == (577,314), " Количество мужчин и женщин на Титанике"

# аналогично протестировать остальные функции