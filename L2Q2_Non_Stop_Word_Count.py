#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 16:45:26 2023

@author: santhoshgunda
"""
from mrjob.job import MRJob
import re

# List of stopwords
stopwords_list = set(["the", "and", "of", "a", "to", "in", "is", "it"])

WORD_RE = re.compile(r"\b\w+\b")

class NonStopWordCount(MRJob):

    def mapper(self, _, line):
        words = re.findall(WORD_RE, line.lower())
        for word in words:
            if word not in stopwords_list:
                yield (word, 1)

    def reducer(self, word, counts):
        yield (word, sum(counts))

if __name__ == '__main__':
    NonStopWordCount.run()



