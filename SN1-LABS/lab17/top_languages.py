# Generate some matplotlib plots to illustrate the world's top 10 languages by number of speakers.
# Intro to Programming 420-SN1
import matplotlib.pyplot as plt

# Some constants / reminders about which columns map to which indices
LANGUAGE = 0 # string; language name
FAMILY   = 1 # string; language family
BRANCH   = 2 # string; language branch / subfamily
L1_N     = 3 # int; number of speakers as a first language
L2_N     = 4 # int; number of speakers as a second language
TOTAL_N  = 5 # int; total speakers

def top_languages_data():
    '''Function that opens and reads the top_languages.csv file.  Convert to list of
lists and returns that data structure. This function is missing two crucial
lines. You must modify this function to make it work!'''
    data=[]
    fp.readline() # skip first line (header line)
    for line in fp:
        line = line.strip().split(",")    # strip off the newline, then split by commas
        for ix in range(L1_N, TOTAL_N+1): # convert our int columns to int data types
            line[ix] = int(line[ix])
        data.append(line)
    fp.close() # close file

def sort_2_lists(source, target):
    '''Sort the source list. Then sort the target list based on ordering of the source
    list. Return both sorted lists. This function works without modification.'''
    ordering = []
    for ix, el in enumerate(source):
        ordering.append((el,ix))
    ordering.sort()
    source_sorted, ix_sorted = zip(*ordering)
    target_sorted = []
    for ix in ix_sorted:
        target_sorted.append(target[ix])
    return source_sorted, target_sorted

# Main section of code. Add your lines of code below to generate the plots
# requested in the lab instructions.
