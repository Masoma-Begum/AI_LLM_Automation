from rag.rag_pipeline import run_rag

def test_rag_api_answer():
   docs = ["API testing ensures that endpoints respond correctly."]
   query = "What is API testing?"
   answer = run_rag(query, docs)
   assert "API" in answer
