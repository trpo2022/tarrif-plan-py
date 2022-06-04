import unittest
import json
import review.review as r

class TestReviewInput(unittest.TestCase):
    def setUp(self):
        self.data = ''
        with open("questions.json") as json_file:
            self.data = json.load(json_file)
        self.review = r.Review(data)
    
    def test_input1(self):
        self.assertEqual(self.review.try_input(0, 1, 5), False)

    def test_input2(self):
        self.assertEqual(self.review.try_input(6, 1, 5), False)

    def test_input3(self):
        self.assertEqual(self.review.try_input('asd', 1, 5), False)

    def test_input4(self):
        self.assertEqual(self.review.try_input(3, 1, 5), True)
    

if __name__ == "__main__":
    unittest.main()