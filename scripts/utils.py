# Written by Rolando Muñoz (2019-2020)
import phontext

def get_wordlist_from_raw_text(fpath):
  wordList = phontext.WordList()
  return wordList.get_from_raw_text_file(fpath, unique = False)

def mkreport(lst_wordList, str_printf= 'wWsl', lst_charGroups = [], lst_vowels = ['a', 'e', 'i', 'o', 'u']):
  # Report word, cv and len
  par = phontext.PhonParser()
  par.set_complex_chars(lst_charGroups)

  for raw_word in lst_wordList:
    word = par.to_word(raw_word)
    stdout = list()
    for p in str_printf:
      # String output
      if p == 'w':
        stdout.append(raw_word)
      if p == 'W':
        stdout.append(str(word))
      if p == 's':
        word_cv = word.to_cv(lst_vowels)
        stdout.append(word_cv)
      if p == 'l':
        word_len = len(word)
        stdout.append(word_len)
      
    stdout_string = '\t'.join(map(str,stdout))
    if stdout_string == '':
      continue
    print(stdout_string)
    
def get_segments(lst_wordList, lst_charGroups = [], lst_phonInventory = [], display_frequencyColumn = True, display_isInInventoryColumn = False):
  frequency = dict()
  # Report word, cv and len
  par = phontext.PhonParser()
  par.set_complex_chars(lst_charGroups)
  
  for raw_word in lst_wordList:
    word = par.to_word(raw_word)
    for phon in word:
      if phon in frequency:
        frequency[phon] += 1
      else:
        frequency[phon] = 1

  for phon, freq in frequency.items():
    stdout = list()
    stdout.append(phon)
    if display_frequencyColumn:
      stdout.append(freq)
    if display_isInInventoryColumn:
      isInInventory = 'known' if phon in lst_phonInventory else 'unknown'
      stdout.append(isInInventory)

    stdout_string = '\t'.join(map(str,stdout))
    print(stdout_string)

def replace_segments(lst_wordList, lst_charGroups = [], dict_phonReplacement = {'a':'V','i':'V', 'ts':'C', 't':'C'}, str_sep = ''):
  par = phontext.PhonParser()
  par.set_complex_chars(lst_charGroups)
  for raw_word in lst_wordList:
    word = par.to_word(raw_word)
    lst_neword = [dict_phonReplacement[phon] if phon in dict_phonReplacement else phon for phon in word]
    str_neword = str_sep.join(lst_neword)
    print(str_neword)
    
if __name__ == '__main__':
  fpath = "/home/rolando/Documents/nomatsigenga/trabajo_de_campo_2016/wordList.txt"
  complexCharList = ['ts', 'tj']
  vowelList = ['a', 'e', 'i', 'o', 'u', 'ɨ']
  validSegmentList = ['a', 'e', 'i', 'o', 'u', 'ɨ', 'n', 'm', 's', 'w', 'p', 't', 'k', 'b', 'ts', 'h', 'ɾ', 'ʧ', 'tj', 'g', 'ŋ', 'ʃ', 'ɲ', 'd']
  
  wordList = get_wordlist_from_raw_text(fpath)
#  get_segments(wordList, ['ts', 'tj'], ['a', 'á', 'e', 'i', 'Q'], True, True)
#  mkreport(wordList, 'wWls')
#  replace_segments(wordList, str_sep ='')
