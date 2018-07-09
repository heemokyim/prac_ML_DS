import os
from pprint import pprint


def get_file_list(dir_name):
    return os.listdir(dir_name)


def get_contents(file_list):
    y_class = []
    X_text = []
    class_dict = {
        1: "0", 2: "0", 3: "0", 4: "0", 5: "1", 6: "1", 7: "1", 8: "1"
    }

    for file_name in file_list:
        try:
            f = open(file_name, "r", encoding="cp949")
            category = int(file_name.split(os.sep)[1].split("_")[0])
            y_class.append(class_dict[category])
            X_text.append(f.read())
            f.close()
        except UnicodeDecodeError as e:
            print(e)
            print(file_name)

    return X_text, y_class


def get_cleaned_text(word):
    import re
    # word.lower() 에 대해서 특수문자(\W+)를 '' 로 바꾼다
    word = re.sub('\W+', '', word.lower())
    return word


def get_corpus_dict(text):
    text = [sentence.split() for sentence in text]
    cleaned_words = [get_cleaned_text(word) for words in text for word in words]

    from collections import OrderedDict
    corpus_dict = OrderedDict()
    for i, v in enumerate(set(cleaned_words)):
        corpus_dict[v] = i
    
    return corpus_dict


def get_count_vector(text, corpus):
    text = [sentence.split() for sentence in text]
    word_number_list = [
        [corpus[get_cleaned_text(word)] for word in words]
        for words in text
    ]

    X_vector = [
        [0 for _ in range(len(corpus))]
        for x in range(len(text))
    ]

    for i, text in enumerate(word_number_list):
        for word_number in text:
            X_vector[i][word_number] += 1
    
    return X_vector

import math
def get_cosine_similarity(v1, v2):
    """
    computer cosine similarity of v1 to v2
    (v1 dot v2 / (|v1||v2|))
    """
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]
        y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return sumxy / math.sqrt(sumxx * sumyy)


def get_similarity_score(X_vector, source):
    source_vector = X_vector[source]
    similarity_list = []
    for target_vector in X_vector:
        similarity_list.append(
            get_cosine_similarity(source_vector, target_vector)
        )
    return similarity_list


def get_top_n_similarity_news(similarity_score, n):
    import operator
    x = {i:v for i, v in enumerate(similarity_score)}
    sorted_x = sorted(x.items(), key=operator.itemgetter(1))

    return list(reversed(sorted_x))[1: n+1]


if __name__ == "__main__":
    dir_name = "d:/prac_ML_DS/ML/python-for-ml/practice/04_case_study/news_data"
    file_list = get_file_list(dir_name)
    file_list = [os.path.join(dir_name, file_name) for file_name in file_list]
    #pprint(file_list)
    #print(len(file_list))

    cnt = 0
    X_text, y_class = get_contents(file_list)

    corpus_dict = get_corpus_dict(X_text)
    #pprint(corpus_dict)
    print("Number of corpus dict : %d" % len(corpus_dict))
    # 이것 사이즈만큼 bag vector size를 해야함
    '''
    for file_path, file_text, category in zip(file_list, *get_contents(file_list)):
        print("\n\n#################################################")
        print(file_path, ":", category)
        print("#################################################\n\n")
        print(file_text)
    '''

    x_vector = get_count_vector(X_text, corpus_dict)
    #print(x_vector)

    simil_list = get_similarity_score(x_vector, 10)
    sorted_simil_list = get_top_n_similarity_news(simil_list, 10)
    
    for i, v in enumerate(sorted_simil_list):
        print(i, v)





