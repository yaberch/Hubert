class FacebookBotError(Exception):
    """Erreur de base pour le bot"""
    pass

class LoginError(FacebookBotError):
    """Erreur de connexion"""
    pass

class NavigationError(FacebookBotError):
    """Erreur de navigation"""
    pass

class PostError(FacebookBotError):
    """Erreur lors de la publication"""
    pass
