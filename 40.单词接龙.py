def ladderLength(self, beginWord, endWord, wordList):
    if beginWord in wordList:
        wordList.remove(beginWord)
    if endWord not in wordList:
        return 0
    min_path = 1
    middle_link_list = [endWord]
    while len(middle_link_list) > 0:
        middle_link_list_tmp = []
        for j in middle_link_list:
            wordList.remove(j)
        for middle_link_word in middle_link_list:
            difference_num = 0
            for k in range(len(middle_link_word)):
                if beginWord[k] != middle_link_word[k]:
                    difference_num += 1
            if difference_num == 1:
                min_path += 1
                return min_path
            else:
                for i in self.findSimilarWord(middle_link_word, wordList):
                    if i not in middle_link_list_tmp:
                        middle_link_list_tmp.append(i)
        if len(middle_link_list_tmp) == 0:
            return 0
        else:
            middle_link_list = middle_link_list_tmp
            min_path += 1


def findSimilarWord(self, word, wordlist):
    middle_wordList = []
    for each_word in wordlist:
        difference_num = 0
        for i in range(len(each_word)):
            if word[i] != each_word[i]:
                difference_num += 1
        if difference_num == 1:
            middle_wordList.append(each_word)
    return middle_wordList
