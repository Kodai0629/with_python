import MeCab


def print_words_and_results(raw_text: str = 'すもももももももものうち'):
    me = MeCab.Tagger()
    print(me.parse(raw_text))


def print_morpheme(raw_text: str = 'すもももももももものうち'):
    mecab = MeCab.Tagger()
    feature_vector = {}
    node = mecab.parseToNode(raw_text)
    while node:
        surface = node.surface
        meta = node.feature.split(",")
        if meta[0] == ("名詞"):
            feature_vector[surface] = feature_vector.get(surface, 0) + 1
        node = node.next
    print(feature_vector)


if __name__ == '__main__':
    print_words_and_results()
    print('---------')
    print_morpheme()