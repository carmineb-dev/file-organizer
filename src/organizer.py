
import shutil
from pathlib import Path

# Main function to organize files
def organize_files(path, dry_run, logger, rules):
    base_path=Path(path)

    for item in base_path.iterdir():

        if item.is_file():
            logger.info(f"FILE: {item.name} | EXT: '{item.suffix}'")
            extension= item.suffix.lower().strip()
            destination=rules.get(extension, "Altro")

            # Choose destination folder
            dest_folder= base_path / destination
            
            # Manage duplicates' names 
            final_path=dest_folder / item.name

            counter =1
            while final_path.exists():
                new_name=f"{item.stem}_{counter:02d}{item.suffix}"
                final_path=dest_folder / new_name
                counter+=1

            # Dry-run logic
            if dry_run:
                # Use only logger without creating folders
                logger.info (f"[DRY-RUN] {item.name} -> {final_path}")
            else:
                # Create the folder
                dest_folder.mkdir(exist_ok=True)
                shutil.move(str(item), str(final_path))
                logger.info (f"Spostato {item.name} -> {final_path}")
