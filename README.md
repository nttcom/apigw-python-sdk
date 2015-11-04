NTT Communications API SDK(python)
===

このライブラリは、NTT Communications APIsと対話的にアクセスするための簡易的なラッパーを提供します。
各APIの仕様については、[デベロッパーポータル](https://developer.ntt.com/ja)のドキュメントを参照ください。

セットアップ
---

### pip での使用

```
$ pip install apigw
```

システム要件
---

* Python 2.7.x
* Python 3.4.x
※Python 2.7.9 および 3.4.3 で動作検証済

使い方
---

現在、クライアントは

* OAuth API
* Business Process API
* APILog API
* IAM API

の3つのAPIへのアクセスを提供します。

### クライアントの生成

クライアントの生成時には、エンドポイントの情報を記載したJSON形式の設定ファイルへのパスを指定します。

```python
from apigw.client import ApiGWClient

client = ApiGWClient(config_path = '/path/to/config.json', environment = 'development')
```

設定ファイル例:

```json
{
  "development": {
    "host": "ホスト名"(e.g. 'https://api.ntt.com/'),
    "api_version": "APIバージョン"(e.g. 'v1'),
    "timeout": タイムアウト(ms),
    "verify_ssl": SSL証明書の検証を行うか(true / false),
    "debuggable": デバッグ情報を表示するか(true / false)
  }
}
```

※ host と api_version は必須となります。

### アクセストークンの取得

[デベロッパーポータル](https://developer.ntt.com/ja) にて払い出されたコンシューマーキーとシークレットキーを指定します。

```python
response = client.oauth('コンシューマーキー', 'シークレットキー').request_access_token()
access_token = response.json().get('accessToken')
```

全てのAPIのレスポンスは [requests.Response](http://docs.python-requests.org/en/latest/api/#requests.Response) オブジェクトで返却されます。
レスポンスのJSONは `Response#json()` メソッドよりdict形式にパースされたものが取得できます。
各APIのレスポンス仕様については、[デベロッパーポータル](https://developer.ntt.com/ja)のドキュメントを参照ください。

### Business Process API

OAuth API にて取得したアクセストークンとAPIパス、サービス名称を指定します。

```python
response = client.business_process('アクセストークン').get('contracts', 'サービス名称')
items = response.json().get('items')
```

情報の参照には `apigw.business_process.BusinessProcess#get(...)` を、各種オーダには `apigw.business_process.BusinessProcess#post(...)` を利用します。

### APILog API

OAuth API にて取得したアクセストークンと利用履歴の対象日を指定します。

```python
response = client.api_log('アクセストークン').get('日付(YYYYMMDD)')
records = response.json().get('Records')
```

### その他API

exampleファイルを参考にしてください。

ApiBase の継承について
---

新しいAPIに対応したクラスを作成する場合は、`apigw.api_base.ApiBase`のサブクラスを実装します。
以下のドキュメント及び `apigw.business_process.BusinessProcess` や `apigw.api_log.ApiLog` を参考に実装してください。

### 実装が必要なクラスメソッド

#### `api_name()`

APIの名称を返すメソッドです。

`https://api.ntt.com/v1/xxxxxx/yyyyyy` の `xxxxxx` の部分を返します。
例えば `BusinessProcess` では `business-process` 、 `ApiLog` では `apilog` を返すよう実装されています。

api_name をオーバーライドしないと NotImplementedError が発生します。

#### `require_authorization()`

このAPIに認証(アクセストークン)が必要かを返します。デフォルトでは False です。

Trueを返すようにすると、リクエストヘッダーに `Authorization` を自動で付加するようになります。

### リクエスト時に使用するインスタンスメソッド

#### `XXX_request(path, **kwargs)`

`get_request`, `post_request`, `put_request`, `delete_request`, `options_request` の5つが定義されています。
それぞれ GET, POST, PUT, DELETE, OPTIONS のリクエストを実行し、結果を返します。

`path` は `https://api.ntt.com/v1/xxxxxx/yyyyyy` の `yyyyyy` の部分を渡します。
`yyyyyy` に相当するパスがないAPIの場合、 `None` を指定します。

ライセンス
---
Copyright © 2015 NTT Communications  
[Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0)
