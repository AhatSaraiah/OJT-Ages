import unittest
from ages import ages 

class TestAgesFunction(unittest.TestCase):
    # testinf child age group age<12
    def test_child_age_group(self):
        result = ages("sara", 10)
        self.assertEqual(result,"child")
   
    # testinf teenager age group 12<=age<=18 
    def test_teenager_age_group(self):
        result = ages("noor", 15)
        self.assertEqual(result, "teenager")

    # testinf teenager age group age>18 
    def test_adult_age_group(self):
        result = ages("aya", 25)
        self.assertEqual(result, "adult")
   
    # # testing name type 
    # def test_invalid_name_type(self):
    #     with self.assertRaises(TypeError):
    #         ages("tarek", 20)


    # # testing age type 
    # def test_invalid_age_type(self):
    #     with self.assertRaises(TypeError):
    #         ages("lorin", 12)

if __name__ == '__main__':
    unittest.main()