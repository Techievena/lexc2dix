from parser import lex, yacc

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

def lexicons_parser(lexicons):
	"""The module to parse Lexicons section"""
	l_p_dict = {}
	for lexicon in lexicons:
		l_p_dict[lexicon.split('\n', 1)[0].split()[1]] = lexicon.split('\n', 1)[1]

def multichar_symbols_formatter(multichar_symbols):
	"""The module to process Multichar_symbols section"""

def root_lexicon_formatter(root_lexicon):
	"""The module to process LEXICON Root section"""

def other_lexicons_formatter(other_lexicons):
	"""The module to parse other LEXICON sections"""

if __name__ == '__main__':
	main()
