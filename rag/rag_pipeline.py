from langchain_community.vectorstores import FAISS
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def run_rag(query, documents):
    # Simple mock embedding using TF-IDF (no API needed)
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(documents + [query])

    doc_vectors = vectors[:-1]
    query_vector = vectors[-1]

    scores = cosine_similarity(query_vector, doc_vectors)[0]

    best_doc = documents[scores.argmax()]

    # Mock answer (no LLM)
    return f"Based on context: {best_doc}"