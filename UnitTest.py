import FieldMiracle
import unittest


class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(FieldMiracle.write_question("Самая длинная река в мире", "амазонка"), "Самая длинная река в мире;амазонка")

    def test_many_quit(self):
        self.assertEqual(FieldMiracle.write_question(2), None)


if __name__ == '__main__':
    unittest.main()
