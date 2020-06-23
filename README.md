# Formula Validator
This project provides a device for verifying whether a formula of the propositional calculus is a tautology. The GUI of the
application has been written using Tkinter. The interface includes buttons for variable creation (p and |, which enable producing p, p|, p||, p|||...) and for the logical connectives. As a user you can type a formula and press 'validate' button; the application can give one of the three answers: TAUTOLOGY, SYNTAX ERROR or a valuation for which the formula is invalid.
Typing a formula must conform to certain conventions (otherwise the answer will be SYNTAX ERROR), namely you must use parenthesis for any 
two-argument logical connective, however, you don't have to add extra parenthesis for negation and you don't have to bracket the whole formula. Some examples of accepted formulas: pU~p, ~(p&~p), (pUp|)=>~p|, (p=>p|)U(p|=>p), 
(pU(p|&p||))<=>((pUp|)&p||). 

A valuation for which the formula is invalid is given as a sequence of 0's and 1's where first digit corresponds to the variable in the formula with the fewest number of bars "|", the second digit to the variable with second fewest number of bars ect.
For instance, for the formula ~p||Up|, '01' is a valuation given as the answer (0 corresponds to p| and 1 corresponds to p||).

Logic of the application:
The formula typed by a user is parsed (for instance variables are substituted for initial natural numbers), then the formula is transformed
into Reverse Polish Notation with the help of the standard algorithm based on the use of a stack. Then a stack is used again in a function to compute boolean value of the formula in RPN for a given valuation c (sequence of 01's of a length equal to the number of variables in the formula). Finally, we make use of Gray-code in a function that generates succesively 01-sequences until a counterexample is found or it returns None otherwise. The answer of this function is then presented in the user's interface.

To use the application you need simply to run the 'main.py' file.
