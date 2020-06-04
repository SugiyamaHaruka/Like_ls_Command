# Like_ls_Command

centosで、linuxのlsコマンド的なものを作りたかった。
実際に利用する方法は以下の通り。

#################################################
$ vi FileList
$ pwd
/home/haruto/PythonTest
$ chmod u+x ~/PythonTest/FileList
$ echo export PATH='$PATH:$HOME/PythonTest/' >> ~/.bashrc
$ source ~/.bashrc
########################################################
