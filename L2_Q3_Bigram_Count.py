#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 18:12:08 2023

@author: santhoshgunda
"""

from mrjob.job import MRJob

class WordBigramCount(MRJob):
    
    def mapper(self, _, line):
        # Split the input line into words
        words = line.split()
        
        # Emit word bigrams as key-value pairs
        for i in range(len(words) - 1):
            bigram = f"{words[i]},{words[i+1]}"
            yield (bigram, 1)

    def reducer(self, key, values):
        # Sum up the counts for each key (bigram)
        total_count = sum(values)
        yield (key, total_count)

if __name__ == '__main__':
    WordBigramCount.run()
