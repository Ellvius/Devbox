import uuid

def generate_uuid(length: int = 6) -> str:
    return uuid.uuid4().hex[:length]