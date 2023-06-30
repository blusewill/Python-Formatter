import pysrt

# Get the filename of the SRT file from the user
filename = srt_file

# Load the SRT file
subs = pysrt.open(filename)

# Create an empty string to store the transcript
transcript = ''

# Loop through each subtitle and add its text to the transcript
for sub in subs:
    transcript += sub.text + '\n'

# Write the transcript to a file called output.txt
with open('output.txt', 'w') as f:
    f.write(transcript)

# Print a message to confirm that the transcript was written to the file
print("Transcript written to output.txt")
