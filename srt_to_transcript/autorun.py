import pysrt
import os

# Get the filename of the SRT file from the user
filename = os.environ.get("SRT_FILE")

# Load the SRT file
subs = pysrt.open(filename)

# Create an empty string to store the transcript
transcript = ''

# Loop through each subtitle and add its text to the transcript
for sub in subs:
    transcript += sub.text + '\n'

# Write the transcript to a file called output.txt
with open('./srt_output.txt', 'w') as f:
    f.write(transcript)

# Print a message to confirm that the transcript was written to the file
print("Transcript has being written")
