#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer


def subsample(x):
    """
    Sub-sample the data to plot the first 30ths + last 10ths
    :param x:
    :return:
    """
    return np.hstack((x[:30], x[len(x)-10:]))


def words_distribution(corpus):
    """
    Vectorize text & plot words distribution
    :param corpus:
    :return:
    """
    # Vectorization
    cv = CountVectorizer()
    X = cv.fit_transform(corpus)
    # Compute rank
    # words = cv.get_feature_names_out()
    words = cv.get_feature_names()
    wsum = np.array(X.sum(0))[0]
    ix = wsum.argsort()[::-1]
    wrank = wsum[ix]
    words = [words[i] for i in ix]
    freqs = subsample(wrank)
    ranks = np.arange(len(freqs))
    return ranks, freqs, words


def print_table(result):
    """
    Compute mean & present results in a dataframe
    :param result:
    :return:
    """
    final = {}

    for model in result:
        arr = np.array(result[model])
        final[model] = {
            "name": model,
            "time": arr[:, 0].mean().round(2),
            "f1": arr[:, 1].mean().round(3),
            "recall": arr[:, 2].mean().round(3),
            "precision": arr[:, 3].mean().round(3),
        }

    df = pd.DataFrame.from_dict(final, orient="index").round(3)
    return df
