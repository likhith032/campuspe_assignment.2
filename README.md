# campuspe_assignment.2
qn-1: Personal Bio Card

Logic Used:
The program stores student details such as name, age, course, college, and email in variables.
It then prints a structured bio card using formatted strings (f-strings) and alignment formatting to display the details inside a decorative box layout.

Concepts Applied:
Variables
String formatting (f-strings)
String alignment (:<20)
Print statements

Error Handling:
Not required since the program uses predefined variable values and does not take user input.
Edge Cases Considered:
If longer text values are used, formatting alignment may need adjustment.

Tested With:
╔════════════════════════════════╗
║        STUDENT BIO CARD        ║
╠════════════════════════════════╣
║ Name    : LIKHITH N.S          ║
║ Age     : 21 years             ║
║ Course  : Python Programming   ║
║ College : VTU University       ║
║ Email   : nslikhithns@gmail.co ║
╚════════════════════════════════╝
Challenges Faced:
Aligning text properly inside the box structure using formatting techniques.


qn-2:Simple Calculator

Logic Used:
The program takes two integer inputs a and b.
It calculates addition, subtraction, multiplication, and exponentiation directly.
Division and modulus operations are performed only if b is not zero to avoid runtime errors.
Formatted print statements (f-strings) are used to display results neatly.

Concepts Applied:
Input and output
Type conversion (int())
Conditional statements (if-else)
Arithmetic operators (+, -, *, /, %, **)
Exception handling logic for zero division

Error Handling:
Checked if b is zero before performing division or modulus to prevent ZeroDivisionError.
Edge Cases Considered:
Division by zero
Modulus by zero
Large numbers 

Tested With:
Enter first number: 34
Enter second number: 39

Results:
34 + 39 = 73
34 - 39 = -5
34 ^ 39 = 534167873480318944771786224084448560214821348668661525643264
34 * 39 = 1326
34 / 39 = 0.87

Challenges Faced:
Ensuring division and modulus do not cause runtime errors
Displaying floating-point division result with 2 decimal places


