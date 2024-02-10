### AirBnB Clone

The ALX B&B sums up the implementation of my four months of studies at the ALX School - the fullstack software engineering program. The goal of the project is to deploy a replica of the Airbnb Website using my server. The final version of this project will have:

- A command interpreter to manipulate data without a visual interface, like a shell (for development and debugging)
- A website (front-end) with static and dynamic functionalities
- A comprehensive database to manage the backend functionalities
- An API that provides a communication interface between the front and backend of the system.

## Features

# Command Interpreter

# Description

 The Command Interpreter is used to manage the whole application's functionality from the command line, such as:

- Crete a new object.
- Retrieve an object from a file, database, etc.
- Execute operation on objects. e.g. Count, compute statistics, etc.
- Update object's attributes.
- Destroy an object.

Usage
To launch the console application in interactive mode simply run:

console.py 

or to use the non-interactive mode run:

echo "your-command-goes-here" | ./console.py 

#Commands
Commands	Description	Usage
help or ?	Displays the documented commands.	help
quit	Exits the program.	quit
EOF	Ends the program. Used when files are passed into the program.	N/A
create	Creates a new instance of the <class_name>. Creates a Json file with the object representation. and prints the id of created object.	create <class_name>
show	Prints the string representation of an instance based on the class name and id.	show <class_name class_id>
destroy	Deletes and instance base on the class name and id.	destroy <class_name class_id>
all	Prints all string representation of all instances based or not on the class name	all or all <class_name class_id>
update	Updates an instance based on the class name and id by adding or updating attribute	update <class_name class_id key value>


#Tests
If you wish to run at the test for this application all of the test are located under the test/ folder and can execute all of them by simply running:

python3 -m unittest discover tests 

from the root directory.

#Bugs
No known bugs at this time.
