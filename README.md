# PhonText (CLI)
A set of command line intefaces for phonology analysis tasks

## Make report
Create a phonetic report from a word list in a text file.

**Get a word list in a text file and display the following columns (in that order): word (w), segmented word (W), cv pattern (s) and word length (l)**

```python3 cli-mkreport.py /home/Desktop/wordList.txt -printf "wWsl"```

**Get a word list in a text file and display the following columns (in that order): segmented word (W) and word length (l)**

```python3 cli-mkreport.py /home/Desktop/wordList.txt -printf "Wl"```

## Phon statistics

Segment statistics from a word list in a text file

**Get all segments in a word list file**

```python3 cli-phonstat.py /home/Desktop/wordList.txt```

**Get all segments and frequency in a word list file**

```python3 cli-phonstat.py /home/Desktop/wordList.txt -f```

**Get all segments, frequency and check if they belong to a segment inventory**

```python3 cli-phonstat.py /home/Desktop/wordList.txt -f```
