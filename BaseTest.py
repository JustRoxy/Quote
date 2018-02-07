import unittest
from BookBase import mainFunc 

class Testing(unittest.TestCase):
    def isIn(self):
        self.name = 'Война'
        self.text = 'Наступило молчание. Графиня глядела на гостью, приятно улыбаясь, впрочем, не скрывая того'
        self.author = 'Толстой'
        self.assertIn(name, mainFunc(text)[0])
        self.assertIn(author, mainFunc(text)[1])

if __name__ == '__main__':
    unittest.main()


##raw = "Наступило молчание. Графиня глядела на гостью, приятно улыбаясь, впрочем, не скрывая того,"
##raw = "Horatio says 'tis but our fantasy, And will not let belief take hold of him"
##raw = "Он стал уединяться и избегать людей. Служба и раньше была ему противна, теперь же она стала для него невыносима. Он боялся,"
##raw = "To be sure we have harvested: but why have all our fruits become rotten and brown? What was it fell last night from the evil moon?"
##raw = "Святой стал смеяться над Заратустрой и так говорил: «Тогда постарайся, чтобы они приня-ли твои сокровища! Они недоверчивы к отшельникам и не верят, что мы приходим, чтобы да-рить."
