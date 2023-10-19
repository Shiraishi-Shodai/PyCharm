import sklearn.datasets
import matplotlib.pyplot as plt
digits = sklearn.datasets.load_digits()
for i in range(100):
    # #5×20の要素の内に１番目の要素に配置する
    plt.subplot(5, 20, i + 1)
    # 枠線を非表示
    plt.axis("off")
    plt.title(digits.target[i])
    # imshowの引数cmapを指定することで、カラーマップを変更することができます。ここでは、グレースケールで表示するために、cmap='Greys'としています。
    # デフォルト値はcmap='viridis'です。
    plt.imshow(digits.images[i], cmap="Greys")
plt.show()