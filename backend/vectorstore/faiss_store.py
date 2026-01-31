# backend/vectorstore/faiss_store.py

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import os

class FAISSVectorStore:
    def __init__(self, embedding_model: str, index_path: str):
        self.model = SentenceTransformer(embedding_model)
        self.index_path = index_path
        self.index = None
        self.metadata = []

        if os.path.exists(index_path):
            self.index = faiss.read_index(index_path)
            self.metadata = np.load(index_path + ".meta", allow_pickle=True).tolist()

    def _save(self):
        faiss.write_index(self.index, self.index_path)
        np.save(self.index_path + ".meta", self.metadata)

    def add(self, texts, metadatas):
        embeddings = self.model.encode(texts)
        dim = embeddings.shape[1]

        if self.index is None:
            self.index = faiss.IndexFlatL2(dim)

        self.index.add(embeddings)
        self.metadata.extend(metadatas)
        self._save()

    def search(self, query, top_k=5):
        embedding = self.model.encode([query])
        _, indices = self.index.search(embedding, top_k)

        return [self.metadata[i] for i in indices[0] if i != -1]
