# 词典+最大逆向匹配进行实体识别

def backward_segment(text, dic):
    '''
    额，先实现了依照字典进行逆向最大匹配后分词，然后想办法改成生成BIO， 改进方法是改变字典的存储结构。

    :param text: 待匹配序列
    :param dic: 词典，
    :return:
    '''
    word_list = []
    i = len(text) - 1
    while i >= 0:
        # 以末尾单字作为最大序列
        longest_word = text[i]
        # 待查询的起点是[0:1]
        for j in range(i):
            # 待查询的单词是区间为[j:i]的
            word = text[j : i+1]
            # 如果单词在词典中
            if word in dic:
                # 并且超过了现存最长的词，就把最长的词存进分词列表里
                if len(word) > len(longest_word):
                    longest_word = word
                    break
        # 如果这玩意在词典里，就给你自动打标，其他的打O
        #生成标注序列的方式是从后往前向列表中插入字，但是向文件中写入还没考虑好怎么做比较快
        if longest_word in dic:
            flag = dic[longest_word]
            for _ in range(len(longest_word)-1,0,-1):
                word_list.insert(0, longest_word[_]+' I-'+flag)
            word_list.insert(0,longest_word[0]+' B-'+flag)
        else:
            word_list.insert(0, longest_word+' O')
        i -= len(longest_word)
    return word_list


text = '宫保鸡丁和红烧牛肉哪个好吃'
dic =dict()
dic['宫保鸡丁'] = 'dish'
dic['红烧牛肉'] = 'meal'
backward_segment(text,dic)