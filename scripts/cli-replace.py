import argparse
import configparser
import utils
import sys

parser = argparse.ArgumentParser(prog = 'PhonReplace', 
  description='Replace segments in a word list from text file',
  epilog = 'This program was created by Rolando Muñoz Aramburú (Jun-2020)',
  formatter_class = argparse.RawTextHelpFormatter
)

parser.add_argument('-i', '--input-file', required= True, help='path of a text file with a word list')
parser.add_argument('-c', '--config', help='path of config file')
group = parser.add_mutually_exclusive_group()
group.add_argument('-r', '--replace-segment', nargs = 2, action = 'append', help='search segment and replace segment')
group.add_argument('-R', '--replace-table-file', help='A file with two tabs columns: search and replace')
parser.add_argument('--version', action='version', version='%(prog)s 1.0')

args = parser.parse_args()

dict_replace = dict()
if args.replace_segment:
  for replacle_item in args.replace_segment:
    search, replace = replacle_item
    dict_replace[search] = replace

if args.replace_table_file:
  with open(args.replace_table_file, mode = 'r') as f:
    lines = f.readlines()
    for line in lines:
      line = line.rstrip()
      search, replace = line.rsplit(' ', 1)
      dict_replace[search] = replace

# Get values from CONFIG files
configPath = '../config.cfg' if args.config == None else args.config
config = configparser.ConfigParser()
config.read_file(open(configPath))
lst_charGroups = config.get('SETTINGS','complexCharList').split()

# Run command
lst_wordList = utils.get_wordlist_from_raw_text(args.input_file)

utils.replace_segments(lst_wordList = lst_wordList,
 lst_charGroups = lst_charGroups,
 dict_phonReplacement = dict_replace,
 str_sep = ''
)
