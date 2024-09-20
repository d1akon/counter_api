#----- IMPORTS
import logging
import sys

#----- DEFINICION DE LOGGER A USAR
def setup_logging():
    """
    Configura el logger que voy a usar para toda la app.
    """
    logging.basicConfig(
        level=logging.INFO,  
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout)  #-----podria guardarse en una ruta de logeo centralizada como mejora
        ]
    )

setup_logging()

#----- instancia de logger
logger = logging.getLogger(__name__)
