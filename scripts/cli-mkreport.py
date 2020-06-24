import argparse
import configparser
import utils
import sys

parser = argparse.ArgumentParser(prog = 'mkreport', 
  description='Create a phonetic report from a word list in a file text',
  epilog = 'This program was created by Rolando Muñoz Aramburú (Jun-2020)',
  formatter_class = argparse.RawTextHelpFormatter
)
parser.add_argument('-i', '--input-file', required= True, help='path of a text file with a word list')
parser.add_argument('-c', '--config', help='path of config file', action='store')
parser.add_argument('-p', '--printf', default='W',
  help="print columns format\n"
  " w = display word as in the word list file\n"
  " W = display segmented word\n"
  " s = display cv pattern\n"
  " l = display number of segments\n"
  )
parser.add_argument('--version', action='version', version='%(prog)s 1.0')

args = parser.parse_args()

configPath = '../config.cfg' if args.config == None else args.config

config = configparser.ConfigParser()
config.read_file(open(configPath))
complexCharList = config.get('SETTINGS','complexCharList').split()
vowelList = config.get('SETTINGS','vowelList').split()
validSegmentList = config.get('SETTINGS','validSegmentList').split()

lst_wordList = utils.get_wordlist_from_raw_text(args.input_file)
utils.mkreport(lst_wordList = lst_wordList,
  str_printf = args.printf,
  lst_charGroups = complexCharList,
  lst_vowels = vowelList
  )
