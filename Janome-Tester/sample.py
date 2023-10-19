from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.tokenfilter import *

text = "蛇の目はPure Ｐｙｔｈｏｎな形態素解析器です。"

t = Tokenizer()
# token_filter = [POSKeepFilter(["名詞"]), LowerCaseFilter()]
# a = Analyzer(tokenizer=t, token_filters=token_filter)

# for token in a.analyze(text):
#     print(token)


phrase = "赤巻紙青巻紙黄巻紙"
analyzer = Analyzer(token_filters=[TokenCountFilter()])
word_count = analyzer.analyze(phrase)
print(word_count)
for _ in word_count:
    print(_)

