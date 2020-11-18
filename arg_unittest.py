import unittest
from argumentation import *






"""-------------------TESTING OF THE HELPER FUNCTIONS IN THE ARGUMENTATION MODULE--------------------"""

""" testing function get_best_args(self, prop): """

class BestArgsTest(unittest.TestCase):

    def testBestArgs1(self):
        case = argumentation()
        dialogTable = case.main(file_path="./examples/murder.txt", propToProve=PropLiteral("murder"))
        arg = case.get_best_args(PropLiteral("murder"))[0]
        self.assertEqual(arg.get_id(),'arg1')
        
    def testBestArgs2(self):
        case = argumentation()
        dialogTable = case.main(file_path="./examples/human_traffic.txt", propToProve=PropLiteral("human_trafficking"))
        arg = case.get_best_args(PropLiteral("transport_exploit_person").negate())[0]
        self.assertEqual(arg.get_id(),'arg3')
        
        
    def testBestArgs3(self):
        case = argumentation()
        dialogTable = case.main(file_path="./examples/accident.txt", propToProve=PropLiteral("accident_fault"))
        arg = case.get_best_args(PropLiteral("caused_it"))[0]
        self.assertEqual(arg.get_id(),'arg2')
    
    def testBestArgs4(self):
        case = argumentation()
        dialogTable = case.main(file_path="./examples/photography.txt", propToProve=PropLiteral("inappropriate_photography"))
        arg = case.get_best_args(PropLiteral("public_property"))[0]
        self.assertEqual(arg.get_id(),'arg6')

""" testing function get_props_to_counter(self, args): """

class GetPropsTest(unittest.TestCase):

    def testGetProp1(self):
        case = argumentation()
        case.loadCase(file_path="./examples/photography.txt", propToProve=PropLiteral("inappropriate_photography"))
        reader = Reader()
        caes_data = open('examples/photography.txt')
        (argset, caes) = reader.load(caes_data)
        args = argset.get_arguments(PropLiteral("public_property"))
        propSet = set(case.get_props_to_counter(args))
        propsToCounter = [PropLiteral("public_property").negate(), PropLiteral("public_ownership").negate(), PropLiteral("state_ownership").negate(), PropLiteral("governament_ownership").negate()]
        for prop in propsToCounter:
            with self.subTest(i=str(prop)):
                self.assertTrue(prop in propSet)
                
                
                
    def testGetProp2(self):
       case = argumentation()
       case.loadCase(file_path="./examples/accident.txt", propToProve=PropLiteral("accident_fault"))
       reader = Reader()
       caes_data = open('examples/accident.txt')
       (argset, caes) = reader.load(caes_data)
       args = argset.get_arguments(PropLiteral("caused_it"))
       propSet = set(case.get_props_to_counter(args))
       propsToCounter = [PropLiteral("caused_it").negate(), PropLiteral("witness1").negate(), PropLiteral("unreliable1")]
       for prop in propsToCounter:
           with self.subTest(i=str(prop)):
               self.assertTrue(prop in propSet)
               
                
                
    def testGetProp3(self):
      case = argumentation()
      case.loadCase(file_path="./examples/murder.txt", propToProve=PropLiteral("murder"))
      reader = Reader()
      caes_data = open('examples/murder.txt')
      (argset, caes) = reader.load(caes_data)
      args = argset.get_arguments(PropLiteral("187_excluded"))
      propSet = set(case.get_props_to_counter(args))
      propsToCounter = [PropLiteral("187_excluded").negate(), PropLiteral("self_defence").negate(), PropLiteral("197_excluded")]
      for prop in propsToCounter:
          with self.subTest(i=str(prop)):
              self.assertTrue(prop in propSet)
               
    def testGetProp4(self):
      case = argumentation()
      case.loadCase(file_path="./examples/human_traffic.txt", propToProve=PropLiteral("human_trafficking"))
      reader = Reader()
      caes_data = open('examples/human_traffic.txt')
      (argset, caes) = reader.load(caes_data)
      args = argset.get_arguments(PropLiteral("transport_exploit_person"))
      propSet = set(case.get_props_to_counter(args))
      propsToCounter = [PropLiteral("transport_exploit_person").negate(), PropLiteral("intent_of_exploit").negate(), PropLiteral("knowledge_of_exploit").negate()]
      for prop in propsToCounter:
          with self.subTest(i=str(prop)):
              self.assertTrue(prop in propSet)
                
                
""" testing function structure_strategy(self, props, args): """

