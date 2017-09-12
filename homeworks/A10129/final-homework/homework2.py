# -*- coding: utf-8 -*-

import codecs
import os


def words_split(words):
    new_words = []
    for word in words:
        if '-' in word:
            temp_words = word.split('-')
            new_words.extend(temp_words)
        else:
            new_words.append(word)
    return new_words


# 1. 读取文件
def read_file(file_path):
    f = codecs.open(file_path, 'r', "utf-8")
    lines = f.readlines()
    words = []
    for line in lines:
        #line = line.strip()
        line_words = line.split(" ")
        if len(line_words) > 0:
            line_words = words_split(line_words)
            words.extend(line_words)
    return words


def format_word(word):
    fmt = 'abcdefghijklmnopqrstuvwxyz-'
    for char in word:
        if char not in fmt:
            word = word.replace(char, '')
    return word.lower()


def format_words(words):
    f_words = []
    for word in words:
        new_word = format_word(word)
        if new_word:
            f_words.append(new_word)
    return f_words


def statistics_words(words):
    s_dict = {}
    for word in words:
        if s_dict.has_key(word):
            s_dict[word] = s_dict[word] + 1
        else:
            s_dict[word] = 1
    return s_dict


# 4.输出成csv
def print_to_csv(items_list, to_file_path, total_num):
    nfile = open(to_file_path, 'w+')
    curr_total = 0
    for item in items_list:
        curr_total = curr_total + item[0]
        curr_percent = (float(curr_total) / total_num) * 100

        curr_percent_str = '%0.3f' % (curr_percent)

        nfile.write("%s,%s,%s\n" % (item[1], str(item[0]), curr_percent_str))
    nfile.close()


def get_file_from_folder(folder_path):
    paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            paths.append(file_path)
    print paths
    return paths


def read_files(paths):
    world_words = []
    for path in paths:
        words = read_file(path)
        world_words.extend(words)
    return world_words


def sort_by_value(word_dict):
    items = word_dict.items()
    item_list = [[it[1], it[0]] for it in items]
    item_list.sort(reverse=True)
    return item_list


def main():
    # words = read_file('data1/dt01.txt') # todo:扩展成所有的文件
    words = read_files(get_file_from_folder('data2'))

    f_words = format_words(words)

    total_num = len(f_words)

    word_dict = statistics_words(f_words)

    items_list = sort_by_value(word_dict)

    print_to_csv(items_list, 'output/test.csv', total_num)


if __name__ == "__main__":
    main()

