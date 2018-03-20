from parser import lex, yacc
import re
import dix_generator as dg

def main():
	"""Main function"""

def dict_split(fileread):
	a = []
	nline = ""
	for line in fileread.splitlines():
		if (not line.startswith('LEXICON')):
			nline += line
		else:
			a.append(nline)
			nline = ""
			nline += line
	m_s = a[0]
	l_p = a[1:]
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

	dg.sdefs_module_generator(m_s_dict)

def root_lexicon_separator(lexicons):
	"""The module to separate LEXICON Root section"""
	r_l_dict = {}
	for line in lexicons['Root'].splitlines():
		try:
			r_l_dict[line.split()[-2]] = lexicons[line.split()[-2]]
		except IndexError:
			print("Invalid lexicons present")
		del lexicons[line.split()[-2]]
	root_lexicon_formatter(r_l_dict)
	other_lexicons_formatter(lexicons)

def root_lexicon_formatter(root_lexicon):
	"""The module to process LEXICON Root section"""
	r_l_dict = {}
	for k, v in root_lexicon.items():
		section_name = k
		for line in v.splitlines():
			line = line.strip(';').strip()
			section_val = re.match(r'(?P<lemma>\w*)(?P<sdef>(%<\w*%>)*):(?P<surface>\w*) (?P<paradigm>\w*)',line).groupdict()
			section_val['sdef'] = section_val['sdef'].replace('%','').replace('<','').replace('>',' ').strip().split()
		r_l_dict[section_name] = section_val
	dg.section_module_generator(r_l_dict)

def other_lexicons_formatter(other_lexicons):
	"""The module to parse other LEXICON sections"""
	l_dict = {}
	for k, v in other_lexicons.items():
		pardef_name = k
		for line in v.splitlines():
			line = line.strip(';').strip()
			pardef_val = re.match(r'(?P<lemma>\w*)(?P<sdef>(%<\w*%>)*):(?P<surface>\w*) (?P<paradigm>\w*)',line).groupdict()
			pardef_val['sdef'] = pardef_val['sdef'].replace('%','').replace('<','').replace('>',' ').strip().split()
		l_dict[pardef_name] = pardef_val
	dg.pardefs_module_generator(l_dict)

if __name__ == '__main__':
	main()
