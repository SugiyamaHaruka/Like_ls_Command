#参考にしたサイト
#https://qiita.com/kzkadc/items/e4fc7bc9c003de1eb6d0
#https://note.nkmk.me/python-script-file-path/
#https://myenigma.hatenablog.com/entry/2015/09/23/211656
#https://note.nkmk.me/python-listdir-isfile-isdir/

import os
import argparse

#このプログラムの説明
parser = argparse.ArgumentParser(description='lsコマンドみたいなのを作りました')
#引数を先に宣言しておく
parser.add_argument('--arg1')#,choices=['all', 'dir', 'file'])
#ファイルやディレクトリの情報を取得
CurrentDirectori = os.getcwd()
files = os.listdir(CurrentDirectori)
files_file = [f for f in files if os.path.isfile(os.path.join(CurrentDirectori, f))]
files_dir = [f for f in files if os.path.isdir(os.path.join(CurrentDirectori, f))]
#引数を解析
args = parser.parse_args()



if args.arg1 == 'dir':
    print(' , '.join(files_dir))
elif args.arg1 == 'file':
    print(' , '.join(files_file))
elif args.arg1 == 'all' or args.arg1 == None:
    print(' , '.join(files_file))
    print(' , '.join(files_dir))
else:
    print('error')
