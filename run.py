import os
import subprocess

input_file = input("Please input your file in here : ")
env = os.environ.copy()
_, variable_for_this = os.path.splitext(input_file)
variable_for_this = variable_for_this.lower()

if variable_for_this == ".srt":
    # Run srt file split and run the Splitter
    srt_file = input_file
    env["SRT_FILE"] = srt_file
    subprocess.call(['python3', './srt_to_transcript/autorun.py'], env=env)
    txt_path = "./srt_output.txt"
    env["TXT_FILE"] = txt_path
    subprocess.call(['python3', './txt_splitter/autorun.py'], env=env)
    os.remove("./srt_output.txt")
elif variable_for_this == ".txt":
    #Run txt file in only Split mode
    txt_path = input_file
    env["TXT_FILE"] = txt_path
    subprocess.call(['python3', './txt_splitter/autorun.py'], env=env)
else:
    print("Not Supported, Only Supported .srt/.txt file format")
