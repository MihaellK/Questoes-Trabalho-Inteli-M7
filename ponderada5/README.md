## Resenha do Artigo 'Machine learning for internet of things data analysis: a survey'

O artigo destaca o crescimento de dispositivos que recebem e enviam informações a internet e a geração de grandes volumes de dados no contexto de Internet das Coisas. A analise desses dados é fundamental para o desenvolvimento de aplicativos “inteligentes”, que, com o uso de aprendizado de maquina para analise desses dados, possuem um potencial incrivel de transformação em nossas vidas. Um estudo de caso é apresentado, aplicando o algoritmo Support Vector Machine (SVM) aos dados de tráfego de uma cidade inteligente. O SVM é um classificador binário que busca encontrar um hiperplano de separação entre duas classes de dados, maximizando a margem entre elas.

No contexto do artigo, o SVM foi aplicado a dados de tráfego de uma cidade inteligente. O objetivo era prever os padrões de tráfego em determinados horários do dia. O algoritmo foi treinado com dados históricos de tráfego, considerando variáveis como horário, localização e características do tráfego.

Após o treinamento, o SVM foi capaz de fazer previsões precisas sobre o tráfego em diferentes momentos do dia. Essas previsões podem ser usadas para otimizar o gerenciamento do tráfego, tomar decisões informadas sobre planejamento urbano e melhorar a eficiência dos sistemas de transporte em uma cidade inteligente.

A aplicação do SVM no contexto do artigo demonstra como esse algoritmo pode ser utilizado para extrair informações valiosas dos dados de IoT e melhorar a tomada de decisões em diferentes domínios.

Comparando o modelo de Extra Tree Regressor usada na atividade ponderada anterior. Primeiramente, no artigo não foi possivel identificar nenhuma técnica de transformação aplicada previamente nos dados, porém pode-se imaginar que um tratamento minimo de retirada de 0s e nulos, tenha sido feito. No modelo Extra Tree Regressor, foi utilizada, além da retirada de 0 e nulos, a normalização utilizando a técnica de zscore, a remoção de outliers.

Por fim, um dos pontos positivos do artigo é sua proposta de categorizar os algoritmos de aprendizado de máquina de acordo com suas similaridades estruturais, tipos de dados que podem lidar e a quantidade de dados que podem processar em um tempo razoável. 

No entanto, o artigo também apresenta algumas limitações. Uma delas é a falta de detalhes sobre os processos de transformação de dados utilizados no estudo de caso e em outros exemplos mencionados ao longo do texto. Isso dificulta a compreensão de como os dados foram preparados e quais técnicas específicas foram aplicadas antes de utilizar os algoritmos de aprendizado de máquina.

Apesar dessas limitações, o artigo fornece uma visão geral sólida sobre o uso de algoritmos de aprendizado de máquina na análise de dados de IoT e destaca a importância dessas técnicas para o desenvolvimento de aplicações inteligentes
