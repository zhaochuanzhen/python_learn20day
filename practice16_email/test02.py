import jieba
import jieba.analyse
import jieba.posseg


def dosegment_all(sentence):
    '''
    带词性标注，对句子进行分词，不排除停词等
    :param sentence:输入字符
    :return:
    '''
    print("===================================")
    jieba.load_userdict('f://jieba.dict')
    sentence_seged = jieba.posseg.cut(sentence.strip())
    outstr = ''
    for x in sentence_seged:
        print(x.word)
        outstr += "{}/{},".format(x.word, x.flag)
    # 上面的for循环可以用python递推式构造生成器完成
    # outstr = ",".join([("%s/%s" %(x.word,x.flag)) for x in sentence_seged])
    return outstr


dosegment_all("明天放假了，我很开心，我想看太空学院")
dosegment_all("学数学")
