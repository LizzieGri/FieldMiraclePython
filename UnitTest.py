import FieldMiracle
import unittest


class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(FieldMiracle.write_question("Самая длинная река в мире", "амазонка"), "Самая длинная река в мире;амазонка")

    # def test_many_quit(self):
    #     self.assertEqual(FieldMiracle.write_question(2), None)

    # def test_get(self):
    #     self.assertEqual(FieldMiracle.get_question(), ('амазонка', 'Самая длинная река в мире'))

    # def test_encryption(self):
    #     self.assertEqual(FieldMiracle.output_question(),'********')

    # def test_answ(self):
    #     self.assertEqual(FieldMiracle.answ('а'), 'а*а****а')

    def test_win(self):
        self.assertEqual(FieldMiracle.answ('амазонка'), 'Вы правильно угадали слово!')



if __name__ == '__main__':
    unittest.main()
