from fomc.tools import get_accuracy
import datetime


def test_dict():
    """
    test the classifier based on Sentiment Dict
    """
    print("DictClassifier")
    print("---" * 45)

    from fomc.classifiers import DictClassifier
    ds = DictClassifier()

    # 对一个单句进行情感分析
    # a_sentence = "剁椒鸡蛋好咸,土豆丝很好吃"
    # ds.sentiment_analyse_a_sentence(a_sentence)

    # 对一个文件内语料进行情感分析
    corpus_filepath = "f_corpus/waimai/positive_corpus_v1.txt"
    runout_filepath_ = "f_runout/f_dict-positive_test.txt"
    pos_results = ds.analysis_file(corpus_filepath, runout_filepath_, end=pos_test_num)

    corpus_filepath = "f_corpus/waimai/negative_corpus_v1.txt"
    runout_filepath_ = "f_runout/f_dict-negative_test.txt"
    neg_results = ds.analysis_file(corpus_filepath, runout_filepath_, end=neg_test_num)

    origin_labels = [1] * pos_test_num + [0] * neg_test_num
    classify_labels = pos_results + neg_results

    filepath = "f_runout/Dict-waimai-pt-%d-%d-nt-%d-%d-%s.xls" % (
        pos_train_num, pos_test_num, neg_train_num, neg_test_num,
        datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
    get_accuracy(origin_labels, classify_labels, parameters, filepath)


def test_knn():
    """
    test the classifier based on KNN
    """
    print("KNNClassifier")
    print("---" * 45)

    from fomc.classifiers import KNNClassifier
    # k = [1, 3, 5, 7, 9, 11, 13]
    # k = [21, 25, 29, 33, 37, 41, 45]
    k = 1
    knn = KNNClassifier(train_data, train_labels, k=k, best_words=best_words)

    classify_labels = []

    print("KNNClassifiers is testing ...")
    for data in test_data:
        classify_labels.append(knn.classify(data))
    print("KNNClassifiers tests over.")

    filepath = "f_runout/KNN-waimai-pt-%d-%d-nt-%d-%d-f-%d-k-%d-%s.xls" % (
        pos_train_num, pos_test_num, neg_train_num, neg_test_num, feature_num, k,
        datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))

    get_accuracy(test_labels, classify_labels, parameters, filepath)


def test_bayes():
    """
    test the classifier based on Naive Bayes
    """
    print("BayesClassifier")
    print("---" * 45)

    from fomc.classifiers import BayesClassifier
    bayes = BayesClassifier(train_data, train_labels, best_words)

    classify_labels = []
    print("BayesClassifier is testing ...")
    for data in test_data:
        classify_labels.append(bayes.classify(data))
    print("BayesClassifier tests over.")

    filepath = "f_runout/Bayes-waimai-pt-%d-%d-nt-%d-%d-f-%d-%s.xls" % (
        pos_train_num, pos_test_num, neg_train_num, neg_test_num, feature_num,
        datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))

    get_accuracy(test_labels, classify_labels, parameters, filepath)


def test_maxent_iteration():
    """
    test the classifier based on Maximum Entropy
    """
    print("MaxEntClassifier")
    print("---" * 45)

    from fomc.classifiers import MaxEntClassifier
    maxent = MaxEntClassifier(train_data, train_labels, best_words, max_iter,
                              test=True, test_data=test_data, test_labels=test_labels, what="waimai")


def test_maxent():
    """
    test the classifier based on Maximum Entropy
    """
    print("MaxEntClassifier")
    print("---" * 45)

    from fomc.classifiers import MaxEntClassifier
    maxent = MaxEntClassifier(train_data, train_labels, best_words, max_iter)

    classify_labels = []
    print("MaxEntClassifier is testing ...")
    for data in test_data:
        classify_labels.append(maxent.classify(data))
    print("MaxEntClassifier tests over.")

    filepath = "f_runout/MaxEnt-waimai-pt-%d-%d-nt-%d-%d-f-%d-iter-%d-%s.xls" % (
        pos_train_num, pos_test_num, neg_train_num, neg_test_num, feature_num, max_iter,
        datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))

    get_accuracy(test_labels, classify_labels, parameters, filepath)


def test_svm():
    """
    test the classifier based on Support Vector Machine
    """
    print("SVMClassifier")
    print("---" * 45)

    from fomc.classifiers import SVMClassifier
    svm = SVMClassifier(train_data, train_labels, best_words, C)

    classify_labels = []
    print("SVMClassifier is testing ...")
    for data in test_data:
        classify_labels.append(svm.classify(data))
    print("SVMClassifier tests over.")

    filepath = "f_runout/SVM-waimai-pt-%d-%d-nt-%d-%d-f-%d-C-%d-%s.xls" % (
        pos_train_num, pos_test_num, neg_train_num, neg_test_num, feature_num, C,
        datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))

    get_accuracy(test_labels, classify_labels, parameters, filepath)


def test_waimai_multiple_classifiers():
    """
    test the Fusion of Multiple Classifiers
    """
    print("Fusion of Multiple Classifiers")
    print("---" * 45)

    from fomc.classifiers import WaiMaiMultipleClassifiers

    # get the instance of classifiers
    # prob = False
    prob = True
    knn = False

    mc = WaiMaiMultipleClassifiers(train_data, train_labels, best_words, max_iter, C, knn)

    print("WaiMaiMultipleClassifiers is testing ...")
    classify_labels = []
    for data in test_data:
        classify_labels.append(mc.classify(data, prob))

    print("WaiMaiMultipleClassifiers tests over.")

    filepath = "f_runout/Multiple-waimai-pt-%d-%d-nt-%d-%d-iter-%d-C-%d-knn-%s-prob-%s-%s.xls" % (
        pos_train_num, pos_test_num, neg_train_num, neg_test_num, max_iter, C,  "True" if knn else "False",
        "True" if prob else "False", datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))

    get_accuracy(test_labels, classify_labels, parameters, filepath)


