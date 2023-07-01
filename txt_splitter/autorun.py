import os

def split_text_file(file_path, chunk_size):
    # Create a directory to store the split files
    os.makedirs("./Split", exist_ok=True)

    # Read the content of the original file
    with open(file_path, "r") as file:
        content = file.read()

    # Split the content into sentences
    sentences = content.split(". ")

    # Iterate over the sentences and create chunks
    chunks = []
    current_chunk = ""
    for sentence in sentences:
        if len(current_chunk) + len(sentence) <= chunk_size:
            current_chunk += sentence + ". "
        else:
            chunks.append(current_chunk)
            current_chunk = sentence + ". "
    # Add the last chunk
    if current_chunk:
        chunks.append(current_chunk)

    # Save each chunk in a separate file
    for i, chunk in enumerate(chunks):
        file_number = str(i + 1).zfill(2)  # Generate file number with leading zeros
        file_name = f"./Split/split_{file_number}.txt"
        with open(file_name, "w") as chunk_file:
            chunk_file.write(chunk)

# Prompt the user for the file path
file_path = os.environ.get("TXT_FILE")

# Desired chunk size
chunk_size = 4096

# Split the file into chunks
split_text_file(file_path, chunk_size)
