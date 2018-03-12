from parser import lex, yacc
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
	l_p = a[1:len(a)-1]
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
	root_lexicon_formatter(l_p_dict)

def multichar_symbols_formatter(multichar_symbols):
	"""The module to process Multichar_symbols section"""
	m_s_dict = {}
	for line in multichar_symbols['Multichar Symbols'].splitlines():
		try:
			m_s_dict[line.split('!')[0].strip().lstrip('%<').rstrip('%>')] = line.split('!')[1].strip()
		except IndexError:
			m_s_dict[line.split('!')[0].strip().lstrip('%<').rstrip('%>')] = ''

	dg.sdefs_module_generator(m_s_dict)

def root_lexicon_formatter(root_lexicon):
	"""The module to process LEXICON Root section"""
	r_l_dict = {}
	for line in root_lexicon['Root'].splitlines():
		r_l_dict[line.split()[-2]] = root_lexicon[line.split()[-2]]
		del root_lexicon[line.split()[-2]]
		other_lexicons_formatter(root_lexicon)

def other_lexicons_formatter(other_lexicons):
	"""The module to parse other LEXICON sections"""
	l_dict = {}

if __name__ == '__main__':
	main()
