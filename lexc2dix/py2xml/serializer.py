'''
Py2XML - Python to XML serialization

This code transforms a Python data structures into an XML document

Usage:
    serializer = Py2XML()
    xml_string = serializer.parse(python_object)
    print python_object
    print xml_string
'''

class Py2XML(object):
    def __init__(self):
        self.data = "" # where we store the processed XML string

    def parse(self, python_obj, obj_name=None):
        '''
        processes Python data structure into XML string
        needs obj_name if python_obj is a List
        '''
        if python_obj is None:
            return ""

        if isinstance(python_obj, dict):
            self.data = self.PyDict2XML(python_obj)

        elif isinstance(python_obj, list):
            # we need name for List object
            self.data = self.PyList2XML(python_obj, obj_name)

        else:
            self.data = "<%(n)s>%(o)s</%(n)s>" % {'n':obj_name, 'o':str(python_obj)}

        return self.data

    def PyDict2XML(self, py_dict_obj, obj_name=None):
        '''
        process Python Dict objects
        They can store XML attributes and/or children
        '''
        tag_str = ""     # XML string for this level
        attributes = {} # attribute key/value pairs
        attr_str = ""    # attribute string of this level
        child_str = ""   # XML string of this level's children

        for key, value in py_dict_obj.items():

            if isinstance(value, dict):
                # child tags, with attributes
                child_str += self.PyDict2XML(value, key)

            elif isinstance(value, list):
                # child tags, list of children
                child_str += self.PyList2XML(value, key)

            else:
                # tag could have many attributes, let's save until later
                attributes.update({key:value})

        if obj_name is None:
            return child_str

        # create XML string for attributes
        for key, value in attributes.items():
            attr_str += " %s=\"%s\"" % (key, value)

        # let's assemble our tag string
        if child_str == "":
            tag_str += "<%(n)s%(a)s />" % {'n':obj_name, 'a':attr_str}
        else:
            tag_str += "<%(n)s%(a)s>%(c)s</%(n)s>" % {'n':obj_name, 'a':attr_str, 'c':child_str}

        return tag_str

    def PyList2XML(self, py_list_obj, obj_name=None):
        '''
        Process Python List objects
        They have no attributes, just children
        Lists only hold Dicts or Strings
        '''
        tag_str = ""    # XML string for this level
        child_str = ""  # XML string of children

        for child_obj in py_list_obj:
            if isinstance(child_obj, dict):
                # here's some Magic
                # we're assuming that List parent has a plural name of child:
                # eg, persons > person, so cut off last char
                # name-wise, only really works for one level, however
                # in practice, this is probably ok
                child_str += self.PyDict2XML(child_obj, obj_name[:-1])
            else:
                for string in child_obj:
                    child_str += string

        if obj_name is None:
            return child_str

        tag_str += "<%(n)s>%(c)s</%(n)s>" % {'n':obj_name, 'c':child_str}

        return tag_str
