# HarkSimpleAPI
ファイルをアップロードして、各種設定を元に定位と分離を実行するだけのサンプル

requirements
=======
各種コマンド等
```
sox
hark
hark-python3
```

python パッケージ
```
flask
```

編集＋起動
=======
endpointの設定:以下のファイルのendpointを適切に変更する。ローカルの場合はから文字列""にすればよい
- public/index.html
- public/new.html

起動
```
python app.py
```
例えば、
`localhost:8080`
にアクセス

Docker
=======
ビルド
```
docker build -t hark:latest .
```

実行
- マウントするパスは適宜変更
```
docker run -it --rm -d -v /var/app/HarkSimpleAPI:/hark_api -p 9010:8080 hark:latest
```

デバッグ等
```
docker run -it --rm -v ~/HarkSimpleAPI:/hark_api --entrypoint "bash" hark:latest"
```

実行結果
実行すると以下に保存されるので直接URLを指定すればダウンロード・アクセス可能
- public/<プロジェクト名>/log.txt：実行ログ
- public/<プロジェクト名>/original_1ch.wav：1ch分の録音データ
- public/<プロジェクト名>/config：設定ファイル
- public/<プロジェクト名>/original.json：音声ファイルの情報
- public/<プロジェクト名>/sep_files/：音声ファイルの情報
- public/<プロジェクト名>/sep_files/sep_0.wav：分離音ファイル（0から順番に分離ID順に出力される）
- public/<プロジェクト名>/sep_files/sep_0.png：分離音スペクトログラム（0から順番に分離ID順に出力される）



