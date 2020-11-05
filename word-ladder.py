import queue


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        
        begin_q = queue.Queue()
        end_q = queue.Queue()
        
        begin_q.put(beginWord)
        end_q.put(endWord)
        
        word_set = set(wordList)
        
        FROM_BEGIN = 1
        FROM_END = -1
        NOT_VISITED = 0
        # 字母表
        CHAR_LIST = [chr(i) for i in range(97,123)]
        
        word_dict = {word: NOT_VISITED for word in word_set}
        word_dict[beginWord] = FROM_BEGIN
        word_dict[endWord] = FROM_END
        
        step = 2
        
        cur_word = None
        word_len = len(beginWord)
        
        q = begin_q
        flag = FROM_BEGIN
        
        while not q.empty(): 
            temp_q = queue.Queue()
            
            
            while not q.empty():
                cur_word = q.get()
                for i in range(word_len):
                    for c in CHAR_LIST:
                        temp_word = cur_word[0: i] + c + cur_word[i + 1: word_len]
                        if temp_word in word_dict:
                            if word_dict[temp_word] == NOT_VISITED:
                                word_dict[temp_word] = flag
                                temp_q.put(temp_word)
                            elif word_dict[temp_word] != flag:
                                return step
            
            step += 1
            
            if flag == FROM_BEGIN:
                begin_q = temp_q
            else:
                end_q = temp_q
            
            if begin_q.qsize() <= end_q.qsize():
                q = begin_q
                flag = FROM_BEGIN
            else:
                q = end_q
                flag = FROM_END
            
        return 0
            
