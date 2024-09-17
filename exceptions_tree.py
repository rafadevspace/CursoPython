def print_exceptions_hierarchy(excepions_class, indent=0):
    print(' ' * indent + excepions_class.__name__)
    for subclass in excepions_class.__subclasses__():
        print_exceptions_hierarchy(subclass, indent + 4)

print_exceptions_hierarchy(Exception)