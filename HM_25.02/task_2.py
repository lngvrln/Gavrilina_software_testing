class Patient:

    def __init__(self, name, year_birth, is_healthy):
        self.name = name
        self.year_birth = year_birth
        self.is_healthy = is_healthy

    def age_category_define(self):
        if 1946 < self.year_birth < 1980:
            return 'Взрослый'
        if self.year_birth >= 1980:
            return 'Молодой'
        return 'Пожилой'

    def health_status_define(self):
        if self.is_healthy:
            return 'Здоров'
        return 'Болен'

    def show_patient(self):
        return (
            f'{self.name}, '
            f'возраст: {self.age_category_define()}, '
            f'статус: {self.health_status_define()}'
        )

# Создайте экземпляр класса Patient с необходимыми параметрами.
# Например, test_old_unhealthy = Patient('Иванов', 1940, False).

# Тест 1: Пожилой и болен
test_old_unhealthy = Patient('Иванов', 1940, False)
assert test_old_unhealthy.health_status_define() == 'Болен', (
    'Метод health_status_define() некорректно обрабатывает is_healthy=False.'
)
assert test_old_unhealthy.age_category_define() == 'Пожилой', (
    'Метод age_category_define() некорректно обрабатывает год рождения до 1946.'
)

# Напишите assert и в нём проверьте,
# что метод health_status_define() этого экземпляра возвращает строку "Болен".
# Во втором assert проверьте, возвращает ли метод age_category_define() значение "Пожилой".

# Тест 2: Взрослый и здоров
test_adult_healthy = Patient('Петров', 1950, True)
assert test_adult_healthy.health_status_define() == 'Здоров', (
    'Метод health_status_define() некорректно обрабатывает is_healthy=True.'
)
assert test_adult_healthy.age_category_define() == 'Взрослый', (
    'Метод age_category_define() некорректно обрабатывает год рождения между 1946 и 1980.'
)

# Создайте новый экземпляр с другими параметрами;
# через assert проверьте, вернут ли и его методы ожидаемый результат.

# Создайте столько экземпляров, сколько нужно,
# чтобы через разные assert проверить все методы во всех вариантах.

# Тест 3: Молодой и болен
test_young_unhealthy = Patient('Сидоров', 1990, False)
assert test_young_unhealthy.health_status_define() == 'Болен', (
    'Метод health_status_define() некорректно обрабатывает is_healthy=False.'
)
assert test_young_unhealthy.age_category_define() == 'Молодой', (
    'Метод age_category_define() некорректно обрабатывает год рождения после 1980.'
)

# Тест 4: Пожилой и здоров
test_old_healthy = Patient('Кузнецов', 1945, True)
assert test_old_healthy.health_status_define() == 'Здоров', (
    'Метод health_status_define() некорректно обрабатывает is_healthy=True.'
)
assert test_old_healthy.age_category_define() == 'Пожилой', (
    'Метод age_category_define() некорректно обрабатывает год рождения до 1946.'
)

# Тест 5: Взрослый и болен
test_adult_unhealthy = Patient('Смирнов', 1970, False)
assert test_adult_unhealthy.health_status_define() == 'Болен', (
    'Метод health_status_define() некорректно обрабатывает is_healthy=False.'
)
assert test_adult_unhealthy.age_category_define() == 'Взрослый', (
    'Метод age_category_define() некорректно обрабатывает год рождения между 1946 и 1980.'
)

# Тест 6: Молодой и здоров
test_young_healthy = Patient('Васильев', 2000, True)
assert test_young_healthy.health_status_define() == 'Здоров', (
    'Метод health_status_define() некорректно обрабатывает is_healthy=True.'
)
assert test_young_healthy.age_category_define() == 'Молодой', (
    'Метод age_category_define() некорректно обрабатывает год рождения после 1980.'
)

print("Done.")