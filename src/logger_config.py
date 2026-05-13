import os
import logging
from logging.handlers import RotatingFileHandler
from typing import Dict, Any

def get_logger(name: str, config: Dict[str, Any] = None) -> logging.Logger:
    """Retorna um logger configurado com base no dicionário do config.yaml."""
    
    # Extrai os parâmetros do YAML ou assume fallbacks seguros se não existirem
    logger_config = config.get("logger", {}) if config else {}
    
    log_file = logger_config.get("log_file", "logs/transcription.log")
    log_level_str = logger_config.get("log_level", "INFO").upper()
    formatter_str = logger_config.get("formatter", "%(asctime)s [%(levelname)s] (%(name)s) %(message)s")
    
    # Mapeia a string do nível de log para a constante do módulo logging
    level = getattr(logging, log_level_str, logging.INFO)
    
    # Cria a pasta de logs se ela não existir
    if os.path.dirname(log_file):
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
    
    logger = logging.getLogger(name)
    
    # Evita duplicar handlers se a função for chamada mais de uma vez
    if not logger.handlers:
        logger.setLevel(level)
        
        # Formato dinâmico vindo do YAML
        formatter = logging.Formatter(formatter_str)
        
        # Handler para o Console
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        
        # Handler para o Arquivo com rotação de 5MB
        file_handler = RotatingFileHandler(
            log_file, 
            maxBytes=5*1024*1024, 
            backupCount=3,        
            encoding="utf-8"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
    return logger
