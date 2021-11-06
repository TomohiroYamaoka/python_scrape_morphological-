import csv
from janome.tokenizer import Tokenizer
from matplotlib import pyplot as plt
from wordcloud import WordCloud

list = []

# csvファイルを開く
with open('result/hoge.csv') as f:
    # readerにcsvファイルのデータを格納する
    reader = csv.reader(f)
    for row in reader:
        list.append(row[1])

    # 先頭文字を排除
    del list[0]
    b = ""
    for a in reversed(list):
        b += a
    text = "".join(b.splitlines())

    # 初期化
    docs = []
    t = Tokenizer()
    tokens = t.tokenize(text)

    for token in tokens:
        word = token.surface
        partOfSpeech = token.part_of_speech.split(',')[0]
        if partOfSpeech == "名詞" or "形容詞":
            docs.append(word)

    c_word = ' '.join(docs)

    # wordcloud化
    stop_words = ["いい", "感じ", "あっ", "使っ", "あり", "やっ", "する", "いる", "なっ", "でき", "よう", "てる",
                  "思っ", "さん", "こと", "ところ", "ため", "ところ", "みよ", "句点", "が", "です", "の", "て", "です", "です", "は", "まし", "も", "ない", "ます", "し", "で", "し", "なので", "い", "と", "なる", "た", "たい", "ない", "を", "に", "こちら", "な", "ので", "の", "で", "購入", "いつも", "これ", "商品", "ワックス", "髪", "か", "思い", "やすい", "から", "でも", "この", "つけ", "他", "でし", "ません", "され", "とても", "歳", "ません", "the", "it", "and", "I"]

    wordcloud = WordCloud(
        font_path='/Library/Fonts/Arial Unicode.ttf',  # フォントファイルの指定
        background_color="whitesmoke",
        colormap="viridis",
        width=400,
        stopwords=set(stop_words),
        height=200
    ).generate(c_word)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()
