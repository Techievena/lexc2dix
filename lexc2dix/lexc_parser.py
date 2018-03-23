import re, sys
from lexc2dix.dix_generator import DixGenerator

def main(nline):
    """Main function"""
    dict_split(nline)

def dict_split(fileread):
    """The module to separate multichar symbols and lexicons"""
    file_module = []
    nline = ""
    for line in fileread.splitlines():
        if not line.startswith('LEXICON'):
            nline += line
        else:
            file_module.append(nline)
            nline = ""
            nline += line
    m_s = file_module[0]
    l_p = file_module[1:]
    multichar_symbols_parser(m_s)
    lexicons_parser(l_p)

def multichar_symbols_parser(multichar_symbols):
    """The module to parse Multichar_symbols section"""
    m_s_dict = {}
    m_s_dict[multichar_symbols.split('\n', 1)[0]] = multichar_symbols.split('\n', 1)[1]
    multichar_symbols_formatter(m_s_dict)

def lexicons_parser(lexicons):
    """The module to parse Lexicons section"""
    l_p_dict = {}
    for lexicon in lexicons:
        l_p_dict[lexicon.split('\n', 1)[0].split()[1]] = lexicon.split('\n', 1)[1]
    root_lexicon_separator(l_p_dict)

def multichar_symbols_formatter(multichar_symbols):
    """The module to process Multichar_symbols section"""
    m_s_dict = {}
    for line in multichar_symbols['Multichar Symbols'].splitlines():
        try:
            m_s_dict[line.split('!')[0].strip().lstrip('%<').rstrip('%>')] = line.split('!')[1].strip()
        except IndexError:
            m_s_dict[line.split('!')[0].strip().lstrip('%<').rstrip('%>')] = ''

    D_G.sdefs_module_generator(m_s_dict)

def root_lexicon_separator(lexicons):
    """The module to separate LEXICON Root section"""
    r_l_dict = {}
    for line in lexicons['Root'].splitlines():
        try:
            r_l_dict[line.split()[-2]] = lexicons[line.split()[-2]]
        except IndexError:
            print("Invalid lexicons present!!")
        del lexicons[line.split()[-2]]
    root_lexicon_formatter(r_l_dict)
    other_lexicons_formatter(lexicons)

def root_lexicon_formatter(root_lexicon):
    """The module to process LEXICON Root section"""
    r_l_dict = {}
    for key, value in root_lexicon.items():
        section_name = key
        section_val = []
        for line in value.splitlines():
            line = line.strip(';').strip()
            s_val = re.match(r'(?P<lemma>\w*)(?P<sdef>(%<\w*%>)*):(?P<surface>\w*) (?P<paradigm>\w*)', line).groupdict()
            s_val['sdef'] = s_val['sdef'].replace('%<', '').replace('%>', ' ').strip().split()
            section_val.append(s_val)
        r_l_dict[section_name] = section_val
    D_G.section_module_generator(r_l_dict)

def other_lexicons_formatter(other_lexicons):
    """The module to parse other LEXICON sections"""
    l_dict = {}
    for key, value in other_lexicons.items():
        pardef_name = key
        pardef_val = []
        for line in value.splitlines():
            line = line.strip(';').strip()
            p_val = re.match(r'(?P<lemma>\w*)(?P<sdef>(%<\w*%>)*):(?P<surface>\w*) (?P<paradigm>\w*)', line).groupdict()
            p_val['sdef'] = p_val['sdef'].replace('%<', '').replace('%>', ' ').strip().split()
            pardef_val.append(p_val)
        l_dict[pardef_name] = pardef_val
    D_G.pardefs_module_generator(l_dict)

if __name__ == '__main__':
    D_G = DixGenerator()
    main(sys.argv[1:])
