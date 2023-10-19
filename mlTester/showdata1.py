import sklearn.datasets
import matplotlib.pyplot as plt
digits = sklearn.datasets.load_digits()
# plt.imshowでデータを画像として表示
plt.imshow(digits.images[0], cmap="Greys")
plt.show()
