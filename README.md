# Machine Learning __LogWriter__

**ML LogWriter:** Biblioteca para Registro de Logs e Armazenamento de Artefatos

## Descrição
O ML LogWriter é uma biblioteca Python de código aberto disponibilizada que visa facilitar o registro de logs de execução de código e o armazenamento de artefatos de modelos em projetos de aprendizado de máquina e experimentos de ciência de dados. 

Com duas classes principais, `LogWriter` e `LogArtifacts`, essa biblioteca oferece uma solução simples e eficiente para acompanhar o desempenho de modelos e registrar informações essenciais durante o desenvolvimento de projetos.

## Funcionalidades
### LogWriter:
A classe LogWriter é responsável por registrar logs de execução em dois locais simultaneamente: em um arquivo de log e no terminal. Suas principais funcionalidades incluem:

Registro detalhado de eventos: Possibilita registrar informações relevantes em diferentes níveis de detalhe (por exemplo, INFO, WARNING, ERROR) para auxiliar na depuração e monitoramento da execução do código.
- **Armazenamento em arquivo:** Registra as informações em um arquivo de log, permitindo revisitar eventos passados e manter um histórico de execuções.
- **Saída no terminal:** Exibe informações importantes diretamente no terminal, facilitando o acompanhamento do progresso do código em tempo real.

### LogArtifacts:
A classe LogArtifacts foi desenvolvida para armazenar e organizar artefatos essenciais de experimentos e modelos. Suas principais funcionalidades incluem:

- **Armazenamento de modelos e metadados:** Permite salvar modelos treinados juntamente com metadados relevantes, como hiperparâmetros e métricas de desempenho.
- **Gerenciamento de experimentos:** Organiza os resultados de experimentos em uma estrutura de diretórios clara e consistente, facilitando a localização e comparação entre diferentes iterações de modelos.
- **Armazenamento de dados e gráficos:** Além dos modelos, a classe LogArtifacts é capaz de armazenar outros artefatos, como conjuntos de dados, gráficos de desempenho e imagens relevantes para a análise dos resultados.

## Principais Benefícios

- **Facilidade de Uso:** Com uma interface intuitiva, a biblioteca permite que desenvolvedores e cientistas de dados incorporem facilmente a funcionalidade de registro de logs e armazenamento de artefatos em seus projetos.
- **Organização e Rastreabilidade:** O ML LogWriter facilita a organização de experimentos e a rastreabilidade de modelos, permitindo que os usuários acessem informações históricas e comparem resultados de forma sistemática.
- **Colaboração Eficiente:** Ao armazenar artefatos e logs em arquivos, a biblioteca possibilita a colaboração entre membros da equipe, uma vez que todos os envolvidos podem compartilhar informações e resultados relevantes.
- **Melhoria no Processo de Desenvolvimento:** Com o registro detalhado de logs e a capacidade de armazenar artefatos, o ML LogWriter auxilia no processo de depuração, otimização de modelos e tomada de decisões com base em métricas objetivas.

## Instalação
```
pip install ml-logwriter
```

## Requisitos
O ML LogWriter requer a instalação das bibliotecas Python necessárias para funcionar corretamente.
```
pip install -r requirements.txt
```

## Contribuição e Licença:
A biblioteca ML LogWriter é de código aberto e incentivo a contribuição da comunidade para o seu aprimoramento. Ela está licenciada sob a Licença MIT, garantindo liberdade de uso e modificação para qualquer projeto, seja comercial ou não.
