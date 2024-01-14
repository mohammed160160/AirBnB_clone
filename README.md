# AirBnB_clone
This is the first part of the group project in which we were tasked to develop and deploy a simple copy of the AirBnB website. Only implementing some of the major features to cover all fundamental concepts of the higher level programming track.

In this first phase, the objective is to create the model files and the console - to emulate the frontend which we will develop in subsequent phases.

Concepts to learn Include:
Unittest
Python packages concept page
Serialization/Deserialization
*args, **kwargs
datetimeConcepts to learn
More coming soon!

Steps Include:
create your data model
manage (create, update, destroy, etc) objects via a console / command interpreter
store and persist objects to a file (JSON file)
The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between My object and How they are stored and persisted. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you wont have to pay attention (take care) of how your objects are stored.
This abstraction will also allow you to change the type of storage easily without updating all of your codebase.
The console will be a tool to validate this storage engine
