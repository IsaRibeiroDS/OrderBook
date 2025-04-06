# OrderBook
OrderBook SE_2

The project requires you to use Python Object-Oriented Programming (OOP) knowledge to create 
the classes for an application that collects all tasks for a software company. This will let you further 
practice working on objects which contain references to other objects. 
The project is constructed in “Parts” that are ordered and serve as a guide towards the final 
implementation.  


Part 1: Task 
create a class named Task which models a single task in a software company’s list of 
tasks. 

Tasks have: 
• A description 
• An estimated number of hours for completion 
• The name of the programmer assigned to it 
• A status field to indicate if it is finished 
• A unique identifier 
 
Part 2: OrderBook 
write a class named OrderBook that collects all the tasks ordered from a software 
company. 

Your class should contain the following methods: 
• A method to add a new order to the OrderBook. The OrderBook stores the orders 
internally as Task objects. The method should take a description, a programmer and a 
workload as arguments. 
• A method that returns a list of all the tasks stored in the OrderBook. 
• A method that returns a list of the names of all the programmers with tasks stored in the 
OrderBook. The list should contain each programmer only once. 

Part 3: Listing task owners more efficiently 
In Part 2, you were asked to implement a method to return a list of programmers that are task 
owners. The previous implementation is not efficient since it only prints out the names of the 
programmers without knowing who works on what. Implement a new method that returns a 
dictionary of key-value pairs, with keys corresponding to the names of the different programmers 
and values corresponding to the list of task identifiers that are assigned to them. 

Part 4: Additional features for OrderBook 
Please add the following methods to your OrderBook class definition: 
• A method that takes the id of the task as its argument and marks the relevant task as 
finished. If there is no task for the given id, the method should raise a ValueError 
exception. 
• A method that returns a list of the finished tasks from the OrderBook. 
• A method that returns a list of the unfinished tasks from the OrderBook. 

Part 5: The finishing touches 
Please add a new method to your OrderBook class: status_of_programmer should take the 
name of a programmer and return a tuple. The tuple should contain the number of finished and 
unfinished tasks the programmer has assigned to them, along with the estimated hours in both 
categories. The first item in the tuple should be the number of finished tasks, the second item 
should be the number of unfinished tasks, and the third and fourth items should be the sums of 
workload estimates for the finished and unfinished tasks respectively. If a name is given for a 
programmer that does not exist, the method should raise a ValueError exception. 

Part 6: Putting it all together 
Using the classes you implemented, write a program that for administering the tasks ordered 
from a software company. Your program should consist of a main function that accepts the 
following commands with their corresponding arguments: 
• 0: exit 
• 1: add order 
• 2: list finished tasks 
• 3: list unfinished tasks 
• 4: mark task as finished 
• 5: programmers 
• 6: status of programmer 

Part 7: Handling errors in user input 
To make the application better, you are required to make it recover from erroneous user input. 
Any input which does not follow the specified format should produce The error message 
erroneous input.  

