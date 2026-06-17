
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

embedding_model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)

def load_policy():

    pdf = fitz.open("policy.pdf")

    text = ""

    for page in pdf:
        text += page.get_text()

    pdf.close()

    return text


def chunk_text(text, chunk_size=500):

    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])

    return chunks



def build_vector_store():

    text = load_policy()

    chunks = chunk_text(text)

    embeddings = embedding_model.encode(
        chunks,
        convert_to_numpy=True
    )

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(
        np.array(embeddings).astype("float32")
    )

    return index, chunks



def search_policy(question):

    index, chunks = build_vector_store()

    query_embedding = embedding_model.encode(
        [question],
        convert_to_numpy=True
    )

    distances, indices = index.search(
        np.array(query_embedding).astype("float32"),
        1
    )

    best_match = chunks[indices[0][0]]

    return best_match


def ai_agent(question):

    
    # Goal
    print("Goal      : Answer user's question")

    # Plan
    print("Planning  : Search enterprise knowledge base")

    # Tool Selection
    print("Tool      : FAISS Semantic Search Tool")

    # Action
    result = search_policy(question)

    # Observation
    print("Observation:")
    print("Relevant document chunk retrieved.")

    # Final Response
    return result

VECTOR_INDEX, DOCUMENT_CHUNKS = build_vector_store()


while True:

    user_question = input("\nYou: ")

    if user_question.lower() == "exit":
        print("\nAgent: Goodbye!")
        break

    answer = ai_agent(user_question)

    print("\nAgent:", answer)
    

