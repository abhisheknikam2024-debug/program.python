# program.pytho

Tinker GUI cslculator application 
  @feature 
  - numeric keypad : buton to  input  number 0 to 9
  - basic arithmatic operation 
   1. addition
   2. subtraction
   3. multiplication
   4. division 
  - cantrol function 
   1. equal : compute and display the result 
   2. clear : reset or clear the display enrty box

 - code overvier 
  1. main window set up : configur 500x500 pixel window (Tk()).
  2. input field : use a tkinter .entry widget  to display input value and calculate result.
  3. event collback : 
      - click (num): display the number in display 
      - add(),sub(),mul(),div() : operator to perfrom oparation 
      - equal (): perform the calculation according to  the opertor and outputs the result
      - clear (): clear the display 
