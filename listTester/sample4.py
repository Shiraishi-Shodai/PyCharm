# 実習などで作成したプロジェクトのパス一覧
path1 = 'c:\\python\\project_a\\syntax_prog'
path2 = 'c:\\home\\takahashi\\program\\draw2'
path3 = 'c:\\java\\stringtest'
# 文字列をsplitで分割してリストに入れる
list1 = path1.split('\\')
list2 = path2.split('\\')
list3 = path3.split('\\')
# フォルダの最後のフォルダを表示するようにしてください
print(list1[-1]) # syntax_progが表示されるようにする
print(list2[-1]) # draw2が表示されるようにする
print(list3[-1]) # stringtestが表示されるようにする
