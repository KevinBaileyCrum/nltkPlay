#!/usr/bok]in/env python

import nltk, zipfile, argparse
from nltk.tokenize import word_tokenize
from nltk.corpus import PlaintextCorpusReader

###############################################################################
## Utility Functions ##########################################################
###############################################################################
# This method takes the path to a zip archive.
# It first creates a ZipFile object.
# Using a list comprehension it creates a list where each element contains
# the raw text of the fable file.
# We iterate over each named file in the archive:
#     for fn in zip_archive.namelist()
# For each file that ends with '.txt' we open the file in read only
# mode:
#     zip_archive.open(fn, 'rU')
# Finally, we read the raw contents of the file:
#     zip_archive.open(fn, 'rU').read()
def unzip_corpus(input_file):
    zip_archive = zipfile.ZipFile(input_file)
    try:
        contents = [zip_archive.open(fn, 'rU').read().decode('utf-8')
                for fn in zip_archive.namelist() if fn.endswith(".txt")]
    except ValueError as e:
        contents = [zip_archive.open(fn, 'r').read().decode('utf-8')
                for fn in zip_archive.namelist() if fn.endswith(".txt")]
    return contents



###############################################################################
## Stub Functions #############################################################
###############################################################################
def process_corpus(corpus_name):
    input_file = corpus_name + ".zip"
    corpus_contents = unzip_corpus(input_file)

    # Your code goes here
    print('getting corpus length')
    # print( corpus_contents ) # prints entire list out
    print( len(corpus_contents) ) # list of num titles
    print('first index 0 of corpus_contents '+ corpus_contents[0] )
    print()
    print()

    print('test')
    i = 0
    word_sum = 0
    while i < len( corpus_contents ):
        #print( corpus_contents[i] )
        print(i)
        corp_tok = word_tokenize( corpus_contents[i] )
        word_sum += len( corp_tok )
        i += 1

    print ('word sum %s' % word_sum)


    # corp_tok = [ for text in corpus_contents ]word_tokenize( corpus_contents[0] ) ] # tokenizes
    # print( corp_tok )
    # print( 'corp_tok len %s' % (corp_tok[0].__len__()))

    pass


###############################################################################
## Program Entry Point ########################################################
###############################################################################
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Assignment 1')
    parser.add_argument('--corpus', required=True, dest="corpus", metavar='NAME',
                        help='Which corpus to process {fables, blogs}')

    args = parser.parse_args()

    corpus_name = args.corpus

    if corpus_name == "fables":
        print( "Corpus name: " + corpus_name )
        process_corpus(corpus_name)

    elif corpus_name == "blogs":
        print( "Corpus name: " + corpus_name )
        process_corpus(corpus_name)

    else:
        print("Unknown corpus name: {0}".format(corpus_name))

