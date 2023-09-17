#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 17:51:18 2023

@author: santhoshgunda
"""

from mrjob.job import MRJob
import re

wordregexp = re.compile(r"\w+")

class MRSentenceWordCount(MRJob):

    def mapper(self, _, line):
        # Splitting each sentence into words and emit (word, 1) for each word
        words = wordregexp.findall(line)
        for word in words:
            yield (word.lower(), 1)

    def combiner(self, word, counts):
        # Combining word counts locally before shuffling
        yield (word, sum(counts))

    def reducer(self, word, counts):
        yield (word, sum(counts))

if __name__ == '__main__':
    MRSentenceWordCount.run()

