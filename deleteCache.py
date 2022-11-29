import glob
import os
import datetime
import send2trash
import pprint

today = datetime.datetime.today()
futureDate = today - datetime.timedelta(days=90)
print("Delete caches with last access date before " + str(futureDate))
# ~/Library/Caches/**/*
files = glob.glob("/Users/oguranaoki/Library/Caches/**/*")

deleteList = []
falseList = []
for file in files:
    if os.path.exists(file):
        fileDate = datetime.datetime.fromtimestamp(os.path.getatime(file))
        if (fileDate < futureDate):
            send2trash.send2trash(file)
            deleteList.append(file)
        else:
            falseList.append(file)

# print("deleteList --------------------------------------------------")
# pprint.pprint(deleteList)
# print("falseLiset --------------------------------------------------")
# pprint.pprint(falseList)

# 改行を挿入
deleteList_lf = '\n'.join(deleteList)
falseList_lf = '\n'.join(falseList)

# Documentsに移動
path = os.path.expanduser('~')
os.chdir(path + '/Documents')

# ログにdelteListとfalseListの内容を上書きモードで記述
with open('deleteCache.log','w') as f:
    f.write('deleteList ----------\n')
    f.write(deleteList_lf)
    f.write('falseList ----------\n')
    f.write(falseList_lf)
