## サザエさんクイズ（ex01/quiz.py）
### 遊び方
* コマンドラインでquiz.pyを実行すると，標準出力に問題が表示される．
* 標準入力から答えを入力する．
* 正解なら「正解！！！」と表示される．
* 不正解なら「出直してこい」と表示される．
* 正解でも不正解でも，1問䛾み出題される．
### プログラム内䛾解説
* main関数：クイズプログラム䛾全体䛾流れを担当する．
* shutudai関数：ランダムに選んだ問題を出題し，解答をmain関数に返す．
* kaitou関数：回答と正解をチェックし，結果を出力する．