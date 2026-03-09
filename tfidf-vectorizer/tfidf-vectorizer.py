import numpy as np
from collections import Counter
import math

def tfidf_vectorizer(documents):
    """
    Build TF-IDF matrix from a list of text documents.
    Returns tuple of (tfidf_matrix, vocabulary).
    """
    n_docs = len(documents)
    tokenized_docs = [doc.lower().split() for doc in documents]
    vocab = sorted(list(set(word for doc in tokenized_docs for word in doc)))

    if not vocab:
        return np.zeros((len(documents), 0)), []

    n_vocab = len(vocab)
    word_to_idx = {word: i for i, word in enumerate(vocab)}
   
    df = Counter()
    for doc_tokens in tokenized_docs:
        unique_tokens = set(doc_tokens)
        for token in unique_tokens:
            df[token] += 1

    idf = np.zeros(n_vocab)
    for i, word in enumerate(vocab):
        idf[i] = math.log(n_docs / df[word])


    tfidf_matrix = np.zeros((n_docs, n_vocab))
    
    for d_idx, doc_tokens in enumerate(tokenized_docs):
        if not doc_tokens:
            continue
            
        counts = Counter(doc_tokens)
        total_terms = len(doc_tokens)
        
        for word, count in counts.items():
            if word in word_to_idx:
                w_idx = word_to_idx[word]
                # tf(t,d) = count / total_terms
                tf = count / total_terms
                tfidf_matrix[d_idx, w_idx] = tf * idf[w_idx]

    return tfidf_matrix, vocab