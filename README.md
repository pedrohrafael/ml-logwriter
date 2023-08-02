# Machine Learning __LogWriter__

**ML LogWriter:** Biblioteca para Registro de Logs e Armazenamento de Artefatos

## Descrição
O ML LogWriter é uma biblioteca Python de código aberto disponibilizada que visa facilitar o registro de logs de execução de código e o armazenamento de artefatos de modelos em projetos de aprendizado de máquina e experimentos de ciência de dados. 

Com duas classes principais, `LogWriter` e `LogArtifacts`, essa biblioteca oferece uma solução simples e eficiente para acompanhar o desempenho de modelos e registrar informações essenciais durante o desenvolvimento de projetos.

## Módulos
### LogWriter:
A classe LogWriter é responsável por registrar logs de execução em dois locais simultaneamente: em um arquivo de log e no terminal. Suas principais funcionalidades incluem:

Registro detalhado de eventos: Possibilita registrar informações relevantes em diferentes níveis de detalhe (por exemplo, INFO, WARNING, ERROR) para auxiliar na depuração e monitoramento da execução do código.
- **Armazenamento em arquivo:** Registra as informações em um arquivo de log, permitindo revisitar eventos passados e manter um histórico de execuções.
- **Saída no terminal:** Exibe informações importantes diretamente no terminal, facilitando o acompanhamento do progresso do código em tempo real.

#### Exemplo de uso do módulo `LogWriter`:
```python
# Importando a classe LogWriter do módulo
from log_module import LogWriter

# Criando uma instância da classe LogWriter e definindo o caminho para o arquivo de log
log_writer = LogWriter()
log_path = 'logs/log_file.txt'

# Obtendo o logger para fazer os registros de log
logger = log_writer.logger(log_path)

# Exemplo de uso do logger para fazer registros de log
logger.debug("Debug message: This is a debug log.")
logger.info("Info message: This is an info log.")
logger.warning("Warning message: This is a warning log.")
logger.error("Error message: This is an error log.")
logger.critical("Critical message: This is a critical log.")
```

### LogArtifacts:
A classe LogArtifacts foi desenvolvida para armazenar e organizar artefatos essenciais de experimentos e modelos. Suas principais funcionalidades incluem:

- **Armazenamento de modelos e metadados:** Permite salvar modelos treinados juntamente com metadados relevantes, como hiperparâmetros e métricas de desempenho.
- **Gerenciamento de experimentos:** Organiza os resultados de experimentos em uma estrutura de diretórios clara e consistente, facilitando a localização e comparação entre diferentes iterações de modelos.
- **Armazenamento de dados e gráficos:** Além dos modelos, a classe LogArtifacts é capaz de armazenar outros artefatos, como conjuntos de dados, gráficos de desempenho e imagens relevantes para a análise dos resultados.

#### Exemplo de Uso do Módulo `LogArtifacts`:

```python
# Importando a classe LogArtifacts do módulo
from log_module import LogArtifacts

# Criando uma instância da classe LogArtifacts e definindo o caminho para o diretório de artefatos
artifacts_path = 'artifacts'

# Criando um novo diretório de artefatos (experimento)
experiment = LogArtifacts(artifacts_path)
experiment.create()

# Exemplo de uso da classe LogArtifacts para registrar parâmetros, métricas, modelo e dataset
parameters = {'learning_rate': 0.01, 'batch_size': 32, 'num_epochs': 50}
metrics = {'accuracy': 0.85, 'precision': 0.78, 'recall': 0.92}
model = 'Trained Model Object'
dataset = pd.DataFrame({'feature1': [1, 2, 3], 'feature2': [4, 5, 6]})

experiment.log_parameters(parameters)
experiment.log_metrics(metrics)
experiment.log_model(model)
experiment.log_dataset(dataset, 'example_dataset')

# Criando um gráfico de desempenho (exemplo com valores aleatórios)
x_values = [1, 2, 3, 4, 5]
y_values = [0.9, 0.85, 0.78, 0.75, 0.72]
experiment.log_performance_graph(x_values, y_values, title='Model Performance',
                                 x_label='Epoch', y_label='Accuracy', filename='accuracy_graph')

# Após executar o código acima, você verá os artefatos salvos no diretório 'artifacts' com os resultados do experimento.
```

## Principais Benefícios

- **Facilidade de Uso:** Com uma interface intuitiva, a biblioteca permite que desenvolvedores e cientistas de dados incorporem facilmente a funcionalidade de registro de logs e armazenamento de artefatos em seus projetos.
- **Organização e Rastreabilidade:** O ML LogWriter facilita a organização de experimentos e a rastreabilidade de modelos, permitindo que os usuários acessem informações históricas e comparem resultados de forma sistemática.
- **Colaboração Eficiente:** Ao armazenar artefatos e logs em arquivos, a biblioteca possibilita a colaboração entre membros da equipe, uma vez que todos os envolvidos podem compartilhar informações e resultados relevantes.
- **Melhoria no Processo de Desenvolvimento:** Com o registro detalhado de logs e a capacidade de armazenar artefatos, o ML LogWriter auxilia no processo de depuração, otimização de modelos e tomada de decisões com base em métricas objetivas.

## Instalação
```python
pip install ml-logwriter
```

## Requisitos
O ML LogWriter requer a instalação das bibliotecas Python necessárias para funcionar corretamente.
```
DateTime==5.2
joblib==1.3.1
logging==0.4.9.6
pytz==2023.3
zope.interface==6.0
matplotlib==3.7.0
```
Ou instale executando:
```python
pip install -r requirements.txt
```



## Contribuição e Licença:
A biblioteca ML LogWriter é de código aberto e é incentivada a contribuição da comunidade para o seu aprimoramento. Ela está licenciada sob a Licença MIT, garantindo liberdade de uso e modificação para qualquer projeto, seja comercial ou não.
