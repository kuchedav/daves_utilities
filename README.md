# daves_utilities

## description
Daves utilities is a collection of function which I repeatedly needed but did not find implemented for python.

## installation
pip install daves_utilities

## functions
- for_long  
  adds some useful functionalities for long running loops
  - Save progress and return calculation where you left off
  - Input multiple list to iterate over permutation of all input lists
  - Loading bar
- fun_save  
  Saves the output of any function to a pickle file.
  If the function is run again it will check the input paramters against the saved file.
  If the input is exactly the same, it will just read the pickle instead of recalculating.
- is_equal  
  Compare two arbitrary python objects. The function will check recourively in any iterative object.
- print_structure  
  Print the structure of any pyhton object.
