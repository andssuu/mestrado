# mestrado

Repositório dedicado para o desenvolvimento das atividades do mestrado em Informática Aplicada na UFRPE.

## Estrutura da Base de Dados

  ### experimento-01

  - branquinha
    - sensores
      - conjunto de arquivos .txt do gps (ts-gps.txt) e acelerômetro (ts-acc.txt). O arquivos unified são a concatenação de todos os dados coletados em múltiplo arquivos .txt
      - Formato dos dados nos arquivos:
      ```
        time_stamp; acc_x; acc_y; acc_z; temperature; gyroscope_x; gyroscope_y; gyroscope_z
      ```
  - Hobo: dados dos dois medidores de temperatura e umidade instalados no pasto (sombra e pasto)

  - Mimosa: dados semelhantes aos de branquinha

  - sd-01-pretinha
    - imagens: nesta vaca instalamos uma camera para que pudessemos verificar o comportamento, no entanto, a camera falhou logo no inicio do experimento e não fomos capazes de utilizar estes dados
    - sensores: dados coletados pelo sensores: dados semelhantes aos de branquinha e mimosa

  - sd-02-chuviscada
    - sensores: dados semelhantes aos de branquinha, mimosa e pretinha

  - Comportamento 08-08-19: dados de comportamento coletados manualmente a cada 10 minutos durante um dia por Pedro no experimento

  - _unified-gps-01.txt_: dados de gps unificados de branquinha

  - _unified-gps-02.txt_: dados de gps unificados de mimosa

  - _unified-gps-03.txt_: dados de gps unificados de pretinha

  - _unified-gps-04.txt_: dados de gps unificados de chuviscada

  - _unified-gps.txt_: dados de gps de todas as vacas

  * * *

  ### experimento-02 
  - O segundo experimento possui estrutura semelhante só uma mudança de animal que para nós a priori é indiferente. saiu pretinha e entrou furtacor)

  * * *

  ### experimento-03
  - O terceiro experimento possui estrutura semelhante no entanto voltou pretinha e saiu furtacor

  * * *

  ### Fotos (fotos do experimento)

  * * *


## Visualização dos Dados

  ### Posição Geográfica (GPS)
  - *Heat Map*: Mapa de calor da posição do animal.
    ![Screenshot from 2020-05-19 08-54-40](https://user-images.githubusercontent.com/6972758/82323462-771d7580-99ae-11ea-81df-14364c0fa8b0.png)

  - *Track Map:* Mapa com a posição e direção do animal.
  ![Screenshot from 2020-05-19 08-56-08](https://user-images.githubusercontent.com/6972758/82323577-a46a2380-99ae-11ea-9fc1-de77ac8d7a32.png)

  ### Acelerômetro
  - ```acc_plot_all.py```: plota os valores das 3 coordenada de um dia em intervalos de 1 hora.
    ![08/08/2019](https://github.com/andssuu/mestrado/blob/master/figures/exp1/accelerometer/exp1_acc_all.png)

  - ```acc_plot_hour.py```: plota os valores das 3 coordenadas em intervalos de 1 hora.
    ![08/08/2019:13:14](https://github.com/andssuu/mestrado/blob/master/figures/exp1/accelerometer/exp1_acc_13-14.png)
    ![08/08/2019:19:20](https://github.com/andssuu/mestrado/blob/master/figures/exp1/accelerometer/exp1_acc_19-20.png)

  - ```acc_plot_minute.py```: plota os valores das 3 coordenadas durante uma determinada hora em intervalos de 1 minuto.
    ![](https://github.com/andssuu/mestrado/blob/master/figures/exp1/accelerometer/0h/exp1_acc_min_0-1.png)

  - ```acc_plot_all_3d.py```: plota em 3D os valores das 3 coordenada de um dia em intervalos de 1 hora.
    ![](https://github.com/andssuu/mestrado/blob/master/figures/exp1/accelerometer/3D/exp1_acc_all_3d.png)

  - ```acc_plot_hour_3d.py```:  plota em 3D os valores das 3 coordenadas em intervalos de 1 hora.
    ![](https://github.com/andssuu/mestrado/blob/master/figures/exp1/accelerometer/3D/exp1_acc_0-1_3d.png)

  - ```acc_plot_minute_3d.py```: plota em 3D os valores das 3 coordenadas durante uma determinada hora em intervalos de 1 minuto.
  ![](https://github.com/andssuu/mestrado/blob/master/figures/exp1/accelerometer/3D/0h/exp1_acc_min_0-1_3d.png)

  - ```acc_plot_minute_power.py```: plota os distribuição do spectro das 3 coordenadas durante uma determinada hora em intervalos de 1 minuto.
  

  - ```acc_plot_minute_distribution.py```: plota os distribuição do spectro das 3 coordenadas durante uma determinada hora em intervalos de 1 minuto.


  - ```acc_plot_minute_std.py```: gráfico de barras exibindo os valores dos desvios-padrão das 3 coordenadas da aceleração em intervalos de 1 minuto dentro de 1 hora.

  - ```acc_boxplot_minute_std.py```: gráfico do tipo boxoplot com os valores dos desvios-padrão das 3 coordenadas da aceleração em intervalos de 1 minuto dentro de 1 hora.  


  ### Giroscópio (TODO)

  ### Temperatura (TODO)

## Arquitetura (TODO)

  ### Pré-processamento
  
  

  ### Extração de Características

  ### Classificação

  #### Principais atividades na determinação do comportamento

  - **Andando:** Caminhando sem apreensão de forragem.
  
  - **Bebendo:** Acesso ao bebedouro e consumo de água.
  
  - **Comendo:** Apreensão de forragem durante o pastejo.
  
  - **Ruminando:** Regurgitação, mastigação e deglutição.
  
  - **Ócio:** Em pé ou deitada, sem realizar nenhuma das atividades anteriores.


## Observações

1. Todas as datas e horários estão em UTC, incluindo os nomes dos próprios arquivos.
