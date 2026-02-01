import faiss
import numpy as np
import os
import threading
from sentence_transformers import SentenceTransformer

# 🔒 singleton embedding model (important for FastAPI)
_model = None
_model_lock = threading.Lock()

def get_embedding_model(name: str):
    global _model
    if _model is None:
        with _model_lock:
            if _model is None:
                print("🧠 Loading embedding model:", name)
                _model = SentenceTransformer(name)
    return _model


class FAISSVectorStore:
    def __init__(self, embedding_model: str, index_path: str):
        self.model = get_embedding_model(embedding_model)
        self.index_path = index_path
        self.index = None
        self.metadata = []

        if os.path.exists(index_path):
            print("📂 Loading FAISS index:", index_path)
            self.index = faiss.read_index(index_path)

            meta_path = index_path + ".meta.npy"
            if os.path.exists(meta_path):
                self.metadata = np.load(meta_path, allow_pickle=True).tolist()
                print(f"📦 Loaded {len(self.metadata)} metadata rows")

    def _save(self):
        faiss.write_index(self.index, self.index_path)
        np.save(self.index_path + ".meta.npy", self.metadata)

    def add(self, texts):
        if not texts:
            return

        embeddings = self.model.encode(texts)
        embeddings = np.array(embeddings).astype("float32")  # 🔥 CRITICAL

        if self.index is None:
            self.index = faiss.IndexFlatL2(embeddings.shape[1])

        self.index.add(embeddings)

        for t in texts:
            self.metadata.append({"text": t})

        self._save()

    def search(self, query, top_k=5):
        if self.index is None or self.index.ntotal == 0:
            print("⚠️ FAISS index empty")
            return []

        q_emb = self.model.encode([query])
        q_emb = np.array(q_emb).astype("float32")  # 🔥 CRITICAL

        distances, indices = self.index.search(q_emb, top_k)

        print("🔎 FAISS distances:", distances)
        print("🔎 FAISS indices:", indices)

        results = []
        for i in indices[0]:
            if i < len(self.metadata):
                results.append(self.metadata[i]["text"])

        return results

    def search_with_scores(self, query, top_k=5):
        if self.index is None:
            return []

        q_emb = self.model.encode([query])
        distances, indices = self.index.search(q_emb, top_k)

        results = []
        for i, idx in enumerate(indices[0]):
            if idx < len(self.metadata):
                results.append(
                    (self.metadata[idx]["text"], float(distances[0][i]))
                )

        return results
