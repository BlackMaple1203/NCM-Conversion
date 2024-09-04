import os
import subprocess
from pydub import AudioSegment

def convert_flac_to_mp3(input_folder,output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    files = [f for f in os.listdir(input_folder) if f.endswith('.flac')]
    print("====================================")
    for file in files:
        input_path = os.path.join(input_folder,file)
        output_path = os.path.join(output_folder,os.path.splitext(file)[0]+'.mp3')
        print(f"Converting {file} to mp3...")
        audio = AudioSegment.from_file(input_path,format="flac")
        audio.export(output_path,format="mp3",bitrate="320k")
        print(f"{file} converted to mp3 successfully")

def convert_ncm_to_mp3(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    files = [f for f in os.listdir(input_folder) if f.endswith('.ncm')]
    print("====================================")
    for file in files:
        input_path = os.path.join(input_folder, file)
        print(f"Decoding {file}...")
        flac_output_path = os.path.join(output_folder, os.path.splitext(file)[0] + '.flac')
        subprocess.run(['ncmdump', input_path, '-o', input_path], check=False)
        print(f"{file} decoded successfully")

    convert_flac_to_mp3(input_folder,output_folder)
    new_files = [f for f in os.listdir(input_folder) if f.endswith('.flac')]
    print("Removing caches...")
    for new_file in new_files:
        new_file_path = os.path.join(input_folder,new_file)
        os.remove(new_file_path)
    print("====================================")   
    print("All files converted to mp3 successfully!")
input_folder = "/Users/tony/Desktop/Tony/Audio"
output_folder = "/Users/tony/Desktop/Tony/Audio_Exported"
convert_ncm_to_mp3(input_folder, output_folder)
