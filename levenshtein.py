# algo source : https://www.python-course.eu/levenshtein_distance.php

import os
import sys
from data import data


class Levenshtein(object):

    def __init__(self, string_bank=data):
        self.string_bank = string_bank

    def __recursive_distance(self, input_string1, input_string2):
        if input_string1 == "":
            return len(input_string2)
        if input_string2 == "":
            return len(input_string1)
        if input_string1[-1] == input_string2[-1]:
            cost = 0
        else:
            cost = 1
        distance = min([self.__recursive_distance(input_string1[:-1], input_string2) + 1,
                        self.__recursive_distance(
                            input_string1, input_string2[:-1]) + 1,
                        self.__recursive_distance(input_string1[:-1], input_string2[:-1]) + cost])
        return distance

    def __iterative_distance(self, input_string1, input_string2):
        rows = len(input_string1) + 1
        cols = len(input_string2) + 1
        dist = [[0 for x in range(cols)] for x in range(rows)]
        for i in range(1, rows):
            dist[i][0] = i
        for i in range(1, cols):
            dist[0][i] = i
        for col in range(1, cols):
            for row in range(1, rows):
                if input_string1[row - 1] == input_string2[col - 1]:
                    cost = 0
                else:
                    cost = 1
                dist[row][col] = min(dist[row - 1][col] + 1,
                                     dist[row][col - 1] + 1,
                                     dist[row - 1][col - 1] + cost)
        return dist[row][col]

    def get(self, input_string, top_index=10):
        string_score = dict()
        for string in self.string_bank:
            distance = self.__iterative_distance(input_string, string)
            if distance not in string_score.keys():
                string_score[distance] = list()
            string_score[distance].append(string)
        string_list = list()
        score_list = list()
        for score in sorted(string_score.keys()):
            string_list += string_score[score]
            score_list += [score for i in xrange(len(string_score[score]))]
        return zip(string_list[:top_index], score_list[:top_index])


if __name__ == '__main__':
    input_string = ' '.join(sys.argv[1:])
    for i in Levenshtein().get(input_string):
        print i
