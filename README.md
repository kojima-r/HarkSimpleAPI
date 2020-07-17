# HarkSimpleAPI
ファイルをアップロードして、各種設定を元に定位と分離を実行するだけのサンプル

requirements
=======
各種コマンド等
```
sox
soxi
hark
hark-python3
```
python パッケージ
```
flask
```

起動
=======
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
```
docker run -it --rm -v ~/HarkSimpleAPI:/hark_api -p 9010:8080 hark:latest^
```

デバッグ等
```
docker run -it --rm -v ~/HarkSimpleAPI:/hark_api --entrypoint "bash" hark:latest"
```
