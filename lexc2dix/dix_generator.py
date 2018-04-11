from xml.dom.minidom import parseString
from lexc2dix.py2xml.serializer import Py2XML

def escape_xml(string_val):
    """Module to escape the characters used in the dictionary for xml format validation"""
    string_val = string_val.replace('&', '&amp;')
    string_val = string_val.replace('"', '&quot;')
    string_val = string_val.replace('<', '&lt;')
    string_val = string_val.replace('>', '&gt;')
    string_val = string_val.replace("'", '&apos;')
    return string_val

class DixGenerator(object):
    """docstring for dix_generator"""
    def __init__(self):
        self.serializer = Py2XML()
        self.sdef_module = ""
        self.pardef_module = ""
        self.section_module = ""

    def sdefs_module_generator(self, multichar_symbols_dict):
        """The module to generate <sdefs> section"""
        m_s_list = []
        for key, value in multichar_symbols_dict.items():
            if not value:
                n_dict = {'n': escape_xml(key)}
            else:
                n_dict = {'n': escape_xml(key), 'c': escape_xml(value)}
            m_s_list.append(n_dict)
        m_s_dict = {'sdefs':m_s_list}
        self.sdef_module = self.serializer.parse(m_s_dict)
        self.sdef_module = parseString(self.sdef_module).toprettyxml()
        self.sdef_module = self.sdef_module.split('\n', 1)[1]

    def pardefs_module_generator(self, lexicons_dict):
        """The module to generate <pardefs> section"""
        lex_list = []
        for key, value in lexicons_dict.items():
            entry_list = []
            for val in value:
                if not val['lemma']:
                    right_entry = []
                else:
                    right_entry = [escape_xml(val['lemma'])]
                for item in val['sdef']:
                    i_obj = {'s': {'n': escape_xml(item)}}
                    i_str = self.serializer.parse(i_obj)
                    right_entry.append(i_str)

                if not val['surface'] and not right_entry:
                    obj = None
                elif not val['surface']:
                    obj = {'r': right_entry}
                elif not right_entry:
                    obj = {'l': [escape_xml(val['surface'])]}
                else:
                    obj = {'l': [escape_xml(val['surface'])], 'r': right_entry}

                x_string = self.serializer.parse(obj) if obj is not None else None

                if x_string is None and not val['paradigm']:
                    ns_dict = None
                elif x_string is None:
                    ns_dict = {'par': {'n': escape_xml(val['paradigm'])}}
                elif not val['paradigm']:
                    ns_dict = {'p': [x_string]}
                else:
                    ns_dict = {'p': [x_string], 'par': {'n': escape_xml(val['paradigm'])}}

                if ns_dict is not None:
                    entry_list.append(ns_dict)
            n_dict = {'n': escape_xml(key), 'es': entry_list}
            lex_list.append(n_dict)
        lex_dict = {'pardefs':lex_list}
        self.pardef_module = self.serializer.parse(lex_dict)
        self.pardef_module = parseString(self.pardef_module).toprettyxml()
        self.pardef_module = self.pardef_module.replace('<es>', '').replace('</es>', '')
        self.pardef_module = self.pardef_module.split('\n', 1)[1]

    def section_module_generator(self, root_lexicon_dict):
        """The module to generate <section> section"""
        entry_list = []
        for key, value in root_lexicon_dict.items():
            for val in value:
                if not val['lemma']:
                    right_entry = []
                else:
                    right_entry = [escape_xml(val['lemma'])]
                for item in val['sdef']:
                    i_obj = {'s': {'n': escape_xml(item)}}
                    i_str = self.serializer.parse(i_obj)
                    right_entry.append(i_str)

                if not val['surface'] and not right_entry:
                    obj = None
                elif not val['surface']:
                    obj = {'r': right_entry}
                elif not right_entry:
                    obj = {'l': [escape_xml(val['surface'])]}
                else:
                    obj = {'l': [escape_xml(val['surface'])], 'r': right_entry}

                x_string = self.serializer.parse(obj) if obj is not None else None

                if x_string is None and not val['paradigm']:
                    ns_dict = None
                elif x_string is None:
                    ns_dict = {'lm': escape_xml(val['surface']), 'par': {'n': escape_xml(val['paradigm'])}}
                elif not val['paradigm']:
                    ns_dict = {'lm': escape_xml(val['surface']), 'p': [x_string]}
                else:
                    ns_dict = {'lm': escape_xml(val['surface']), 'p': [x_string], 'par': {'n': escape_xml(val['paradigm'])}}

                if ns_dict is not None:
                    entry_list.append(ns_dict)
        lex_dict = {'es': entry_list}
        self.section_module = self.serializer.parse(lex_dict)
        self.section_module = parseString(self.section_module).toprettyxml()
        self.section_module = self.section_module.replace('<es>', '<section id=\"main\" type=\"standard\">').replace('</es>', '</section>')
        self.section_module = self.section_module.split('\n', 1)[1]

    def all_module_merger(self):
        """The module to join all the generated sections to yeild the final dix file"""
        dix_file = [self.sdef_module, self.pardef_module, self.section_module]
        separator = '\n'
        dix_file = separator.join(dix_file)
        print(dix_file)