class StrategyTest(unittest.TestCase):

    def testStrategy1(self):
        case = argumentation()
        case.loadCase(file_path="./examples/human_traffic2.txt", propToProve=PropLiteral("human_trafficking"))
        reader = Reader()
        caes_data = open('examples/human_traffic2.txt')
        (argset, caes) = reader.load(caes_data)
        strategy = case.structure_strategy(argset.propset(), list())
        self.assertEqual([strategy[0][0], strategy[0][1][0].get_id()],[PropLiteral("not_uk_citizen"), "arg5" ])


    def testStrategy2(self):
        case = argumentation()
        case.loadCase(file_path="./examples/murder.txt", propToProve=PropLiteral("murder"))
        reader = Reader()
        caes_data = open('examples/murder.txt')
        (argset, caes) = reader.load(caes_data)
        strategy = case.structure_strategy(argset.propset(), list())
        self.assertEqual([strategy[0][0], strategy[0][1][0].get_id()],[PropLiteral("murder"), "arg1" ])

        
    def testStrategy3(self):
        case = argumentation()
        case.loadCase(file_path="./examples/accident.txt", propToProve=PropLiteral("accident_fault"))
        reader = Reader()
        caes_data = open('examples/accident.txt')
        (argset, caes) = reader.load(caes_data)
        strategy = case.structure_strategy(argset.propset(), list())
        self.assertEqual([strategy[0][0], strategy[0][1][0].get_id()],[PropLiteral("caused_it").negate(), "arg6" ])
        
 
    def testStrategy4(self):
        case = argumentation()
        case.loadCase(file_path="./examples/syntaxEx.txt", propToProve=PropLiteral("murder"))
        reader = Reader()
        caes_data = open('examples/syntaxEx.txt')
        (argset, caes) = reader.load(caes_data)
        strategy = case.structure_strategy(argset.propset(), list())
        self.assertEqual([strategy[0][0], strategy[0][1][0].get_id()],[PropLiteral("murder"), "arg1" ])
        
        
        
        
        
"""-------------------------------TESTING OF THE ARGUMENTATION MODULE---------------------------------"""

"""
NOTE: testing the decision making of one of the party (e.g. opponent) is equivalent to testing the system for both parties
      given the recursive part of the software used by both parties to make a decision at each given time.
"""

"""
-------------------------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------------------------
This test is performed on a murder case. The example models a case where THE BEST OPTION for 
the opponent to make the BoP shift is attacking one if the exceptions to the argument put forward by the proposition in favor of the main statement.
The dynamics of the case should be as follows:

1. proponent states "murder" in the case
2. proponent backs up statement with an argument. BoP shifts
3. opponent counters by attacking the exception to the argument previously put forward by the proponent. 
4. opponent backs up the argument previously put forward by supporting one of its premises. BoP shifts
5. proponent tries to attack one of the premises of the argument proving the exception with an argument but fails

The OPPONENT wins the case
"""         
class ArgumentationTestCase1(unittest.TestCase):

    def test_argumentation(self):
        case = argumentation()
        correctResult = [(1, 'PROPONENT', '', 'murder', False, 'PROPONENT'), (2, 'PROPONENT', 'arg1', '[killing, malice], ~[187_excluded] => murder', True, 'OPPONENT'), (3, 'OPPONENT', 'arg2', '[self_defence], ~[197_excluded] => 187_excluded', True, 'OPPONENT'), (4, 'OPPONENT', 'arg3', '[witness1], ~[unreliable1] => self_defence', False, 'PROPONENT'), (5, 'PROPONENT', 'arg4', '[witness2], ~[unreliable2] => -self_defence', False, 'PROPONENT')]
        dialogTable = case.main(file_path="./examples/murder.txt", propToProve=PropLiteral("murder"))
        for i in range(0,(len(dialogTable))):
            with self.subTest(i=i):
                self.assertEqual((dialogTable[i][0],dialogTable[i][1],dialogTable[i][2],str(dialogTable[i][3]),dialogTable[i][4], dialogTable[i][5]), correctResult[i])
     



                
