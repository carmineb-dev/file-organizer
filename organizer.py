import os
import shutil
import argparse

# Set the arguments' parser
def parse_args():
    parser = argparse.ArgumentParser(description="Organizza i file in una cartella.")
    parser.add_argument('--path', type=str, required=True, help="Percorso della cartella da organizzare." )
    parser.add_argument('--dry-run', action='store_true', help="Simula l'operazione senza modifiche.")
    return parser.parse_args()

# Execute parsing
args=parse_args()
path=args.path
dry_run=args.dry_run

print (f"Path selezionato: {path}")
print(f"Modalità dry-run: {'Si' if dry_run else 'No'}")

# Path checking
if not os.path.exists(path):
    print ("Il percorso non esiste.")
    exit()

# File type dictionary
rules={
    ".jpg":"Immagini",
    ".png":"Immagini",
    ".pdf":"Documenti",
    ".txt": "Documenti",
    "docx": "Documenti",
    ".exe":"Programmi",
    ".mp4":"Video",
    ".zip":"Archivio"
}

# Main function to organize files
def organize_files(path, dry_run):
    files = os.listdir(path)

    for file in files:
        full_path=os.path.join(path, file)

        if os.path.isfile(full_path):
        
            extension= os.path.splitext(full_path)[1].lower()
            destination=rules.get(extension or "", "Altro")

            # Create destination folder
            dest_folder= os.path.join(path, destination)
            os.makedirs(dest_folder, exist_ok=True)
            
            # Manage duplicates' names 
            base, ext=os.path.splitext(file)
            final_path=os.path.join(dest_folder, file)

            counter =1
            while os.path.exists(final_path):
                new_name=f"{base}_{counter:02d}{ext}"
                final_path=os.path.join(dest_folder, new_name)
                counter+=1

            # Dry-run logic
            if dry_run:
                print (f"[DRY-RUN] {file} -> {final_path}")
            else:
                shutil.move(full_path, final_path)
                print (f"Spostato {file} -> {final_path}")

# Execute
organize_files(path, dry_run)