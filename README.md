# アプリの概要 
・ゲーム配信の録画から、ゲーム音を取り除き、配信の声だけを抽出するアプリ  
・FPSなどのゲーム音が大切なゲームをやりながら、同じゲームを
　プレイしている配信もみたいという要望を叶えることができる

# 導入
・FFmpegのダウンロード　https://ffmpeg.org/download.html  ※環境変数の設定方法に注意  
・pip install -r requirements.txt
・python 3.9で作成

# 使用方法
配信の録画（mp4）をアップロードし、

# どんな意図で作ったのか
 ・エンジニアとして働けるのか、自分の適性を試すために  自分が欲しいと思うアプリを作成しようと考えた  
 ・1から座学よりも、コードを1行毎に読み解いて、その意味や役割を調べるという学習方法の方が  
 　学習のゴールが見えるので、効果的と思った   
　→ChatGPTに要件を伝え、ベースのコードをまず作ってもらう

# 作成のきっかけ  
 ①ゲーム配信を見ながら、ゲームをするときに感じていた問題を解決したい  
 ②XでYoutubeの音楽からアカペラを作るアプリを見た  
 ③音楽から声を取り除けるなら、その逆をすれば、ゲーム配信から声だけ抽出できるのでは  
 
 # 作成方法  
 ①ChatGPTに要件を伝え、コードを作成  
 ②pycharmで動くか試す  
 ③エラーがでたらChatGPTに返して、コードを修正する  

# 今後の課題  
・ダウンロードできない場合がある  
　繰り返すとできるが、原因究明中  
・リアルタイムの配信でできるようにしたい  
　下記を参考にすれば可能か？  
　https://github.com/wakapippi/VocalRemoverWebExtension  
・WEB上にデプロイする  
・声も劣化している　完全にゲーム音が取り除けていない  
　→spleeterが音楽を前提に作られているから？   
　　音声の学習をゲーム毎や配信者毎に用意する