"""
-------------------------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------------------------
This test is performed on a case of human trafficking. The example models a case where THE BEST OPTION for the opponent to change the BoP is attacking  
the main conclusion directly, rather than any of the premises.
The dynamics of the case should be as follows:

1. proponent puts forward "human_trafficking" in the case
2. proponent backs up human trafficking with an argument
3. proponent backs up the argument in support of the conclusion by proving one of the premises and the BoP shifts
4. the best argument for the opponent is now attacking the conclusion (i.e. human_trafficking) directly with arg4
5. to make arg4 valid one of the premises needs to be now proven with another argument. The BoP should here shift backs
6. the proponent has no more arguments

The OPPONENT ultimately wins the case
"""
class ArgumentationTestCase2(unittest.TestCase):

    def test_argumentation(self):
        case = argumentation()
        correctResult = [(1, 'PROPONENT', '', 'human_trafficking', False, 'PROPONENT'), (2, 'PROPONENT', 'arg1', '[transport_exploit_person], ~[] => human_trafficking' , False, 'PROPONENT'), (3, 'PROPONENT', 'arg2', '[intent_of_exploit, knowledge_of_exploit], ~[] => transport_exploit_person', True, 'OPPONENT'), (4, 'OPPONENT', 'arg4', '[not_uk_citizen], ~[uk_territory] => -human_trafficking', True, 'OPPONENT'), (5, 'OPPONENT', 'arg5', '[passport], ~[not_authentic] => not_uk_citizen', False, 'PROPONENT')]
        dialogTable = case.main(file_path="./examples/human_traffic.txt", propToProve=PropLiteral("human_trafficking"))
        for i in range(0,(len(dialogTable))):
            with self.subTest(i=i):
                self.assertEqual((dialogTable[i][0],dialogTable[i][1],dialogTable[i][2],str(dialogTable[i][3]),dialogTable[i][4], dialogTable[i][5]), correctResult[i])




"""
-------------------------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------------------------
This test is performed on a case of human trafficking like previously described. The Opponent however, this time attacks one of the premises in the con
arguments rather than the main statement directly, given the changed highest weight.

The OPPONENT ultimately wins the case
"""
class ArgumentationTestCase3(unittest.TestCase):

    def test_argumentation(self):
        case = argumentation()
        correctResult = [(1, 'PROPONENT', '', 'human_trafficking', False, 'PROPONENT'), (2, 'PROPONENT', 'arg1', '[transport_exploit_person], ~[] => human_trafficking', False, 'PROPONENT'), (3, 'PROPONENT', 'arg2', '[intent_of_exploit, knowledge_of_exploit], ~[] => transport_exploit_person', False, 'PROPONENT'), (4, 'PROPONENT', 'arg7', '[witness2], ~[unreliable2] => knowledge_of_exploit', True, 'OPPONENT'), (5, 'OPPONENT', 'arg3', '[consense], ~[] => -transport_exploit_person', True, 'OPPONENT'), (6, 'OPPONENT', 'arg6', '[witness1], ~[unreliable1] => consense', False, 'PROPONENT')]
        dialogTable = case.main(file_path="./examples/human_traffic2.txt", propToProve=PropLiteral("human_trafficking"))
        for i in range(0,(len(dialogTable))):
            with self.subTest(i=i):
                self.assertEqual((dialogTable[i][0],dialogTable[i][1],dialogTable[i][2],str(dialogTable[i][3]),dialogTable[i][4], dialogTable[i][5]), correctResult[i])


                
    
    
    
"""
-------------------------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------------------------
This test is performed on a case of car accident. The example models a case where THE BEST OPTION for the opponent is attacking one of the premises 
of an argument put forward by the proponent. 
The dynamics of the case should be as follows:

1. proponent puts forward "accident_fault" int the case
2. proponent backs up the conclusion with an argument 
3. proponent supports one of the premises of the argument previously put forward with an argument
4. proponent supports the second premise of the argument initially put forward with an argument. BoP shifts
5. opponent CHOSES to attack one of the premises, rather than the main statement directly, since it has the strongest case against it
6. after failing the attack to the premise now the opponent tries to disproof the main statement directly 

The PROPONENT ultimately wins the case
"""
class ArgumentationTestCase4(unittest.TestCase):


    def test_argumentation(self):
        case = argumentation()
        correctResult = [(1, 'PROPONENT', '', 'accident_fault', False, 'PROPONENT'), (2, 'PROPONENT', 'arg1', '[caused_it, violated_traffic_laws], ~[] => accident_fault', False, 'PROPONENT'), (3, 'PROPONENT', 'arg3', '[witness2], ~[unreliable2] => violated_traffic_laws', False, 'PROPONENT'), (4, 'PROPONENT', 'arg2', '[witness1], ~[unreliable1] => caused_it', True, 'OPPONENT'), (5, 'OPPONENT', 'arg6', '[witness4], ~[unreliable4] => -caused_it', True, 'OPPONENT'), (6, 'OPPONENT', 'arg4', '[-caused_it, -violated_traffic_laws], ~[was_behind] => -accident_fault', True, 'OPPONENT')]
        dialogTable = case.main(file_path="./examples/accident.txt", propToProve=PropLiteral("accident_fault"))
        for i in range(0,(len(dialogTable))):
            with self.subTest(i=i):
                self.assertEqual((dialogTable[i][0],dialogTable[i][1],dialogTable[i][2],str(dialogTable[i][3]),dialogTable[i][4], dialogTable[i][5]), correctResult[i])
         


    
    
    
    
