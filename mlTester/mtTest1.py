import sklearn.datasets
import sklearn.svm
import PIL.Image
import numpy
# ユーザが用意した画像ファイルを数値リストに変換する
def imageToData(filename):
    # 画像を8x8のグレースケールに変換
    # ファイルを開いて0~255の値を割り当てる(0を黒,255は白)
    # scikit-learnは16が黒,0が白
    grayImage = PIL.Image.open(filename).convert("L")
    # 8×8にリサイズして、アンチエイリアスをかける(grayImageは画像データ)
    grayImage = grayImage.resize((8,8),PIL.Image.Resampling.LANCZOS)
    # 画像データを数値リストに変換
    numImage = numpy.asarray(grayImage, dtype = float)
    # numImage / 256で色の明るさのパーセンテージを求める
    # 16をかけて16諧調に
    # 色を逆転するために16からその値を引く
    numImage = numpy.floor(16 - 16 * (numImage / 256))
    numImage = numImage.flatten() #多次元配列を１次元配列にする
    return numImage
# 数字を予測する
def predictDigits(data):
    # 学習用データを読み込む
    digits = sklearn.datasets.load_digits()
    # 機械学習する
    clf = sklearn.svm.SVC(gamma = 0.001)
    clf.fit(digits.data, digits.target)
    # 予測結果を表示する
    n = clf.predict([data])
    print("予測=",n)
# ここからがプログラムの本体
data = imageToData("9.png") # 画像ファイルを数値リストに変換する
predictDigits(data) # 数字を予測する