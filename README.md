# iksmproxy

## Description
Splatoon2戦績自動投稿システムになる予定。  
今のところiksm_session自動取得用プロキシサーバ。  
これを起動しているサーバをプロキシに設定しNintendo Switch OnlineのSplatoon2へ接続すると、自動的にiksm_sessionを取得して[splatnet2statink](https://github.com/frozenpandaman/splatnet2statink)の設定ファイルを書き換える。  
アップロードはsplatnet2statinkをモニタリングモードで起動して自動でやってもらう（予定、未実装）。  
プロセスのdaemon化は現状Linux環境のみ（動作未検証）。  

## How to use
### 1. splatnet2statinkをセットアップし、使える状態にしておく  
[splatnet2statink](https://github.com/frozenpandaman/splatnet2statink)を参照。

### 2. iksmproxyの準備
cloneしてくる
```
$ git clone https://github.com/SeiyaTakei/iksmproxy.git
$ cd iksmproxy/
```
依存パッケージのインストールをする。  
現状mitmproxyだけ（な気がする）。
```
$ sudo pip install -r requirements.txt
```
setup.shを実行する。  
実行中splatnet2statinkの場所を聞かれるので、パスを入力してenter。  
```
$ setup.sh
Enter splatnet2statink directory:
```
#### daemon化が必要ないなら
main.pyを実行すればOK。
```
python main.py
```
#### daemon化が必要なら
serviceファイルを然るべき場所へ置く。  
CentOS7系とかならこんなかんじ？
```
$ cd service/
$ sudo cp iksmproxy.service /usr/lib/systemd/system/
```
起動する。
```
$ sudo systemctl start iksmproxy
```
