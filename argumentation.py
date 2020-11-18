from caes import *


class argumentation(object):
    
    def __init__(self):
        self.dialogOutput        = ""
        self.case_caes           = None
        self.case_argset         = None
        self.new_argset          = ArgumentSet()
        self.new_assumptions     = {}
        self.new_weights         = {}
        self.new_audience        = Audience({},{})
        self.ps_to_make          = []
        self.new_ps              = ProofStandard([])
        self.new_caes            = None
        self.toProve             = None
        self.propsWithArgsInCase = set()
        self.proponentArgs       = None
        self.opponentArgs        = None
        self.dialogTable         = list()
        

        
        
        
        
        
    """ ----------------------------------------------------------------
        Function that prints the dialog table in a human readable format
        ----------------------------------------------------------------
    """    
    def printDialog(self):
        if (len(self.dialogTable)!=0):
            
            print("\n\n\n\n\n\n--------------------------------------------------------------------------------------------\n"+\
              "--------------- CASE DEBATED OVER STATEMENT << "+ str(self.toProve) + " >> ------------\n" +\
              "--------------------------------------------------------------------------------------------\n\n\n")
              
            print("-----------------------------------------------------------------------------------------------------\n"+\
                 "-----------------------------------------------STEP 1------------------------------------------------\n"+\
                 "-----------------------------------------------------------------------------------------------------\n\n"+\
                 self.dialogTable[0][1] + " puts main statement << " + str(self.dialogTable[0][3]) + " >> forward\n\n"+\
                 "main statement << "+ str(self.dialogTable[0][3]) +" >>"+ " NOT ACCEPTED at this point in the case\n\n"+\
                 "----<< BURDEN OF PROOF ON " + self.dialogTable[0][5] + " >>---\n\n\n")
              
            for i in range(1,(len(self.dialogTable))):
            
                print("-----------------------------------------------------------------------------------------------------\n"+\
                 "-----------------------------------------------STEP "+ str(self.dialogTable[i][0]) +"------------------------------------------------\n"+\
                 "-----------------------------------------------------------------------------------------------------\n\n\n"+\
                 self.dialogTable[i][1] + " tries to prove << " + str(self.dialogTable[i][3].get_conclusion()) + " >>\n"+\
                 self.dialogTable[i][1] + " puts forward << "+ str(self.dialogTable[i][3]) +" >>")
                
                if(self.dialogTable[i][4]==True):
                    print("\nmain statement << "+ str(self.toProve) +" >> is ACCEPTABLE at this point in the case")
                else:
                    print("\nmain statement << "+ str(self.toProve) +" >> is NOT ACCEPTABLE at this point in the case")
                if(self.dialogTable[i][1]!=self.dialogTable[i][5]):
                    print("\n----<< BURDEN OF PROOF SHIFTS from "+ self.dialogTable[i][1] +" to "+ self.dialogTable[i][5] +" >>---\n\n")
                else:
                    print("\n----<< BURDEN OF PROOF DOESN'T SHIFT >>---\n\n")
                    
            print("-----------------------------------------------------------------------------------------------------")
            print(self.dialogTable[(len(self.dialogTable)-1)][5] + " has nothing more to do.")
            if(self.dialogTable[(len(self.dialogTable)-1)][4]==True):
                print("\n\n\nTHE  PROPONENT  WINS THE CASE \nTHE STATEMENT << "+str(self.toProve)+" >> IS ULTIMATELY ACCEPTED IN THE CASE CASE ")
            else:
                print("\n\n\nTHE  OPPONENT  WINS THE CASE \nTHE STATEMENT << "+str(self.toProve)+" >> IS ULTIMATELY NOT ACCEPTED IN THE CASE CASE ")
                
            
        else:
            print("No dialog to print.")

            
            
            
            
            
        
    """ ------------------------------------------------------
        Function that returns opposition for the current party
        ------------------------------------------------------
    """
    def opposition(self, party):
        if(party=="PROPONENT"):
            return "OPPONENT"
        else:
            return "PROPONENT"

    
 
    
    
    """ --------------------------------------------------------------------------------
        Function that updates the new caes with the current "new" variables in the class
        --------------------------------------------------------------------------------
    """
    def build_new_caes(self):
        self.new_audience = Audience(self.new_assumptions, self.new_weights)
        self.new_caes = CAES(self.new_argset, self.new_audience, self.new_ps)
    
    
   
    
    
    
    
    """ -------------------------------------------------
        Function that returns the best arguments to apply
        -------------------------------------------------
        the method, given a caes and a PropLiteral, returns a list of the arguments to apply ordered in descending order of weight 
        (i.e. best-to-worst to apply) for proving the proposition. If no arguments can be applied the methods returns an empty list
    """
    def get_best_args(self, prop):
        if(prop in self.propsWithArgsInCase):
            proArgs = self.case_argset.get_arguments(prop)
            #order list
            proArgs = sorted(proArgs, key= lambda x: self.case_caes.weight_of(x), reverse=True)
            return proArgs
        else:
            return list()

            
            
            
            
            
            
            
            
    """ -------------------------------------------------------------
        Function that returns the propositions to counter for a party
        -------------------------------------------------------------
        the method, given a list of arguments (which should be all in favor of either the opponent or proponent), returns a list of 
        all possible propositions to attack 
        e.g. if arg1 is an argument in favor or Proponent, and the conclusion of arg1 is murder
        then -murder will be returned in the list; opponent can therefore look for args in favor of -murder to conunter Proponent. 
        The list of propositions is ordered with first the arguments conclusions,exceptions and ultimetely
        premises
        -> this is equivalent of retrieving a list of possible critical questions for the opponent
    """
    def get_props_to_counter(self, args):
        conclusionList = list()
        premisesList = list()
        exceptionsList = list()
        if (args != None):
            for arg in args:
                conclusionList.append(arg.get_conclusion())
                premisesList += arg.get_premises()
                exceptionsList += arg.get_exceptions()
            conclusionList = list(map(lambda x: x.negate(), conclusionList))
            premisesList = list(map(lambda x: x.negate(), premisesList))
            return conclusionList + exceptionsList + premisesList
        else:
            return list()
        
        
        
        
        
        
        
        
        
    """ ----------------------------------------------------------
        Function that returns a strategy for argument introduction
        ----------------------------------------------------------
        the method, given a list of propositions and of arguments returns an ordered list of (proposition, argumentList) tuples.
        argumentList is the list of arguments for the correspondent proposition, with the best-to-worst ordering
        e.g.
        returns
        (proposition1, [arg1,arg3])
        (proposition2, [arg2,arg4,arg6, arg5])
        (proposition3, [arg10,arg11,arg2])
                    ...
        (proposition_n, [arg7,arg32,arg15])
       
        where arg1 is the best argument applicable for proposition1 (and also against arg2, arg10, arg7 ... etc.)
        Moreover, no argument in the list of arguments passed as a parameter is present in the tuple lists
        Note: for the ordering to make sense the passes propositions should be all propositions in favor of either the
              Proponent or the Opponent
    """
       
    def structure_strategy(self, props, args):
        strategyList = list()
        if(props != None):
            for prop in props:
                listForProp = list(filter(lambda x: x not in args, self.get_best_args(prop)))
                if (len(listForProp) != 0):
                    strategyList.append((prop, listForProp))
            return sorted(strategyList, key= lambda x: self.case_caes.weight_of(x[1][0]), reverse=True)
        else:
            return list()
        
        
        
        
        
        
        
        
        
        
    """ -------------------------------------------
        Function that performs one step of the case
        -------------------------------------------
        the method does the following:
             - the party (either proponent or opponent) looks for all possible critical questions (all propositions they could possibly argue against the opposition)
             - the party also looks at all propositions in their favor (which they could provide further arguments for)
             - the party chooses best card on their deck, i.e best argument they could put forward at the moment
             - the party puts it forward, checks acceptability and keeps the burder or shifts it depending on the result
    """  
    def make_step(self, props, stepNo, party):
            
        """---------- looks for the best proposition to support with an argument and puts it forward --------"""
        strategy = self.structure_strategy(props, self.new_caes.get_arguments())
        if(len(strategy) != 0):
        
            argToApply = strategy[0][1][0]
            argID = argToApply.get_id()
            
            
            self.new_argset.add_argument(argToApply, arg_id = argID)
            self.new_weights[argID] = self.case_caes.weight_of(argToApply)
            standardToAdd = argToApply.get_conclusion()
            self.ps_to_make.append((standardToAdd, (self.case_caes.get_proof_standards().get_proofstandard(standardToAdd))))
            self.new_ps = ProofStandard(self.ps_to_make)
            self.build_new_caes()
            if(party=="PROPONENT"):
                self.proponentArgs.append(argToApply)
            else:
                self.opponentArgs.append(argToApply)
            acceptable = self.new_caes.acceptable(self.toProve)
            
            
            """----------------------- checks for acceptability and shifts burden accordingly -------------------"""
                        
            """---------SHIFT of BOP---------"""
            
            if((acceptable==True and party=="PROPONENT") or (acceptable==False and party=="OPPONENT")):
                
                
                self.dialogTable.append((stepNo, party, argID, argToApply, acceptable, self.opposition(party)))
                
                nextStepProps = list()
                if(party=="PROPONENT"):
                    nextStepProps = list(set(self.get_props_to_counter(self.proponentArgs)+list(map(lambda x: x.negate(), self.get_props_to_counter(self.opponentArgs)))))
                else:
                    nextStepProps = list(set(self.get_props_to_counter(self.opponentArgs)+list(map(lambda x: x.negate(), self.get_props_to_counter(self.proponentArgs)))))
                """---iterative step---"""
                self.make_step(nextStepProps, (stepNo+1), self.opposition(party))
    
            else:
                """-------NON SHIFT of BOP-------"""
                
                
                self.dialogTable.append((stepNo, party, argID, argToApply, acceptable, party))
                
                nextStepProps = list()
                if(party=="PROPONENT"):
                    nextStepProps = list(set(self.get_props_to_counter(self.opponentArgs)+list(map(lambda x: x.negate(), self.get_props_to_counter(self.proponentArgs)))))
                else:
                    nextStepProps = list(set(self.get_props_to_counter(self.proponentArgs)+list(map(lambda x: x.negate(), self.get_props_to_counter(self.opponentArgs)))))
                """---iterative step---"""
                self.make_step(nextStepProps, (stepNo+1), party)
        
     
     
     
     
     
     
     
     
    """ ---------------------------------------------------------
        Function that propts the user for inputs to load the case 
        ---------------------------------------------------------
        this method prompts the user for inputs to load the case when those are not 
        specified to the main function beforehand
    """
    def loadCase(self, file_path, propToProve):
    
        """ ---------------------------------INPUT READING-------------------------------------------------------------------------------- """
        
        """if not given to main prompts user for case to load"""
        if(file_path==""):
            file_path = input("\n-----------------------------------------------------------------------------------------------\n" +\
                              "Please insert the path of the argument file to be loaded (from the current folder). \npath: ")
            
        reader = Reader()
        data = open(file_path)
        (self.case_argset, self.case_caes) = reader.load(data)
        
        """if not given to main prompts user for proposition to prove"""
        if(propToProve==None):
            print("\n-----------------------------------------------------------------------------------------------------\n")
            print("                                      LIST OF PROPOSITIONS                                ")

            argList = list(self.case_argset.propset())
            for i in range(1, len(argList)):
                print("[ ",i," ]  "+str(argList[i-1])+"\n")
            print("\n")

            argChoice = str()
            while argChoice not in map(lambda x: str(x), range(1,len(argList))):
                argChoice = input("Please insert the number correspondent to the proposition the PROPONENT wants to put forward in the argument: ")

            propToProve = argList[int(argChoice)-1]
            
        self.toProve = propToProve

        for arg in self.case_caes.get_arguments():
            self.propsWithArgsInCase.add(arg.get_conclusion())
            
        """ ------------------------------------------------------------------------------------------------------------------------------
            ------------------------------------------------------------------------------------------------------------------------------"""
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
    """ -------------------------------------------
        ----------------MAIN METHOD----------------
        -------------------------------------------
        
        The main method models a case in a court where a proponent (prosecution) and an opponent argue over a main statement.
         - initially the user specifies the path of the file containing all the information about the case
         - the user then chooses a statement from a list of statements. The statements will be argued over in the case.
         - the proposition then performs 2 SPECIAL steps:
                * one where it puts the pure statement forward to start the case; and
                * one where it looks for an argument in support of it
         following this initial steps, then, a pattern for either the opponent or the proponent repeats and thus is implemented in a loop, i.e.:
                - the party (either proponent or opponent) look for all possible critical questions (all propositions they could possibly argue against the opposition)
                - the party also looks at all propositions in their favor (which they could provide further arguments for)
                - the party chooses best card on their deck, i.e best thing they could put forward at the moment
                - the party puts it forward, checks acceptability and keeps the burder or shifts it depending on the result
         the main method heavily relies on the other methods in the class
    """
    def main(self, file_path="", propToProve=None):
    
        
        """loads the the case to use for the dialog"""
        self.loadCase(file_path, propToProve)
                
        """start out with a blank new caes"""
        self.new_assumptions = self.case_caes.get_assumptions()
        self.build_new_caes()
        
        """lists of arguments put forward for the proponent and opponent"""
        self.proponentArgs = list()
        self.opponentArgs = list()

              
        """-------------------------FIRST STEP-----------------------------"""
        stepNo = 1
        party = "PROPONENT"
        bop = party
        argID = ""
        acceptable = False
        
        self.dialogTable.append((stepNo, party, argID, self.toProve, acceptable, bop))
        
        
        """-------------------------SECOND STEP----------------------------"""
        stepNo = 2
        party = "PROPONENT"
        
        """    get best argument to apply """
        argsToApply = self.get_best_args(self.toProve)
        if(len(argsToApply) != 0):
            argToApply = argsToApply[0]
            
            
            """includes the chosen argument to the case so far debated and updates it with all relevant information"""
            argID = argToApply.get_id()
            self.new_argset.add_argument(argToApply, arg_id = argID)
            self.new_weights[argID] = self.case_caes.weight_of(argToApply)
            standardToAdd = argToApply.get_conclusion()
            self.ps_to_make.append((standardToAdd, (self.case_caes.get_proof_standards().get_proofstandard(standardToAdd))))
            self.new_ps = ProofStandard(self.ps_to_make)
            self.build_new_caes()
            self.proponentArgs.append(argToApply)
            
            acceptable = self.new_caes.acceptable(self.toProve)
            
        
        
        
        
            """------------------------ STEP FROM 2 ONWARDS -------------------------------"""    
        
            """---------SHIFT of BOP---------"""
            
            if((acceptable==True and party=="PROPONENT") or (acceptable==False and party=="OPPONENT")):
                
                
                self.dialogTable.append((stepNo, party, argID, argToApply, acceptable, self.opposition(party)))
                
                nextStepProps = list()
                if(party=="PROPONENT"):
                    nextStepProps = list(set(self.get_props_to_counter(self.proponentArgs)+list(map(lambda x: x.negate(), self.get_props_to_counter(self.opponentArgs)))))
                else:
                    nextStepProps = list(set(self.get_props_to_counter(self.opponentArgs)+list(map(lambda x: x.negate(), self.get_props_to_counter(self.proponentArgs)))))
                """--- iterative step ---"""
                self.make_step(nextStepProps, (stepNo+1), self.opposition(party))
                
            else:
            
                """-------NON SHIFT of BOP-------"""
                
                self.dialogTable.append((stepNo, party, argID, argToApply, acceptable, party))
                
                nextStepProps = list()
                if(party=="PROPONENT"):
                    nextStepProps = list(set(self.get_props_to_counter(self.opponentArgs)+list(map(lambda x: x.negate(), self.get_props_to_counter(self.proponentArgs)))))
                else:
                    nextStepProps = list(set(self.get_props_to_counter(self.proponentArgs)+list(map(lambda x: x.negate(), self.get_props_to_counter(self.opponentArgs)))))
                """--- iterative step ---"""
                self.make_step(nextStepProps, (stepNo+1), party)
                
                
                
            """-----------------------------END OF STEPS -------------------------------""" 
            
        # Comment out the following line if you don't want the dialog to be printed
        self.printDialog()
        
        # Uncomment the following lines if you want the table to be printed
        #for line in self.dialogTable:
        #    print(line)
            
        return self.dialogTable
        
        
        
        
if __name__ == "__main__":
    case = argumentation()
    case.main()

































