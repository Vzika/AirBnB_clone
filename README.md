PROJECT DESCRIPTION:

The goal of the project is to deploy on your server a simple copy of the AirBnB website.
this application wooldnt be built all at once, but step by step.

Each step will link to a concept:
FIRST STEP:
The console
create your data model
manage (create, update, destroy, etc) objects via a console / command interpreter
store and persist objects to a file (JSON file)
The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.


Web static
learn HTML/CSS
create the HTML of your application
create template of each object

MySQL storage
replace the file storage by a Database storage
map your models to a table in database by using an O.R.M.

Web framework - templating
create your first web server in Python
make your static HTML file dynamic by using objects stored in a file or database

RESTful API
expose all your objects stored via a JSON web interface
manipulate your objects via a RESTful API

Web dynamic
learn JQuery
load objects from the client side by using your own RESTful API

Storage
Persistency is really important for a web application. It means: every time your program is executed, it starts with all objects previously created from another execution. Without persistency, all the work done in a previous execution won’t be saved and will be gone.

In this project, you will manipulate 2 types of storage: file and database. For the moment, you will focus on file.

Why separate “storage management” from “model”? It’s to make your models modular and independent. With this architecture, you can easily replace your storage system without re-coding everything everywhere.

You will always use class attributes for any object. Why not instance attributes? For 3 reasons:

Provide easy class description: everybody will be able to see quickly what a model should contain (which attributes, etc…)
Provide default value of any attribute
In the future, provide the same model behavior for file storage or database storage

DESCRIPTION OF THE COMMAND INTERPRETER:
COMMANDS			USAGE

Run the console			./console.py
Quit the console		(hbnb) quit
Display the help 
for a command			(hbnb) help <command>
Create an object 
(prints its id)			(hbnb) create <class>
Show an object			(hbnb) show <class> <id> or (hbnb) <class>.show(<id>)
Destroy an object		(hbnb) destroy <class> <id> or (hbnb) <class>.destroy(<id>)
Show all objects, or all instances 
of a class			(hbnb) all or (hbnb) all <class>
Update an attribute of an object (hbnb) update <class> <id> <attribute name> "<attribute value>" or (hbnb) <class>.update(<id>,
				 <attribute name>, "<attribute value>")

Interactive mode (example)
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$

Non-interactive mode (example):
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$

