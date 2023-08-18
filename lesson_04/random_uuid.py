from uuid import uuid4, UUID
# The example of UUID v4

used_uuids: set[UUID] = set()

def generate_unique_uuid() -> UUID:
    while True:
        
        
        generated_uuid = uuid4()
        
        if generated_uuid not in used_uuids:
            used_uuids.add(generated_uuid)
            return generated_uuid
        
print(generate_unique_uuid())
print(generate_unique_uuid())
print(generate_unique_uuid())
print(generate_unique_uuid())
print(generate_unique_uuid())