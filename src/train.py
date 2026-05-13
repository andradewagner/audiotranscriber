import yaml
import pandas as pd
# Exemplo de uso
def load_config(config_path="config.yaml"):
    with open(config_path, "r") as f:
        return yaml.safe_load(f)

def train():
    config = load_config()
    
    # Acessando os dados do YAML
    data_path = config['paths']['processed_data']
    n_estimators = config['model']['params']['n_estimators']
    
    print(f"🚀 Training {config['model']['algorithm']} with {n_estimators} estimators...")
    # Lógica de treino aqui...

if __name__ == "__main__":
    train()