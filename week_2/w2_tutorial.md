

**MOVIE THEATER ADMISSION SYSTEM :)**


------------------------------------------------------------------------
**1. IDENTIFY THE COMPONENTS**
------------------------------------------------------------------------

**1.1. What are the inputs?**
   - Age (Integer)          : The physical age of the person trying to enter.
   - Accompanied (Boolean)  : True if accompanied by an adult, False if alone.
   - Valid Ticket (Boolean) : True if the person has a valid ticket, False if not.

**1.2. What is the process?**
- Step 1: Evaluate the age and accompaniment rules. A user satisfies this
               condition if they are 13 or older OR accompanied by an adult.
               
- Step 2: Evaluate the entry permission by combining the previous condition 
               with the ticket status. The user must have a valid ticket AND
               satisfy the age/accompaniment criteria.
               
- Logical Formula: (Age >= 13 OR Accompanied) AND ValidTicket

**1.3. What is the output?**
- Admission Status        : "Allowed to Enter" (Access Granted) OR 
                                  "Denied Entry" (Access Denied).


------------------------------------------------------------------------
**2. DESIGN THE ALGORITHM**
------------------------------------------------------------------------

**2.1. Flowchart Diagram Logic**

      [Start] -> [Input: age, accompanied, ticket] -> [Is ticket valid?]
                                                             |
                                                   +---------+---------+
                                                   | Yes               | No
                                                   v                   v
                                     [age >= 13 OR accompanied?]  [Denied Entry]
                                                   |                   |
                                         +---------+---------+         |
                                         | Yes               | No      |
                                         v                   v         v
                                  [Allowed Entry]      [Denied Entry] 
                                         |                   |
                                         +---------+---------+
                                                   |
                                                   v
                                                [End]

**2.2. Complete the Truth Table**
     
     Let:
     A = User is 13 years old or older
     B = User is accompanied by an adult
     C = User has a valid ticket
     Y = Admission Allowed (Output)

     
      A (Age>=13) | B (Accompanied) | C (Valid Ticket) |    A OR B Rule    | Y (Admission Allowed)
     +------------+-----------------+------------------+-------------------+----------------------+
        0 (No)    |     0 (No)      |      0 (No)      |       0 (F)       |      0 (Denied)     
        0 (No)    |     0 (No)      |      1 (Yes)     |       0 (F)       |      0 (Denied)     
        0 (No)    |     1 (Yes)     |      0 (No)      |       1 (T)       |      0 (Denied)     
        0 (No)    |     1 (Yes)     |      1 (Yes)     |       1 (T)       |      1 (Allowed)    
        1 (Yes)   |     0 (No)      |      0 (No)      |       1 (T)       |      0 (Denied)     
        1 (Yes)   |     0 (No)      |      1 (Yes)     |       1 (T)       |      1 (Allowed)    
        1 (Yes)   |     1 (Yes)     |      0 (No)      |       1 (T)       |      0 (Denied)     
        1 (Yes)   |     1 (Yes)     |      1 (Yes)     |       1 (T)       |      1 (Allowed)    
     

**2.3. Design an Algorithm**
- Step 1: Start.
- Step 2: Read age.
- Step 3: Read accompanied_status (True/False).
- Step 4: Read ticket_status (True/False).
- Step 5: If ticket_status is False, go to Step 8.
- Step 6: If age is greater than or equal to 13 OR accompanied_status is True, go to Step 9.
- Step 7: Go to Step 8.
- Step 8: Set status = "Denied Entry", then go to Step 10.
- Step 9: Set status = "Allowed to Enter".
- Step 10: Display status.
- Step 11: End.

**2.4. Create Pseudocode**
     
     BEGIN
         DISPLAY "Enter customer age: "
         INPUT age
         DISPLAY "Is customer accompanied by an adult? (true/false): "
         INPUT is_accompanied
         DISPLAY "Does customer have a valid ticket? (true/false): "
         INPUT has_ticket

         // Check conditional statements
         IF (age >= 13 OR is_accompanied == true) AND has_ticket == true THEN
             DISPLAY "OUTPUT: Access Granted. Allowed to enter."
         ELSE
             DISPLAY "OUTPUT: Access Denied. Not allowed to enter."
         ENDIF
     END


------------------------------------------------------------------------
**3. EVALUATE EXPRESSION**
------------------------------------------------------------------------

**3.1. Test with some input samples**

- Sample Case 1: Underage and alone, with ticket
     - Inputs: age = 11, is_accompanied = false, has_ticket = true
     - Evaluation: (11 >= 13 OR false) AND true -> (false OR false) AND true -> false AND true -> false
     - Expected Output: Denied Entry

- Sample Case 2: Underage and accompanied, with ticket
     - Inputs: age = 10, is_accompanied = true, has_ticket = true
     - Evaluation: (10 >= 13 OR true) AND true -> (false OR true) AND true -> true AND true -> true
     - Expected Output: Allowed to Enter
