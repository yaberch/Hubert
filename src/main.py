from dotenv import load_dotenv
import os
from bot.hubert import Hubert
from utils.logger import setup_logger
from exceptions.custom_exceptions import *

def main():
    # Charger les variables d'environnement
    load_dotenv()
    
    # Configurer le logger principal
    logger = setup_logger("Main")
    
    try:
        # Initialiser le bot
        bot = Hubert()
        
        # Se connecter à Facebook
        if not bot.login():
            raise LoginError("Échec de la connexion à Facebook")

        """            
        # Exemple d'utilisation
        group_url = os.getenv('FB_GROUP_URL')
        if group_url:
            bot.navigate_to_group(group_url)
            # Ajoutez ici d'autres actions...
        """    

    except LoginError as e:
        logger.error(f"Erreur de connexion: {str(e)}")
    except Exception as e:
        logger.error(f"Erreur inattendue: {str(e)}")
    finally:
        if 'bot' in locals():
            bot.cleanup()

if __name__ == "__main__":
    main()
