from evaluation.hallucination_detector import check_hallucination

def test_hallucination_example():
   response = "API testing checks endpoints and data exchange."
   keywords = ["API", "endpoints", "data"]
   assert not check_hallucination(response, keywords)
