# PhonText (CLI)
A set of command line intefaces for phonology analysis tasks

## Report command
Create a phonetic report from a word list in a text file.

Get a word list in a text file and display the following columns (in that order): word (w), segmented word (W), cv pattern (s) and word length (l)

```python3 cli-mkreport.py -i /home/Desktop/wordList.txt -printf "wWsl"```

Get a word list in a text file and display the following columns (in that order): segmented word (W) and word length (l)

```python3 cli-mkreport.py -i /home/Desktop/wordList.txt -printf "Wl"```

## Segment statistics command

Segment statistics from a word list in a text file

Get all segments in a word list file

```python3 cli-phonstat.py -i /home/Desktop/wordList.txt```

Get all segments and their frequency in a word list file

```python3 cli-phonstat.py -i /home/Desktop/wordList.txt -f```

Get all segments, frequency and check if they belong to a segment inventory

```python3 cli-phonstat.py -i /home/Desktop/wordList.txt -f```

## Search and replace command

Replace the vowel **a** by **V**

```python3 cli-replace.py -i /home/Desktop/wordList.txt -r "a" "V"```

Replace the vowels **a** and **i** by **V**

```python3 cli-replace.py -i /home/Desktop/wordList.txt -r "a" "V" -r "i" "V"```

Use a tab table for searching and replacing segments (the firs column is the search segment and the second, the replace segment)

```python3 cli-replace.py -i /home/Desktop/wordList.txt -R /home/Desktop/replace-table.txt```


