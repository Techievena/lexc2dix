from xml.dom.minidom import parseString
from lexc2dix.py2xml.serializer import Py2XML

def main():
    """Main function"""

def sdefs_module_generator(multichar_symbols_dict):
    """The module to generate <sdefs> section"""
    m_s_list = []
    m_s_dict = {'sdefs':m_s_list}
    serializer = Py2XML()
    for key, value in multichar_symbols_dict.items():
        n_dict = {'c': value, 'n': key}
        m_s_list.append(n_dict)
    sdef_module = serializer.parse(m_s_dict)
    sdef_module = parseString(sdef_module).toprettyxml()

def pardefs_module_generator(lexicons_dict):
    """The module to generate <pardefs> section"""
    lex_list = []
    lex_dict = {'pardefs':lex_list}
    serializer = Py2XML()
    for key, value in lexicons_dict.items():
        entry_list = []
        n_dict = {'n': key, 'es': entry_list}
        for val in value:
            left_entry = [val['surface']]
            right_entry = [val['lemma']]
            for item in val['sdef']:
                i_obj = {'s': {'n': item}}
                i_str = serializer.parse(i_obj)
                right_entry.append(i_str)
            obj = {'l': left_entry, 'r': right_entry}
            x_string = serializer.parse(obj)
            ns_dict = {'p':[x_string]}
            entry_list.append(ns_dict)
        lex_list.append(n_dict)
    pardef_module = serializer.parse(lex_dict)
    pardef_module = parseString(pardef_module).toprettyxml()
    pardef_module = pardef_module.replace('<es>', '').replace('</es>', '')

def section_module_generator(root_lexicon_dict):
    """The module to generate <section> section"""
    lex_root_list = []

def all_module_merger(sdef_module, pardef_module, section_module):
    """The module to join all the generated sections to yeild the final dix file"""

if __name__ == '__main__':
    main()
