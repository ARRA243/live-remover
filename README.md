アプリの概要
ゲーム配信の録画から、ゲーム音を取り除き、配信の声だけを抽出するアプリ。
FPSなどのゲーム音が大切なゲームをやりながら、同じゲームを
プレイしている配信もみたいという要望を叶えることができる。

どんな意図で作ったのか
①エンジニアとして働けるのか、自分の適性を試すために
　自分が欲しいと思うアプリを作成しようと考えた
②ゲーム配信を見ながら、ゲームをするときに感じていた問題を解決したい
③XでYoutubeの音楽からアカペラを作るアプリを見た
④音楽から声を取り除けるなら、その逆をすれば、ゲーム配信から声だけ抽出
　できるのでは
⑤まずは、最低限、動くアプリを作り、その後、コードを1行づつ読み解き
　pythonの理解を深めていく

作成方法
CHATGPTに要件を伝え、コードを出してもらう→pycharmで動くか試す
→エラーがでたら、chatgptに返す→エラーの原因を調べて、改修する

こだわった個所

使用技術・選定理由

今後の課題
・リアルタイムでできていない


・精度が悪い　声も劣化している　完全にゲーム音が取り除けていない
　→spleeterが音楽を前提に作られているから？
　　他の音声分離ソフトを試してみる、
　　音声の学習をゲーム毎や配信者毎にチューニングする
