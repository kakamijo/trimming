trimming
====

ディープラーニングの研究などでデータセットを作成する際、二枚一組の画像から、任意の正方形領域を同じ座標で切り出す際に用いる。

## Description
元画像の大きさや切り取り領域の大きさに応じてプログラムの改変を行ってください。  
renameを使い画像の名前を1~nにリネームする。  
trimで切り取る。画像が二枚表示されるので比較しながら切り取りたい部分の左上を左クリック、次に右下を左クリックし右クリックすることで次の画像の組へ進む。
ディスプレイは二枚を推奨。おおまかに選択しても選択領域の中心座標から正方形領域を切り取ることができる。領域サイズの変更はプログラムのf_trimedとr_trimedの改変で可能です。  
  
プログラムの流れとしては、画像読み込み→ディスプレイに収まるサイズにリサイズ→クリックによる座標取得→アフィン変換を用いてリサイズ画像座標から元画像の座標へ変換
→座標の中心を取得→切り取り領域の生成→切り取り　です。
