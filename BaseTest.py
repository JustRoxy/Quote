import unittest
from BookBase import mainFunc 

class Testing(unittest.TestCase):
	def isIn(self):
		self.assertIn('Война', mainFunc('Наступило молчание. Графиня глядела на гостью, приятно улыбаясь, впрочем, не скрывая того')[0])
		self.assertIn('Толстой', mainFunc('Наступило молчание. Графиня глядела на гостью, приятно улыбаясь, впрочем, не скрывая того')[1])

if __name__ == '__main__':
    unittest.main()