# excel⇔JSON 変換サンプル

* エクセルをJSONに変換
* JSONをエクセルに変換
* JSONのネストされたオブジェクトは1セルに押し込まれる
* 1セルに押し込まれたオブジェクトはダブルクォーテーションで括られてしまうのでネストされたオブジェクトに戻らず、1オブジェクトになってしまう
  
## 前提条件

* Python

## はじめに

```sh
pip install pandas
pip install openpyxl
pip install xlrd
```

## 使い方

* エクセルをJSONに変換

```sh
py xlsx-json.py
```

* JSONをエクセルに変換

```sh
py json-xlsx.py
```
