#!/usr/bok]in/env python

import nltk, zipfile, argparse, sys, json
from nltk.tokenize import word_tokenize, sent_tokenize
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
    corp_toks = []
    word_sum = 0
    while i < len( corpus_contents ):
        print(i)
        corp_toks += word_tokenize( corpus_contents[i] )
        i += 1
    word_sum=len( corp_toks )

    # print total words
    #   This was found by tokenizing the entire corpus and printing the sum
    print ('Total words in the corpus: %s' % word_sum)


    # open file for part of speech tagging
    #   open file
    #       tokenize sentences
    #       format output
    #   close file
    fpos = open( corpus_name+"-pos.txt", "w+" )

    sentences = nltk.sent_tokenize( corpus_contents[0] )
    print( nltk.pos_tag( nltk.word_tokenize(sentences[0]) ) )
    out=""
    for sentence in sentences:
        ptag = nltk.pos_tag( nltk.word_tokenize( sentence ) )
        for token in ptag:
            out+= ("%s/%s "%( token[0] , token[1] ) )
        out+='\n'

    fpos.write( out )
    fpos.close()                                     # close file


    # print vocabulary size
    #   the size is determined by the unique words in the set
    #   I only counted the words and not punctuation for
    #   the set hence the use of isalpha()
    vocab_size = len( set (word.lower() for word in corp_toks
                      if word.isalpha() ) )
    print( vocab_size )

    # open file and do stuff
    f= open( corpus_name+"-word-freq.txt", "w+" ) # opens file

    f.close()                                     # close file



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

