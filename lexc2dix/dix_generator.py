from py2xml.serializer import Py2XML
from xml.dom.minidom import parseString

def main():
	"""Main function"""

def sdefs_module_generator(multichar_symbols_dict = {}):
	"""The module to generate <sdefs> section"""
	m_s_list = []
	m_s_dict = {'sdefs':m_s_list}
	for key, value in multichar_symbols_dict.items():
		n_dict = {'c': value, 'n': key}
		m_s_list.append(n_dict)
	serializer = Py2XML()
	sdef_module = serializer.parse(m_s_dict)
	sdef_module = parseString(sdef_module).toprettyxml()

def pardefs_module_generator(lexicons_dict = {}):
	"""The module to generate <pardefs> section"""
	lex_list = []
	lex_list = {'pardefs':lex_list}
	for key, value in lexicons_dict.items():
		n_dict = {'n': ""}

def section_module_generator(root_lexicon_dict = {}):
	"""The module to generate <section> section"""
	print("Section module")

if __name__ == '__main__':
	main()
