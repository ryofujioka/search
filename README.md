# search

## 概要
指定されたキーワードを使ってYouTubeの動画を検索し、動画タイトルと動画idを最大50件、リストで出力するスクリプト

## 使い方
1. 設定ファイル(setting.ini)のSETTINGセクションにAPIキーを記述する
1. コマンドラインで下記の要領でスクリプト呼び出し
```
python search 検索キーワード
```

## 出力例
```
python .\search.py ボードゲーム
Videos:(50件)
 【お勧めボードゲーム】 - 多人数プレイ可能ゲームで二人プレイベスト10選 (nHdf-9yS2WA)
【Sapporo 1876】札幌の発展を二人で共に競い合う特徴あるアクション選択の対戦ゲーム / TGG ボードゲーム (XAuXN4-c1lM)
【ボードゲーム】指を賭ける！狂気のじゃんけん【18】 (IMRb6qVO-UE)
今いっっっっちばん叫んでしまうボドゲ『どうぶつ滝くだり』 (lAVDyV-P1X4)
【マニア女が選ぶ】カップル・夫婦におすすめのボードゲーム５選 (mZpk-3etpAs)

~~~
(中略)
~~~

参加自由！ボードゲームアリーナ生配信＃１７　緊急生配信 (8ISdHRUebgI)
【ボードゲーム都市伝説】ボードゲームカフェは今後半分になる？ (bsmLHoW_SRY)
3秒で決着をつけるボードゲームが最高に面白いwww【3秒トライ！】 (BUAXKBJ6TCs)
石器時代でサバイバル！　ボードゲーム「パレオ」をソロで遊ぶ (G26_pr3mYOM)
【神】まさに神ゲー!! 美麗カードゲーム!!【ボードゲームアリーナ】 (foGAd1VTSZA)

スクリプトを終了します
```

## 環境
### 動作環境
Windows10  
python 3.9.5  

### ライブラリ等  
asgiref==3.3.4  
cachetools==5.0.0  
certifi==2021.10.8  
charset-normalizer==2.0.12     
cycler==0.10.0  
Django==3.2.3  
google-api-core==2.5.0  
google-api-python-client==2.37.0  
google-auth==2.6.0  
google-auth-httplib2==0.1.0  
googleapis-common-protos==1.54.0  
httplib2==0.20.4  
idna==3.3  
kiwisolver==1.3.1  
matplotlib==3.4.2  
numpy==1.20.3  
pandas==1.2.4  
Pillow==8.2.0  
protobuf==3.19.4  
pyasn1==0.4.8  
pyasn1-modules==0.2.8  
pyparsing==2.4.7  
python-dateutil==2.8.1  
pytz==2021.1  
requests==2.27.1  
rsa==4.8  
six==1.16.0  
sqlparse==0.4.1  
uritemplate==4.1.1  
urllib3==1.26.8  