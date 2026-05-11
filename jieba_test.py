import jieba
text = "谢明津毕业于西南大学计算机系"
word_list = jieba.lcut(text)
print(word_list)