"""
-------------------------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------------------------
This test is performed on a case of inappropriate photography. The example models a case where THE BEST OPTION for the opponent to make
the BoP shift is attacking the main statement directly, but THE BEST counter move of the opponent is attacking one of the exceptions.
The dynamics of the case should be as follows:

1. proponent states "inappropriate_photography" in the case
2. proponent backs up statement with an argument
3. proponent supports one of the premises of the previous argument with an argument. BoP shifts
4. opponent counters by attacking "inappropriate_photography" directly
5. opponent backs up argument put forward with an argument in support of one of the premises. Bop shifts
6. proponent tries to prove the exception to the argument against "inappropriate_photography" given it has the highest weight

The OPPONENT ultimately wins the case
"""
class ArgumentationTestCase5(unittest.TestCase):

    def test_argumentation(self):
        case = argumentation()
        correctResult = [(1, 'PROPONENT', '', 'inappropriate_photography', False, 'PROPONENT'), (2, 'PROPONENT', 'arg1', '[private_property, prohibited], ~[] => inappropriate_photography', False, 'PROPONENT'), (3, 'PROPONENT', 'arg4', '[proof_of_sign], ~[unreliable_proof] => prohibited', True, 'OPPONENT'), (4, 'OPPONENT', 'arg2', '[public_property], ~[of_people_in_privacy] => -inappropriate_photography', True, 'OPPONENT'), (5, 'OPPONENT', 'arg6', '[governament_ownership], ~[] => public_property', False, 'PROPONENT'), (6, 'PROPONENT', 'arg3', '[secluded], ~[] => of_people_in_privacy', False, 'PROPONENT')]
        dialogTable = case.main(file_path="./examples/photography.txt", propToProve=PropLiteral("inappropriate_photography"))
        for i in range(0,(len(dialogTable))):
            with self.subTest(i=i):
                self.assertEqual((dialogTable[i][0],dialogTable[i][1],dialogTable[i][2],str(dialogTable[i][3]),dialogTable[i][4], dialogTable[i][5]), correctResult[i])
    
         
         
         
         

"""
-------------------------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------------------------
This test is performed on a simplified murder case. The example is supplied with the open source carneades implementation and its dynamics should be as follows:

1. proponent puts forward "murder" in the case
2. proponent pics the only argument available in the graph to support "murder" i.e.  
3. proponent backs up argument previously put forward with a witness
4. proponent has nothing more to do, the BoP never changes

the dynamics of this case are consistent with the example provided in caes.py
the PROPONENT ultimately wins the case
"""
class ArgumentationTestCase6(unittest.TestCase):

    def test_argumentation(self):
        case = argumentation()
        dialogTable = case.main(file_path="./examples/syntaxEx.txt", propToProve=PropLiteral("murder"))
        correctResult = [(1, 'PROPONENT', '', 'murder', False, 'PROPONENT'), (2, 'PROPONENT', 'arg1', '[intent, kill], ~[] => murder', False, 'PROPONENT'), (3, 'PROPONENT', 'arg2', '[witness1], ~[unreliable1] => intent', False, 'PROPONENT')]
        for i in range(0,(len(dialogTable))):
            with self.subTest(i=i):
                self.assertEqual((dialogTable[i][0],dialogTable[i][1],dialogTable[i][2],str(dialogTable[i][3]),dialogTable[i][4], dialogTable[i][5]), correctResult[i])

     

     
     
     
     
     
     
     

def load_tests():
    test_cases = [BestArgsTest, GetPropsTest, StrategyTest, ArgumentationTestCase1, ArgumentationTestCase2, ArgumentationTestCase3, ArgumentationTestCase4, ArgumentationTestCase5, ArgumentationTestCase6]
    suite = unittest.TestSuite()
    for test_class in test_cases:
        loader = unittest.TestLoader()
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    return suite
        
mySuit=load_tests()
runner=unittest.TextTestRunner()
runner.run(mySuit)