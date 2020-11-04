#!/usr/bin/python3
""" Module for command interpreter
"""
import cmd
from models.base_model import BaseModel
import models
from models import storage


class HBNBCommand(cmd.Cmd):
    """Class for command interpreter
    """
    prompt = '(hbnb) '
    dict_classes = {"BaseModel": "BaseModel"}

    def do_quit(self, line):
        """ Quit command to exit the program
        """
        quit()

    def do_EOF(self, line):
        """ End of File to exit the program

        Returns:
            true == exit
        """
        print()
        return True

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything
        """
        pass

    def do_create(self, line):
        """Create attribute and save it in Json file

        Args:
            line ([type]): [description]
        """
        if line == "" or line is None:
            print("{}".format("** class name missing **"))
        elif line not in self.dict_classes:
            print("{}".format("** class doesn't exist **"))
        else:
            New = BaseModel()
            New.save()
            print(New.id)

    def do_show(self, line):
        """
        Prints the string representation
        of an instance based on the class name and id
        """
        if line == "" or line is None:
            print("{}".format("** class name missing **"))
        else:
            list_line = line.split(' ')
            if list_line[0] not in self.dict_classes:
                print("{}".format("** class doesn't exist **"))
            elif len(list_line) < 2:
                print("{}".format("** instance id missing **"))
            else:
                objects = storage.all()
                key = "{}.{}".format(list_line[0], list_line[1])
                if key not in objects:
                    print("{}".format("** no instance found **"))
                else:
                    print("{}".format(objects[key]))

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id"""
        if line == "" or line is None:
            print("{}".format("** class name missing **"))
        else:
            list_line = line.split(' ')
            if list_line[0] not in self.dict_classes:
                print("{}".format("** class doesn't exist **"))
            elif len(list_line) < 2:
                print("{}".format("** instance id missing **"))
            else:
                objects = storage.all()
                key = "{}.{}".format(list_line[0], list_line[1])
                if key not in objects:
                    print("{}".format("** no instance found **"))
                else:
                    del objects[key]
                    storage.save()

    def do_all(self, line):
        """ Prints all string representation of all instances
         based or not on the class name """
        objects = storage.all()
        if line != "":
            list_line = line.split(' ')
            if list_line[0] not in self.dict_classes:
                print("{}".format("** class doesn't exist **"))
            else:
                list1 = [str(obj) for key, obj in objects.items()
                         if type(obj).__name__ == list_line[0]]
                print(list1)
        else:
            list1 = [str(obj) for key, obj in objects.items()]
            print(list1)

    def do_update(self, line):
        """ Updates an instance based on the class name and
         id by adding or updating attribute """
        list_line = line.split()
        objects = storage.all()
        if len(list_line) == 0:
            print("{}".format("** class name missing **"))
        elif list_line[0] not in self.dict_classes:
            print("{}".format("** class doesn't exist **"))
        elif len(list_line) == 1:
            print("{}".format("** instance id missing **"))
        # key = "{}.{}".format(list_line[0], list_line[1])
        elif ".".join(list_line[:2]) not in objects:
            print("{}".format("** no instance found **"))
        elif len(list_line) == 2:
            print("{}".format("** atribute name missing **"))
        elif len(list_line) < 4:
            print("{}".format("** value missing **"))
        else:
            key = "{}.{}".format(list_line[0], list_line[1])
            attribute = list_line[2]
            value = list_line[3].strip(' "')
            if value.isdigit():
                value = int(value)
            elif '.' in value:
                float1 = value.split('.')
                if float1[0].isdigit() and float1[1].isdigit():
                    value = float(value)
            dic_obj = objects[key].__dict__
            dic_obj[attribute] = value
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
