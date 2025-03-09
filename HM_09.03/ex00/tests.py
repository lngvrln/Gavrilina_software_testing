# tests.py
import unittest

from time import sleep

from services import service_unique_id

class TestUniqueIdService(unittest.TestCase):
    
    '''
    def test_value_is_running_out(self):
        first_value = service_unique_id()
        sleep(1)
        second_value = service_unique_id()
        self.assertNotEqual(first_value, second_value)

    def test_result_is_int(self):
        result = service_unique_id()
        self.assertIsInstance(result, int)
    '''

    def test_unique_id_within_expected_range(self):
        result = service_unique_id()
        self.assertGreaterEqual(result, 0)  # Уникальный идентификатор не должен быть отрицательным

    def test_multiple_unique_ids(self):
        """Проверяет, что несколько вызовов функции возвращают разные значения."""
        unique_ids = {service_unique_id() for _ in range(100)}  # Генерируем 100 уникальных идентификаторов
        self.assertEqual(len(unique_ids), 100)  # Все идентификаторы должны быть уникальными

unittest.main()  # Запуск тестов. 

