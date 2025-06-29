import subprocess
import os
import re

language = "en"

def sanitize_filename(filename):
    # Remove invalid characters
    filename = re.sub(r'[<>:"/\\|?*]', '', filename)
    return filename

# A simple function to create the audio files using the name and its text

def convertText(title, myText):
    filename = f"{title}.wav"
    filepath = os.path.join("static", filename)

    if os.path.exists((filepath)) or not (myText):
        return
        
    # Pipe text directly to Piper instead of using a file
    result = subprocess.run([
        "piper/piper.exe",
        "--model", "en_GB-cori-medium.onnx",
        "--output_file", filepath
    ], input=myText, text=True)
    
    print(f"Piper finished. Return code: {result.returncode}")
    
    if os.path.exists(filepath):
        file_size = os.path.getsize(filepath)
        print(f"Audio file created: {filepath} ({file_size} bytes)")
    else:
        print("ERROR: Audio file was not created!")

    
