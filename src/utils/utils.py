"""
Useful helper methods and such...
"""


def split_int(num):
    """
    Returns list of ints in integer num
    """
    return [int(i) for i in str(num)]


def css_pretty_indent(filepath):
    """
    Goes through a css file, following the following indent scheme:  

    .class-name {
        attribute: value;
    }
    .class-name .subclass-name {
        attribute: value;
    }

    .class-name {
        attribute: value;
    }
    """
    try:
        with open(filepath, 'r+') as file:
            linesToRead = True
            while linesToRead:
                line = file.readline()
                if not line:
                    linesToRead = False
                    break
                else:
                    # TODO:
                    #   check if class/id
                    #   brackets
                    #   indent
                    #   attribute: value;
                    #   new class / subclass spacing
                    pass

    except Exception:
        print(f"[ERROR] in css_pretty_indent opening filepath {filepath}")


def post_order(inorder_eq):
    """
    Uses '+', '-', '*', '/', '(', ')', '^'
    """
    ops = ['+', '-', '*', '/', '(', ')', '^']

    pass


def pre_order(inorder_eq):
    """
    Uses '+', '-', '*', '/', '(', ')', '^'
    """
    ops = ['+', '-', '*', '/', '(', ')', '^']
    
    pass
