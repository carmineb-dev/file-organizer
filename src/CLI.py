import argparse
import os

# Set the arguments' parser
def parse_args():
    parser = argparse.ArgumentParser(description="Organizza i file in una cartella.")
    parser.add_argument('--path', type=str, required=True, help="Percorso della cartella da organizzare." )
    parser.add_argument('--dry-run', action='store_true', help="Simula l'operazione senza modifiche.")

        
    return parser.parse_args()