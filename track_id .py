import uuid

def generate_track_id():
    """
    Generates a unique track ID for a complaint.
    Format: C-XXXXXX (where XXXXXX is 6 random uppercase alphanumeric characters).
    """
    # Generate a UUID and take the first 6 characters, make uppercase
    random_part = str(uuid.uuid4())[:6].upper()
    return f"C-{random_part}"

# Example usage
track_id = generate_track_id()
print(track_id)  # Output: e.g., "C-A1B2C3"
