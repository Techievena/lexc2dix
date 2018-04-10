from sys import exit
import argparse
import lexc2dix.lexc_parser as lp

def main():
    """Parse the arguments using argparse package"""
    argparser = argparse.ArgumentParser(description='lexc2dix')

    argparser.add_argument("-e", action="store_true", default=False)
    argparser.add_argument("-v", "--version", action="store_true",
                           default=False)
    argparser.add_argument("filename", metavar="filename", type=str,
                           nargs='?', default=False)

    args = argparser.parse_args()
    process(args)

def process(args):
    """Process the arguments. Call engine if flags are used."""
    if args.e:
        detailed_usage()
        exit(2)
    if args.version:
        from lexc2dix import release
        print(release.__version__)
        exit(2)
    if args.filename:
        file_read(args.filename)

def detailed_usage():
    """Detailed documentation of lexc2dix."""
    print("A software that parses over the existing lttoolbox format and generates the " +
          "corresponding monolingual dictionary in lttoolbox format. The package is modular and " +
          "is user-friendly with proper help message and usage instructions. \nThis was done as a " +
          "part of coding challenge for the project `Extend lttoolbox to have the power of HFST`." +
          "\n\nUSAGE INSTRUCTIONS:\n\n" +
          "\t$ lexc2dix tests/test_files/apertium-kaz.kaz.lexc\n\n" +
          "For printing results to a file execute the command,\n\n" +
          "\t$ lexc2dix tests/test_files/apertium-kaz.kaz.lexc | tee tests/test_files/apertium-kaz.kaz.dix\n")

def file_read(filename):
    """Read the dictionary file parsed as arguement"""
    filename = str(filename)
    nline = ""
    with open(filename, 'r') as lines:
        for line in lines:
            line = line.rstrip('\n').strip(' ').strip('\t')
            nline += (line+'\n') if (len(line) and not line.startswith('!')) else ''
    lines.close()
    lp.main(nline)

if __name__ == '__main__':
    main()
