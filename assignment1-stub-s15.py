#!/usr/bok]in/env python

import nltk, zipfile, argparse, sys, json, codecs
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
    i = 0
    corp_toks = []
    word_sum = 0
    while i < len( corpus_contents ):
        corp_toks += word_tokenize( corpus_contents[i] )
        i += 1
    word_sum=len( corp_toks )

    # print total words
    #   This was found by tokenizing the entire corpus and printing the sum
    print ('Total words in the corpus: %s' % word_sum)


    # open file for part of speech tagging
    #   open file
    #       tokenize sentences
    #       format output note: I added way more newlines then specified,
    #                           I found it to be way more readible
    #   close file
    fpos = codecs.open( corpus_name+"-pos.txt", "w+" , 'utf-8')
    i=0
    out=""
    while i < len( corpus_contents ):
        sentences = nltk.sent_tokenize( corpus_contents[i] )
        for sentence in sentences:
            ptag = nltk.pos_tag( nltk.word_tokenize( sentence ) )
            for token in ptag:
                out+= ("%s/%s "%( token[0] , token[1] ) )
            out+='\n\n'
        out+='\n\n\n\n'
        i+= 1
    fpos.write( out )
    fpos.close()                                     # close file


    # print vocabulary size
    #   the size is determined by the unique words in the set
    #   I only counted the words and not punctuation for
    #   the set hence the use of isalpha()
    vocab =  set (word.lower() for word in corp_toks
                      if word.isalpha() )
    vocab_size = len( vocab )
    print( "The vocabulary size of the corpus is %s"%vocab_size )


    # most frequent part of speech tag using FreqDist
    #   this will use vocab since it is already formatted
    uniq_freq = ( word.lower() for word in corp_toks if word.isalpha() )
    fdist = nltk.FreqDist( uniq_freq )
    print( fdist )
    out =""
    for word, frequency in fdist.most_common( corp_toks.__len__() ):
        out+= ( u'{};{}'.format( word, frequency ) )
        out+= '\n'

    print("the most frequent part of speech tag is: ")

    # open file and do stuff
    ffreq= open( corpus_name+"-word-freq.txt", "w+" ) # opens file
    ffreq.write( out )
    ffreq.close()                                     # close file



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

