import sklearn.datasets
# 行ごとに手書きのデータセットが入ったデータを返す
digits = sklearn.datasets.load_digits()
print("データの個数=",len(digits.images))
print("画像データ=",digits.images[0])
print(type(digits.images[0]))
# digits.targetはそれぞれの画像の正解（=どの数字を表しているか）を示している。
print("何の数字か=",digits.target[0])