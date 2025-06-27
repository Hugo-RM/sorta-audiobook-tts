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

if __name__ == '__main__':
    file_path = 'I Am Not Your Perfect Mexican Daughter Full Book.txt'  # Replace with the actual path to your text file

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            string_file = file.read()
        convertText('Audio Book I Am Not Your Perfect Mexican Daughter by Erika L. Sanchez', string_file)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    