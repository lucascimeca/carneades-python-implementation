Luca Scimeca
UNN: s1344727



--------------------------------
CARNEADES LOADING IMPLEMENTATION
--------------------------------


-----------------------------------------------------------------------------------------------
----------------------------------SYNTAX-------------------------------------------------------
-----------------------------------------------------------------------------------------------

 - The input file to load with Carneades needs to be split in exactly three sets of curly brackets to specify:
   arguments, proof standards and assumptions respectively.
   Inside each of the sets the parameters need to be specified like described below:

  -----ARGUMENTS-----

  syntax:  Argument_Name(audience_weight): conclusion; premises; exceptions;

  - "Argument_Name" is the argument name, it can contain any letter and the symbol '_'.
  - "audience_weight" is the weight of the argument for the audience.
     The weight needs to be put in round parenthesis and has to be a number within 0 and 1
  - "conclusion" is the conclusion for the argument. Only one conclusion
     should be instantiated, an error will occur otherwise.
  - "premises" are a list of premises for the argument. The list should be 
     separated by commas for clarity, however, the absence of these will not
     affect the loading process.
  - "exceptions" is a list of exceptions for the argument. The list should be 
     separated by commas for clarity, however, the absence of these will not
     affect the loading process.
  - A ':' separates the argument name and weight from the parameters.
  - A ';' separates each of the sections (conclusion, premises and exception)
  - A '#' if nothing applies for the specific case. The absence of the '#' will
    not effect the loading process.
  - Each argument should be instantiated in a new line.

  EXAMPLE:

  {
  arg1(0.8): murder; kill, intent; # ;
  arg2(0.3): intent; witness1; unreliable1;
  arg3(0.8): -intent; witness2; unreliable2;
  }


  -----PROOF STANDARDS---

  syntax:  proposition1, name_of_proofstandard1;

  - "proposition1" is the name of the proposition to be assigned a proofstandard.
    The default proof standard for propositions which are not assigned one 
    is 'scintilla'.
  - "name_of_proofstandard1" is the name of the proof standard to be used, an exception
    will be thrown if the proof stanrdard is not in the following list:
    'scintilla', 'preponderance', 'clear_and_convincing', 'beyond_reasonable_doubt' and
    'dialectical_validity'.
  - A comma separates the proposition name to the name of the proof standard, however, 
    a missing comma does not affect the loading process as long as long as 2 variables 
    are specified.
  - A ';' separates each proof standard assignment.
  - Proof standards should be put in new lines for clarity, however, this will not
    affect the loading process.
  
  EXAMPLE:
   
  {
  intent, beyond_reasonable_doubt;
  kill, preponderance;
  unreliable1, beyond_reasonable_doubt;
  }


  -----ASSUMPTIONS-----
  
  syntax:  assumption1, assumption2, assumption3;

  - "assumption1" is the name of the proposition to be assumed at priori 
    (assumption2 and assumption3 likewise).
  - Commas separate each of the assumptions, however, the absence of these will not
    affect the loading process.
  - A ';' should be added at the end of the list for clarity and consistency, however,
    the absence of this will not affect the loading performance.
  
  EXAMPLE:
  
  {
  kill, witness1, witness2, unreliable2;
  }

  
  ----COMMENTS-----

  Anything outside the three sets of brackets are comments on the case and thus will not be
  processed. The comments should not include '{' or '}' symbols but can otherwise be anything.


-----------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------



-------to create a new case do the following:

1. create a new text file "caesfile.txt" in the carneades folder 
   (use the directions in the "SYNTAX" section above to write the case)
3. save the file

NOTE: The 'sintaxEx.txt' file in the 'example' folder is a syntactically correct example in caes, 
      and can be looked at for guidance.
      The file'sintaxEx.txt' can be loaded and drawn like you would any other example, . 




-------to load a case in caes do the following:

1. run shell
2. navigate into the carneades folder
3. run python3.4
4. >>> from caes import *
5. >>> caes_data = open('examples\ex1.txt')
6. >>> reader = Reader() 
7. >>> (argset, caes) = reader.load(caes_data)

