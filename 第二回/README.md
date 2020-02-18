# 集合・位相勉強会（第１-2回用）の資料
集合・位相 第1章の資料まとめです．
第４節までは，functionsにある関数等を使っています．
> ## 動作環境
- 特に何も必要ないはず
> ## functions
- __init__.py
    - 使うものまとめ
- operand.py
    - 集合間の演算や写像の判定のまとめ
    - ```union```
        : 和集合
    - ```intersection```
        : 共通部分
    - ```diff```
        : 差集合
    - ```flatten```
        : ネストしたリストをフラットにする
    - ```direct_product```
        : 直積を作る
    - ```power_set```
        : 冪集合を作る
    - `get_equiv_class`
        : 同値関係を作る
    - `is_injective`
        : 単射かどうか判定する
    - `is_surjective`
        : 全射かどうか判定する
    - `is_bijective`
        : 全単射かどうか判定する
    - `is_map`
        : 写像かどうか判定する
     - `is_identity`
        : 恒等写像かどうか判定する
- type_map.py
    - 写像(対応も？)を作るためのクラス`Map`を定義
    - `__init__(values, types='func', A=Set(set([])), B=Set(set([])), init=False)`
        - values: function
        - types: str 'func' で固定
        - A: Set 始集合
        - B: Set 終集合
        - init: bool 終集合をAから作るかどうか
    - `values`
        : 関数を入れる．指定しないとエラー．
    - `param_set`
        : 始集合，終集合を設定
    - `target_init`
        : 終集合を始集合から設定
    - `relations`
        : 対応関係をだす
    - `image`
        : 像，逆像をだす
    - `delta`
        : 逆対応をだす
    - `_inv`
        : 逆対応用の関数定義
    - `inv`
        : 逆対応用の関数
    - `__eq__`
        : 写像同士が等しいかどうか決められる
    - `__call__`
        : 値を入れると写像を飛ばす
    - `__mul__`
        : 写像の合成
- type_set.py
    - 写像や演算に対応させた集合を作るためのクラス`Set`を定義
    - `__init__(values, types='set')`
        - values: set 集合
        - types: str 'set' で固定
    - `__or__`
        : 和集合
    - `__sub__`
        : 差集合
    - `__and__`
        : 共通部分
    - `__mul__`
        : 直積
    - `__pow__`
        : 冪集合
    - `__contain__`
        : 元を包むかどうか
    - `__truediv__`
        : 同値関係で割る．同値類を返す．
    - `__eq__`
        : 同じ集合かどうか
    - `__lt__`, `__gt__`
        : 集合同士の包含関係
    - `__getitem__`
        : 元を取り出す
    - `__len__`
        : 集合の大きさ
    - `__hash__`
        : ハッシャブルにする
    - `__iter__`, `__next__`
        : イテレータとしての挙動


> ## ST*.ipynb
### ST2
- 第1章第二節の資料
    - 共通部分
    - 和集合
    - 差集合
    - ド・モルガンの法則
    - 対称差
    - (アーベル群)
### ST3
- 第1章第三節の資料
    - 元の数
    - 直積
    - 対応
    - 定義域，値域
    - グラフ
    - 逆対応
    - 写像
### ST4
- 第1章第四節の資料
    - 全射・単射・全単射
    - 逆写像
    - 合成写像
    - 恒等写像