def test_waimai_multiple_classifiers2():
    """
    test the Fusion of Multiple Classifiers
    """
    print("Fusion of Multiple Classifiers")
    print("---" * 45)

    from fomc.classifiers import WaiMaiMultipleClassifiers2

    # get the instance of classifiers
    mc = WaiMaiMultipleClassifiers2(train_data, train_labels, best_words, max_iter, C)

    print("WaiMaiMultipleClassifiers is testing ...")
    classify_labels = []
    for data in test_data:
        classify_labels.append(mc.classify(data))

    print("WaiMaiMultipleClassifiers tests over.")

    filepath = "f_runout/Multiple2-waimai-pt-%d-%d-nt-%d-%d-iter-%d-C-%d--%s.xls" % (
        pos_train_num, pos_test_num, neg_train_num, neg_test_num, max_iter, C,
        datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))

    get_accuracy(test_labels, classify_labels, parameters, filepath)


def test_waimai_multiple_classifiers3():
    """
    test the Fusion of Multiple Classifiers
    """
    print("Fusion of Multiple Classifiers")
    print("---" * 45)

    from fomc.classifiers import WaiMaiMultipleClassifiers

    # get the instance of classifiers
    # prob = False
    prob = True
    knn = True

    mc = WaiMaiMultipleClassifiers(train_data, train_labels, best_words, max_iter, C, knn)

    print("WaiMaiMultipleClassifiers is testing ...")
    classify_labels = []
    for data in test_data:
        classify_labels.append(mc.classify(data, prob))

    print("WaiMaiMultipleClassifiers tests over.")

    filepath = "f_runout/Multiple3-waimai-pt-%d-%d-nt-%d-%d-iter-%d-C-%d-knn-%s-prob-%s-%s.xls" % (
        pos_train_num, pos_test_num, neg_train_num, neg_test_num, max_iter, C,  "True" if knn else "False",
        "True" if prob else "False", datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))

    get_accuracy(test_labels, classify_labels, parameters, filepath)


def test_waimai_multiple_classifiers4():
    """
    test the Fusion of Multiple Classifiers
    """
    print("Fusion of Multiple Classifiers")
    print("---" * 45)

    from fomc.classifiers import WaiMaiMultipleClassifiers3

    # get the instance of classifiers
    # prob = False

    mc = WaiMaiMultipleClassifiers3(train_data, train_labels, best_words, max_iter, C)

    print("WaiMaiMultipleClassifiers is testing ...")
    classify_labels = []
    for data in test_data:
        classify_labels.append(mc.classify(data))

    print("WaiMaiMultipleClassifiers tests over.")

    filepath = "f_runout/Multiple4-waimai-pt-%d-%d-nt-%d-%d-iter-%d-C-%d-%s.xls" % (
        pos_train_num, pos_test_num, neg_train_num, neg_test_num, max_iter, C,
        datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))

    get_accuracy(test_labels, classify_labels, parameters, filepath)


def test_waimai_multiple_classifiers5():
    """
    test the Fusion of Multiple Classifiers
    """
    print("Fusion of Multiple Classifiers")
    print("---" * 45)

    from fomc.classifiers import WaiMaiMultipleClassifiers4

    # get the instance of classifiers
    # prob = False

    mc = WaiMaiMultipleClassifiers4(train_data, train_labels, best_words, max_iter, C)

    print("WaiMaiMultipleClassifiers is testing ...")
    classify_labels = []
    for data in test_data:
        classify_labels.append(mc.classify(data))

    print("WaiMaiMultipleClassifiers tests over.")

    filepath = "f_runout/Multiple5-waimai-pt-%d-%d-nt-%d-%d-iter-%d-C-%d-%s.xls" % (
        pos_train_num, pos_test_num, neg_train_num, neg_test_num, max_iter, C,
        datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))

    get_accuracy(test_labels, classify_labels, parameters, filepath)


if __name__ == "__main__":
    pos_train_num = neg_train_num = 3500
    pos_test_num = neg_test_num = 1000
    feature_num = 4000
    max_iter = 50
    C = 20
    ratio = 0.5
    parameters = [pos_train_num, neg_train_num, pos_test_num, neg_test_num, feature_num]

    # get the f_corpus
    from fomc.corpus import WaimaiCorpus

    corpus = WaimaiCorpus()
    train_data, train_labels = corpus.get_train_corpus(pos_train_num, neg_train_num)
    test_data, test_labels = corpus.get_test_corpus(pos_test_num, neg_test_num)

    # feature extraction
    from fomc.feature_extraction import ChiSquare

    fe = ChiSquare(train_data, train_labels)
    best_words = fe.best_words(feature_num)

    # test f_dict
    # test_dict()

    # test knn
    # test_knn()

    # test bayes
    # test_bayes()

    # test maxent
    # test_maxent()
    # test_maxent_iteration()

    # test SVM
    # test_svm()

    # test multiple_classifiers
    # test_waimai_multiple_classifiers()
    # test_waimai_multiple_classifiers2()
    # test_waimai_multiple_classifiers3()
    # test_waimai_multiple_classifiers4()
    test_waimai_multiple_classifiers5()
