# python-practice

- python3使用
- poetry使用
  - 別途venvを生成しなくてOK

## コマンド

- 起動
  - `poetry run python {ファイルパス}`
- 仮想環境に入る
  - `eval $(poetry env activate)`
- 仮想環境から出る
  - `deactivate`

## package

- requests
  - http通信時につかう
- pyproject-flake8
  - Pythonのコードチェッカー
- black
  - コードフォーマッター
- isort
  - import文の並びを整列させる
- mypy
  - Pythonの型チェックを行う
  - コーディング規約で型ヒントを使うように定義しておく
- pytest
  - テストライブラリ
- playwright
  - ブラウザ自動操作ライブラリ
- flask
  - Webアプリケーションフレームワーク
