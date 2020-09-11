School Enrollment REST API demo using Python and Flask framework

=============
Instructions:
=============
1. Initiate virtual server environment by executing the python file enroll.py 
2. From the path folder where enroll.py is located type: 
   C:\your_folder>python enroll.py
   
   -- Ensure that Python and Flask framework are installed in your PC --
   Python - https://www.python.org/downloads/ (Python 2.7 was used on enroll.py)
   Flask - C:\> pip install flask
   
3. Point your internet browser to 'http://127.0.0.1:5000/'
4. Click the 'Add' button to add the sample record
5. Click the 'Update' button to update the sample record
6. Click the 'Detete' button to update the sample record
7. The local database is stored on 'students.db'
8. You can open your preferred database browser to monitor database record changes
9. Click the link "http://127.0.0.1:5000/fetchStudents?class=3 A" to view the students under class '3 A'
10. Click the link "http://127.0.0.1:5000/fetchStudents?id=223444" to view record id 223444

Notes:
REST API static inputs in these examples should suffice as per required in Test#1 guideline. 
A more dynamic based inputs can be developed, time permitting.

