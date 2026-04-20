import os
from CLI import parse_args
from organizer import organize_files
from utils import setup_logger, load_rules

def main():
    logger= setup_logger()
    config=load_rules()
    args=parse_args()

    logger.info(f"Path selezionato: {args.path}")
    logger.info(f"Modalità dry-run: {'Si' if args.dry_run else 'No'}")

    # Path checking
    if not os.path.exists(args.path):
        logger.info ("Il percorso non esiste.")
        exit()

    try:
        logger.info("Avvio organizer... ")
        organize_files(args.path, args.dry_run, logger, config)
        logger.info("Fine esecuzione")
    except Exception as e:
        logger.error(f"Errore fatale: {e}")
if __name__=="__main__":
    main()