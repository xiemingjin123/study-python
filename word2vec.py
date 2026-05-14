from gensim.models import KeyedVectors

model_path = 'sgns.sikuquanshu.word.bz2'
model = KeyedVectors.load_word2vec_format(model_path)
print(model['地铁'])
