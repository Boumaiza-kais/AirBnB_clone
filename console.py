#!/usr/bin/python3
"""Class HBNBComand a program called console.py 
that contains the entry point of the command interpreter
"""
import cmd
import shlex
from models import base_model, storage, user, place, state, city, amenity
from models import review
from models.engine import file_storage

BaseModel = base_model.BaseModel
FileStorage = file_storage.FileStorage
User = user.User
Place = place.Place
State = state.State
City = city.City
Amenity = amenity.Amenity
Review = review.Review
NClass = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]


class HBNBCommand(cmd.Cmd):
    """ Command Interpreter
    """
    prompt = "(hbnb) "

    def do_quit(self, args):
        """ quit is command for exit program
        """
        return(True)

    def emptyline(self):
        """ dont perform any action
        """
        pass

    def do_EOF(self, args):
        """EOF command for exit program
        """
        return(True)

    def do_create(self, args):
        """ Creates a new instance of BaseModel
        """
        Arg = shlex.split(args)
        if len(Arg) == 0:
            print("** class name missing **")
        elif len(Arg) == 1 and Arg[0] in NClass:
            new_base_model = eval(Arg[0])()
            new_base_model.save()
            print("{}".format(new_base_model.id))
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
    """
    """
    pass

    def do_destroy(self, args):
    """ Delete instance based on the class name and id
    """
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes_names:
            print("** class doesn't exist **")
        elif not args[1]:
            print("** instance id missing **")
        data = storage.all()

    def do_show(self, args):
    """ Print the string based on the class name and id.
    """
    Arg = shlex.split(args)
        if len(Arg) == 0:
            print("** class name missing **")
        elif len(Arg) >= 1 and Arg[0] not in NClass:
            print("** class doesn't exist **")
        elif len(Arg) == 1:
            print("** instance id missing **")
        else:
            dict = storage.all()
            name_clas = Arg[0] + "." + Arg[1]
            if name_clas in dict:
                print(dict[name_clas])
            else:
                print("** no instance found **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
                        
