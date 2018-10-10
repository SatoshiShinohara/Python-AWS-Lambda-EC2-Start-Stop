# python-aws-lambda-ec2-start-stop

## 概要
特定のタグ・値を付与していないEC2インスタンスに対して、AWS CloudWatch Eventsから起動・停止を実行する。

## 要求仕様
AWS Lambda Python 3.6

## 使い方
1. 本スクリプトで起動・停止したくないインスタンスに特定のタグと値を設定する。
2. AWS Lambdaの関数に本スクリプトを登録する。
3. AWS CloudWatch Eventsに起動イベント・停止イベントを作成し、定数に以下を指定する。

#### 起動
``` json
{"Action": "start", "Region": "ap-northeast-1", "Tag": "NoStartStop", "Value": "true"}
```

#### 停止
``` json
{"Action": "stop", "Region": "ap-northeast-1", "Tag": "NoStartStop", "Value": "true"}
```