- "caes" will be the CAES object returned with the values of the loaded case
- "argset" will be the argset loaded from the file
- messages should progressively show what's been successfully loaded in the file

*try caes.get_all_arguments() to show the arguments loaded
*try to call argset.draw() to check weather the arguments were loaded like intended
*try to open 'examples\ex2.txt' and 'examples\ex3.txt' and repeat the process

(the function doIt() by default loads and draws the argument set of the 'syntaxEx.txt' example)




-------to run the tests for the load function do the following:


1. run shell
2. navigate into the carneades folder
3. type and execute "load_doctest.py -v"

  The tests cover:
  - missing brackets 
  - missing colons 
  - missing semicolons
  - missing commas 
  - omitting weight
  - weight out of bounds
  - multiple conclusions
  - wrong proof standard name
  - correct exception throwing
  - correct error handling
  - correct feedback for errors
  - correct syntax handling
  - correct arguments after loading
  - correct structure of caes loaded
  - + correct general checks for correct loading functionality

* The tests are in the form of doctest.
* Each test covers a specific output caes should give for one or more
  of the instances above specified.

* The functions are tested with the use of text files in the 'tests' folder,
  the files contain proper caes cases with minor errors (eg. missing a bracket, 
  containing multiple conclusions etc). Through doc tests, the files are loaded 
  and what's returned is matched agains expected outputs for the specific error
  in the file.
  the explanation of each test is contained in the 'load_doctest.py' file.

------to run the default tests for caes do

1. run shell
2. navigate into the carneades file
3. type and execute "caes_doctest.py -v"







---------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------








-------------------------------
CARNEADES DIALOG IMPLEMENTATION
-------------------------------



-------to upload and execute a dialog over a case do the following:

1. run shell
2. navigate to carneades folder
3. type and execute "argumentation.py"

	- when asked for path to caes file insert the path from current folder 
	  to the case file you wish to upload, the file should be in the syntax 
	  above specified 

	     EXAMPLE INPUTS

             ./examples/murder.txt
             ./examples/accident.txt
             ./examples/human_traffic.txt
             ./examples/human_traffic2.txt
             ./examples/photography.txt
             ./examples/syntaxEx.txt


	- when prompted with a list of proposition, type the number 
	  corresponding to the proposition you wish the two parties 
	  (i.e. Proponent, and Opponent) to argue over.

	      EXAMPLE INPUTS

             if file "murder.txt"  	    main proposition  "murder"
	     if file "accident.txt"         main proposition  "accident_fault"
	     if file "human_traffic.txt"    main proposition  "human_trafficking"
	     if file "human_traffic2.txt"   main proposition  "human_trafficking"
	     if file "photography.txt"      main proposition  "inappropriate_photography"
	     if file "sintaxEx.txt"         main proposition  "murder"


*The results shows the case developing in steps, from the beginning (i.e. putting 
 forward proposition to argue over) to end (i.e. final acceptance or rejection of 
 the conclusion). 
*The steps inform of the action of the party with the burden of proof. 
*At the end of each step the burden of proof is either shifted or unmoved.






-----to test the dialog do the following:

1. run shell
2. navigate to carneades folder
3. type and execute "python arg_unittest.py"


  The tests cover:
  - correct argument picking functionality        -    helper function
  - correct proposition attack functionality      -    helper function
  - correct strategy building functionality       -    helper function
  - party picking main statements as proposition to attack 
  - party picking pro/con arg premises as proposition to attack/support
  - party picking exception as proposition to attack	
  - PROPONENT winning the case
  - OPPONENT winning the case
  - multiple arguments to support one claim
  - correct proof standard updates through the dialogs


* The tests are in the form of unittests.
* Each test for the dialog testing simulates a case in carneades and matches the 
  resulting dialog against the expected. The cases used are contained in the 'examples' 
  folder.
* The arg_unittest.py file contains a detailed explanation of each test 
  considering context case and party decisions at each step for all cases.
  Please look in "arg_unittest.py" for a description of each test
* All functions in the system are separately tested