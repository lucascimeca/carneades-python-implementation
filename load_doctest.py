
"""
---------------------------------------------------------------------------------------------------------------
---------------------------LOAD FUNCTION TESTS-----------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------


-------------------LOADING FUNCTIONALITY-------------------------------------------------------
-----------------------------------------------------------------------------------------------

Example from syntaxEx.txt:      Checks wether load() loads the documented example like it should
------------------------------------------------------------------------------------------------

>>> caes_data = open('examples\syntaxEx.txt')
>>> reader = Reader() 
>>> (argset, caes) = reader.load(caes_data)
1 argument loaded successfully!
2 argument loaded successfully!
3 argument loaded successfully!
proof standard for 'intent' loaded successfully!
assumptions loaded successfully!
caes loading status: 100%


>>> caes.get_all_arguments()
[intent, kill], ~[] => murder
[witness1], ~[unreliable1] => intent
[witness2], ~[unreliable2] => -intent

>>> arg_for_intent = argset.get_arguments(PropLiteral('intent'))[0]
>>> print(arg_for_intent)
[witness1], ~[unreliable1] => intent
>>> caes.applicable(arg_for_intent)
True

>>> caes.acceptable(PropLiteral('intent'))
False

>>> any(caes.applicable(arg) for arg in argset.get_arguments(PropLiteral('intent').negate()))
False

>>> caes.acceptable(PropLiteral('intent').negate())
False

>>> caes.acceptable(PropLiteral('murder'))
False
>>> caes.acceptable(PropLiteral('murder').negate())
False





Example from human_traffic.txt:      Checks wether load() loads the documented example like it should
--------------------------------------------------------------------------------------------

>>> caes_data = open('examples\human_traffic.txt')
>>> reader = Reader() 
>>> (argset, caes) = reader.load(caes_data)
1 argument loaded successfully!
2 argument loaded successfully!
3 argument loaded successfully!
4 argument loaded successfully!
5 argument loaded successfully!
proof standard for 'human_trafficking' loaded successfully!
assumptions loaded successfully!
caes loading status: 100%

>>> caes.get_all_arguments()
[transport_exploit_person], ~[] => human_trafficking  
[intent_of_exploit, knowledge_of_exploit], ~[] => transport_exploit_person  
[consense, witness1], ~[unreliable1] => -transport_exploit_person  
[not_uk_citizen], ~[uk_territory] => -human_trafficking  
[passport], ~[not_authentic] => not_uk_citizen



-------------------ERROR HANDLING---------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------


Misplaced curly brackets:      Checks wether load() notifies the user of a mistake in bracketing when there is one
------------------------------------------------------------------------------------------------------------------

>>> caes_data = open('tests\wrong_curly_brackets1.txt')
>>> reader = Reader()
>>> (argset, caes) = reader.load(caes_data)
error: misplaced brackets in input file, there should be three sets of curly brakets in the file to be uploaded
Nothing was loaded!


>>> caes_data = open('tests\wrong_curly_brackets2.txt')
>>> reader = Reader() 
>>> (argset, caes) = reader.load(caes_data)
error: misplaced brackets in input file, there should be three sets of curly brakets in the file to be uploaded
Nothing was loaded!


>>> caes_data = open('tests\wrong_curly_brackets3.txt')
>>> reader = Reader() 
>>> (argset, caes) = reader.load(caes_data)
error: misplaced brackets in input file, there should be three sets of curly brakets in the file to be uploaded
Nothing was loaded!




Missing a colon:      Checks wether load() notifies the user when there is a colon missing in the argument specification
------------------------------------------------------------------------------------------------------------------------

>>> caes_data = open('tests\missing_arg_colon.txt')
>>> reader = Reader() 
>>> (argset, caes) = reader.load(caes_data)
1 argument loaded successfully!  
<BLANKLINE>  
ERROR: wrong syntax for arguments in input text, wrong use of ':'  
2 argument wasn't loaded!  
<BLANKLINE>  
3 argument loaded successfully!  
<BLANKLINE>  
ERROR: wrong syntax for arguments in input text, wrong use of ':'  
4 argument wasn't loaded!  
<BLANKLINE>  
5 argument loaded successfully!  
proof standard for 'human_trafficking' loaded successfully!  
assumptions loaded successfully!  
caes loading status: 100%





Missing a semicolon:      Checks wether load() notifies the user of a semicolon missing when there is one in the Argument specification
------------------------------------------------------------------------------------------------  NOTE: a semicolon missing in other parts of the load file 
																									    typically won't result in a wrong split
>>> caes_data = open('tests\missing_arg_semicolon.txt')
>>> reader = Reader() 
>>> (argset, caes) = reader.load(caes_data)
1 argument loaded successfully!
2 argument loaded successfully!
3 argument loaded successfully!
<BLANKLINE> 
ERROR: wrong syntax for argument 'arg4' in input text, wrong use of ';', three semicolons need to be instantiated at all times
The argument 'arg4' wasn't uploaded!
<BLANKLINE> 
5 argument loaded successfully!
proof standard for 'inappropriate_photography' loaded successfully!
assumptions loaded successfully!
caes loading status: 100%






Weight out of bounds:      Checks wether load() notifies the user when their inserting a weight that isn't within 0 and 1
------------------------------------------------------------------------------------------------------------------------- 

>>> caes_data = open('tests\weight_OOB.txt')
>>> reader = Reader() 
>>> (argset, caes) = reader.load(caes_data)
1 argument loaded successfully!
<BLANKLINE> 
ERROR: the weight for 'arg2' is out of bounds or has not been inserted, 
please change the weight to a value between 0 and 1 
A weight of 0 was assigned to the argument! 
<BLANKLINE> 	
2 argument loaded successfully!						  
3 argument loaded successfully!
4 argument loaded successfully!
5 argument loaded successfully!
proof standard for 'accident_fault' loaded successfully!
assumptions loaded successfully!
caes loading status: 100%






Multiple conclusions:      Checks wether load() notifies the user when they insert more than one coclusion for an argument
--------------------------------------------------------------------------------------------------------------------------

>>> caes_data = open('tests\multiple_conclusions.txt')
>>> reader = Reader() 
>>> (argset, caes) = reader.load(caes_data)
1 argument loaded successfully!
2 argument loaded successfully!
<BLANKLINE> 
ERROR: too many conclusions were added in 'arg3', only the first will be considered
<BLANKLINE> 
3 argument loaded successfully!
4 argument loaded successfully!
<BLANKLINE> 
ERROR: too many conclusions were added in 'arg5', only the first will be considered
<BLANKLINE> 
5 argument loaded successfully!
proof standard for 'accident_fault' loaded successfully!
assumptions loaded successfully!
caes loading status: 100%






Missing weight:      Checks wether load() notifies the user of a missing weight in one or more arguments
--------------------------------------------------------------------------------------------------------

>>> from caes import * 
>>> caes_data = open('tests\missing_arg_weight.txt') 
>>> reader = Reader() 
>>> (argset, caes) = reader.load(caes_data) 
1 argument loaded successfully! 
<BLANKLINE> 
ERROR: the weight for 'arg2' is out of bounds or has not been inserted, 
please change the weight to a value between 0 and 1 
A weight of 0 was assigned to the argument! 
<BLANKLINE> 
2 argument loaded successfully! 
3 argument loaded successfully! 
proof standard for 'intent' loaded successfully! 
assumptions loaded successfully!
caes loading status: 100%





Missing Proof Standard comma:  Checks wether the load() function loads and creates a caes when commas are missing from the syntax
---------------------------------------------------------------------------------------------------------------------------------

>>> from caes import * 
>>> caes_data = open('tests\missing_comma1.txt') 
>>> reader = Reader() 
>>> (argset, caes) = reader.load(caes_data) 
1 argument loaded successfully!  
2 argument loaded successfully!  
3 argument loaded successfully!  
proof standard for 'intent' loaded successfully!  
assumptions loaded successfully!  
caes loading status: 100%






Missing Assumptions' commas: Checks wether the load() function loads the assumptions independently of the missing commas in the syntax
--------------------------------------------------------------------------------------------------------------------------------------

>>> from caes import * 
>>> caes_data = open('tests\missing_comma2.txt') 
>>> reader = Reader() 
>>> (argset, caes) = reader.load(caes_data) 
1 argument loaded successfully!  
2 argument loaded successfully!  
3 argument loaded successfully!  
proof standard for 'intent' loaded successfully!  
assumptions loaded successfully!  
caes loading status: 100%





Incorrect proof standard name:   Checks wether an exception is thrown when a wron proof standard is inserted
------------------------------------------------------------------------------------------------------------

>>> from caes import * 
>>> caes_data = open('tests\mistaken_ps.txt') 
>>> reader = Reader() 
>>> (argset, caes) = reader.load(caes_data)
Traceback (most recent call last):
...
ValueError: thisisnotaproofstandard is not a valid proof standard
"""




if __name__ == '__main__':
    import os, sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))    
    from carneades.caes import *
    from carneades.tracecalls import TraceCalls
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)