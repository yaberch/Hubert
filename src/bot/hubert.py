import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from utils.config import config
from utils.logger import setup_logger
import time
import random

class Hubert:
    def __init__(self):
        self.logger = setup_logger()
        self.driver = None
        self.wait = None
        self.setup_driver()

    def setup_driver(self):
        """Configure le navigateur Chrome"""
        try:
            chrome_options = uc.ChromeOptions()
            prefs = {
                "profile.default_content_setting_values.notifications": 2,  # Désactive les notifications
                "credentials_enable_service": False,  # Désactive la popup d'enregistrement des identifiants
                "profile.password_manager_enabled": False  # Désactive le gestionnaire de mots de passe
            }
            chrome_options.add_experimental_option("prefs", prefs)
            chrome_options.add_argument('--start-maximized')  # Fenêtre maximisée
            
            # En mode debug, ne pas cacher le navigateur
            if config.DEBUG:
                chrome_options.headless = False
            else:
                chrome_options.add_argument('--headless')

            self.driver = uc.Chrome(options=chrome_options)
            self.wait = WebDriverWait(self.driver, config.WAIT_TIMEOUT)
            self.logger.info("Navigateur initialisé avec succès")
        except Exception as e:
            self.logger.error(f"Erreur lors de l'initialisation du navigateur: {str(e)}")
            raise

    def random_sleep(self, min_time=1, max_time=4):
        """Pause aléatoire pour simuler un comportement humain"""
        time.sleep(random.uniform(min_time, max_time))

    def humanlike_typing(element, text):
        """Simule la frappe humaine avec vitesse variable et pauses occasionnelles"""
        for char in text:
            element.send_keys(char)
            # Pause plus longue après ponctuation
            if char in ['.', ',', '!', '?']:
                time.sleep(random.uniform(0.3, 0.7))
            else:
                time.sleep(random.uniform(0.05, 0.25))
            
            # Parfois faire une pause comme un humain réfléchissant
            if random.random() < 0.05:
                time.sleep(random.uniform(0.5, 1.2))

    def login(self):
        """Se connecte à Facebook"""
        try:
            self.logger.info("Tentative de connexion à Facebook")
            self.driver.get(config.FB_URL)
            self.random_sleep()

            # Trouver les champs d'identification
            email_field = self.wait.until(EC.presence_of_element_located((By.ID, "email")))
            password_field = self.wait.until(EC.presence_of_element_located((By.ID, "pass")))

            # Simuler mouvement souris avec courbe naturelle
            action = ActionChains(self.driver)
            action.move_to_element_with_offset(email_field, random.randint(-5, 5), random.randint(-3, 3))
            action.perform()
            self.random_sleep()
            action.click(email_field).perform()

            # Simulation de frappe humaine
            self.logger.info("Saisie du nom d'utilisateur...")
            self.humanlike_typing(email_field, config.FB_USERNAME)

            self.logger.info("Saisie du mot de passe...")
            self.humanlike_typing(password_field, config.FB_PASSWORD)
    
            # Parfois cliquer sur le bouton de connexion au lieu d'appuyer sur Entrée
            if random.choice([True, False]):
                login_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='login']")))
                action.move_to_element(login_button).perform()
                time.sleep(random.uniform(0.5, 1))
                login_button.click()
            else:
                password_field.send_keys(Keys.RETURN)

            # Vérifier si la connexion est réussie
            self.logger.info("Attente du chargement de la page d'accueil...")
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[role='navigation']")))
            self.logger.info("Connexion réussie !")
            return True

        except Exception as e:
            self.logger.error(f"Erreur lors de la connexion: {str(e)}")
            return False

    def cleanup(self):
        """Nettoie les ressources"""
        if self.driver:
            self.driver.quit()
            self.logger.info("Navigateur fermé")

    # Ajoutez ici vos méthodes spécifiques pour l'automatisation
    # Par exemple :
    def navigate_to_group(self, group_url):
        try:
            self.logger.info(f"Navigation vers le groupe: {group_url}")
            self.driver.get(group_url)
            self.random_sleep()
        except Exception as e:
            self.logger.error(f"Erreur lors de la navigation: {str(e)}")

    def post_message(self, message):
        try:
            # Implémentez ici la logique pour poster un message
            pass
        except Exception as e:
            self.logger.error(f"Erreur lors de la publication: {str(e)}")
