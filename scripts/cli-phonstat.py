import argparse
import configparser
import utils
import sys

parser = argparse.ArgumentParser(prog = 'PhonStat', 
  description='Segment statistics from a word list in a file text',
  epilog = 'This program was created by Rolando Muñoz Aramburú (Jun-2020)',
  formatter_class = argparse.RawTextHelpFormatter
)
parser.add_argument('-i', '--input-file', required= True, help='path of a text file with a word list')
parser.add_argument('-c', '--config', help='path of config file')
parser.add_argument('-f', '--frequency', action = 'store_true', help='display frequency of segments')
parser.add_argument('-e', '--check-inventory', action = 'store_true', help='display if the segment belongs to the segment inventory or not')
parser.add_argument('--version', action='version', version='%(prog)s 1.0')

args = parser.parse_args()

configPath = '../config.cfg' if args.config == None else args.config

config = configparser.ConfigParser()
config.read_file(open(configPath))
lst_charGroups = config.get('SETTINGS','complexCharList').split()
lst_phonInventory = config.get('SETTINGS','validSegmentList').split()

# Run command
lst_wordList = utils.get_wordlist_from_raw_text(args.input_file)

utils.get_segments(lst_wordList = lst_wordList,
  lst_charGroups = lst_charGroups,
  lst_phonInventory = lst_phonInventory,
  display_frequencyColumn = args.frequency,
  display_isInInventoryColumn = args.check_inventory
  )
