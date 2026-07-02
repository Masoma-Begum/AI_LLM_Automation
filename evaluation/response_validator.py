def validate_response(response: str) -> bool:
   if not response or len(response) < 20:
       return False
   return True
