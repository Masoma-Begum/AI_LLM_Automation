def check_hallucination(response: str, expected_keywords: list) -> bool:
   for word in expected_keywords:
       if word.lower() not in response.lower():
           return True  # possible hallucination
   return False
