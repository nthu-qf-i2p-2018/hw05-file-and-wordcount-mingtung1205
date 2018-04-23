# -*- coding: utf-8 -*-
import string
import csv
import json
import pickle


def main(filename):
    textfile = open(filename)
    lines = textfile.readlines()
    all_words = []
    for line in lines:
        words = line.split()
        for word in words:
            word = word.strip(string.punctuation)
            if word != (" "):
                all_words.append(word)

    from collections import Counter
    counter = Counter(all_words).most_common()

    
    with open("wordcount.csv", "w") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['word', 'count'])
        writer.writerows(counter)
        csv_file.close()

    with open("wordcount.json", "w") as json_file:
            json.dump(counter, json_file)

    pickle.dump(counter, open("wordcount.pkl", 'wb'))


if __name__ == '__main__':
    main("i_have_a_dream.txt")
