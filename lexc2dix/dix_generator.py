from xml.dom.minidom import parseString
from lexc2dix.py2xml.serializer import Py2XML

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
            n_dict = {'c': value, 'n': key}
            m_s_list.append(n_dict)
        m_s_dict = {'sdefs':m_s_list}
        self.sdef_module = self.serializer.parse(m_s_dict)
        self.sdef_module = parseString(self.sdef_module).toprettyxml()

    def pardefs_module_generator(self, lexicons_dict):
        """The module to generate <pardefs> section"""
        lex_list = []
        for key, value in lexicons_dict.items():
            entry_list = []
            for val in value:
                right_entry = [val['lemma']]
                for item in val['sdef']:
                    i_obj = {'s': {'n': item}}
                    i_str = self.serializer.parse(i_obj)
                    right_entry.append(i_str)
                obj = {'l': [val['surface']], 'r': right_entry}
                x_string = self.serializer.parse(obj)
                ns_dict = {'p':[x_string]}
                entry_list.append(ns_dict)
            n_dict = {'n': key, 'es': entry_list}
            lex_list.append(n_dict)
        lex_dict = {'pardefs':lex_list}
        self.pardef_module = self.serializer.parse(lex_dict)
        self.pardef_module = parseString(self.pardef_module).toprettyxml()
        self.pardef_module = self.pardef_module.replace('<es>', '').replace('</es>', '')

    def section_module_generator(self, root_lexicon_dict):
        """The module to generate <section> section"""
        lex_root_list = []
        for key, value in root_lexicon_dict.items():
            entry_list = []

    def all_module_merger(self):
        """The module to join all the generated sections to yeild the final dix file"""
