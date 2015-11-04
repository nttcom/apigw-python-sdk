サンプルスクリプト実行方法
===

前準備
---

```
$ cd /path/to/apigw-lib-python
$ pip install -r requirements.txt
```

example_request-access-token.py
---

アクセストークン取得サンプルスクリプト

```
$ export CONSUMER_KEY=<コンシューマーキー> export SECRET_KEY=<シークレットキー> ./example_request-access-token.py
```

example_get-contracts.py
---

契約一覧取得サンプルスクリプト

```
$ export ACCESS_TOKEN=<アクセストークン> export SERVICE_NAME=<サービス名> ./example_get-contracts.py
```

example_get-api-log.py
---

本日分のAPI Logを取得するサンプルスクリプト

```
$ export ACCESS_TOKEN=<アクセストークン> ./example_get-api-log.py
```
