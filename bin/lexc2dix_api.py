from sys import exit
import argparse

def main():
    """Parse the arguments using argparse package"""
    argparser = argparse.ArgumentParser(description='lexc2dix')

    argparser.add_argument("-e", action="store_true", default=False)
    argparser.add_argument("-V", "--version", action="store_true",
                           default=False)

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

def detailed_usage():
    """Detailed documentation of lexc2dix."""
    print("Welcome to the detailed documentation of lexc2dix !")

if __name__ == '__main__':
	main()
