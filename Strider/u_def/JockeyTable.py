
def JockeyTable(df_jockey):

    # 騎手勝率リスト作成 (下記サイト参照)
    # http://www.keibacho.com/rank/rank_kis1.html
    # 短期外人騎手でサイトに載っていない場合は仮で勝率10%とする(中堅騎手レベル)
    jockey_list = [
                    ' 10:グティ',
                    ' 10:コレッ',
                    ' 10:ベハラ',
                    ' 10:フォー',
                    ' 10:メンデ',
                    ' 10:スコフ',
                    ' 10:クリッ',
                    ' 10:ティー',
                    ' 15:ボウマ',
                    ' 10:バルジ',
                    ' 10:ミナリ',
                    ' 10:Ｃオド',
                    ' 10:アヴド',
                    ' 10:プレブ',
                    ' 37:ルメー',
                    ' 33:モレイ',
                    ' 25:ムーア',
                    ' 24:Ｍデム',
                    ' 15:Ｃデム',
                    ' 16:福永祐',
                    ' 16:北村友',
                    ' 15:武　豊',
                    ' 15:浜中俊',
                    ' 12:津村明',
                    ' 12:藤岡佑',
                    ' 11:石橋脩',
                    ' 11:丸山元',
                    ' 11:戸崎圭',
                    ' 11:秋山真',
                    ' 11:三浦皇',
                    ' 10:川田将',
                    ' 10:鮫島駿',
                    ' 10:岩田康',
                    ' 10:横山典',
                    ' 10:Ｆベリ',
                    '  9:田辺裕',
                    '  9:松山弘',
                    '  8:森一馬',
                    '  8:幸英明',
                    ' 13:ビュイ',
                    '  8:北村宏',
                    '  8:松田大',
                    '  8:勝浦正',
                    '  7:大野拓',
                    '  7:池添謙',
                    '  7:吉田隼',
                    '  7:川又賢',
                    '  7:荻野極',
                    '  7:古川吉',
                    '  7:岡田祥',
                    '  6:石神深',
                    '  6:菱田裕',
                    '  6:内田博',
                    '  6:藤田菜',
                    '  6:四位洋',
                    '  6:小坂忠',
                    '  6:横山武',
                    '  6:松若風',
                    '  6:高田潤',
                    '  6:田中健',
                    '  6:高倉稜',
                    '  6:菊沢一',
                    '  5:藤岡康',
                    '  5:国分恭',
                    '  5:中村将',
                    '  5:横山和',
                    '  5:森泰斗',
                    '  5:大江原',
                    '  5:木幡巧',
                    '  5:杉原誠',
                    '  5:酒井学',
                    '  5:伊藤工',
                    '  5:武藤雅',
                    '  5:柴山雄',
                    '  0:蛯名正',
                    '  0:柴田大',
                    '  0:西村淳',
                    '  0:宮崎北',
                    '  0:難波剛',
                    '  0:加藤祥',
                    '  0:阿部龍',
                    '  0:井上俊',
                    '  0:井上敏',
                    '  0:荻野琢',
                    '  0:下原理',
                    '  0:嘉藤貴',
                    '  0:丸田恭',
                    '  0:岩橋勇',
                    '  0:岩崎翼',
                    '  0:岩部純',
                    '  0:義英真',
                    '  0:原田和',
                    '  0:五十冬',
                    '  0:御神本',
                    '  0:江田照',
                    '  0:国分優',
                    '  0:佐原秀',
                    '  0:左海誠',
                    '  0:笹川翼',
                    '  0:鮫島良',
                    '  0:三津谷',
                    '  0:山田敬',
                    '  0:山本聡',
                    '  0:柴田善',
                    '  0:柴田未',
                    '  0:小崎綾',
                    '  0:小牧太',
                    '  0:小林徹',
                    '  0:松岡正',
                    '  0:城戸義',
                    '  0:森裕太',
                    '  0:水口優',
                    '  0:菅原隆',
                    '  0:西村太',
                    '  0:西田雄',
                    '  0:石川裕',
                    '  0:川須栄',
                    '  0:川島信',
                    '  0:村田一',
                    '  0:太宰啓',
                    '  0:黛弘人',
                    '  0:大庭和',
                    '  0:大畑雅',
                    '  0:瀧川寿',
                    '  0:丹内祐',
                    '  0:竹之下',
                    '  0:中井裕',
                    '  0:長岡禎',
                    '  0:的場文',
                    '  0:的場勇',
                    '  0:田村太',
                    '  0:田中勝',
                    '  0:嶋田純',
                    '  0:藤懸貴',
                    '  0:藤原幹',
                    '  0:畑端省',
                    '  0:伴啓太',
                    '  0:繁田健',
                    '  0:富田暁',
                    '  0:武士沢',
                    '  0:木幡育',
                    '  0:木幡初',
                    '  0:野中悠',
                    '  0:和田竜',
                    '  0:服部寿',
                    '  0:服部茂',
                    '  0:桑村真',
                    '  0:岡部誠',
                    '  0:五十嵐',
                    '  0:北沢伸',
                    '  0:金子光',
                    '  0:林満明',
                    '  0:植野貴',
                    '  0:佐藤友',
                    '  0:二本柳',
                    '  0:木幡広',
                    '  0:永島太',
                    '  0:菅原辰',
                    '  0:山本咲',
                    '  0:宮崎光',
                    '  0:永島太',
                    '  0:石川倭',
                    '  0:大柿一',
                    '  0:高松亮',
                    '  0:菅原俊',
                    '  0:大下智',
                    '  0:坂井瑠',
                    '  0:小野寺',
                    '  0:鈴木慶',
                    '  0:白浜雄',
                    '  0:真島大',
                    '  0:山口勲',
                    '  0:佐久間',
                    '  0:江田勇',
                    '  0:田中学',
                    '  0:黒岩悠',
                    '  0:平沢健',
                    '  0:浜野谷',
                    '  0:西谷誠',
                    '  0:山本康',
                    '  0:高野和',
                    '  0:草野太',
                    '  0:蓑島靖',
                    '  0:上野翔',
                    '  0:大山真',
                    '  0:小島太',
                    '  0:中谷雄',
                    '  0:熊沢重',
                    '  0:吉原寛'
                  ]

    #リストサイズ分ループ
    for data in jockey_list:

        # 騎手番号抽出(例 '117:武　豊' → '117')
        jockey_no = str(data)[0:3]
        jockey_no = float(jockey_no.replace( " ", "" )) #空白を削除 & 浮動小数点化

        # 騎手名抽出(例 '117:武　豊' → '武　豊')
        jockey_name = str(data)[4:7]

        # データフレームの騎手名を騎手番号へ置換
        df_jockey = df_jockey.replace( jockey_name, jockey_no )

    # 置換後のデータフレームをリターン
    return df_jockey
