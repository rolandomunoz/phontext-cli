import phontext
import cmd2
import argparse

class PhonTextCLI(cmd2.Cmd):
  intro = 'PhonText (CLI) version 0.1 (21/Jun/2020) -- "Fly me to the phoneme"\nCopyright (C) Rolando Muñoz Aramburú\n\nType help or ? to list commands.\n'
  '''A simple cmd2 application'''
  prompt = '> '
  
  def __init__(self):
    super().__init__()

    # Make maxrepeats settable at runtime
    self.maxrepeats = 3
    self.add_settable(cmd2.Settable('maxrepeats', int, 'max repetitions for speak command'))
  
  parser_read_wordlist = argparse.ArgumentParser()
  parser_read_wordlist.add_argument('-i', '--input-file', help='The path of the input file')
  
  @cmd2.with_argparser(parser_read_wordlist)
  def do_read_wordlist(self, args):
    '''Read a word list in a plain text file'''
    wordList = phontext.WordList()
    wordList = wordList.get_from_raw_text_file(args.input_file, unique = False)
    self.poutput('\n'.join(wordList))

if __name__ == '__main__':
  import sys

  fpath = "/home/rolando/Documents/nomatsigenga/trabajo_de_campo_2016/wordList.txt"
  complexCharList = ['ts', 'tj']
  vowelList = ['a', 'e', 'i', 'o', 'u', 'ɨ']
  validSegmentList = ['a', 'e', 'i', 'o', 'u', 'ɨ', 'n', 'm', 's', 'w', 'p', 't', 'k', 'b', 'ts', 'h', 'ɾ', 'ʧ', 'tj', 'g', 'ŋ', 'ʃ', 'ɲ', 'd']

  phontext_app = PhonTextCLI()
  sys.exit(phontext_app.cmdloop())
  
#  wordList = get_wordlist_from_raw_text(fpath)
#  get_segments(wordList, ['ts', 'tj'], ['a', 'á', 'e', 'i', 'Q'], True, True)
#  mkreport(wordList, 'wWsl')
#  replace_segments(wordList, str_sep ='')
