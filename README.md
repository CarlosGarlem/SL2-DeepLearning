## Modelos de aprendizaje profundo
El siguiente proyecto presenta la aplicación de tres distintos modelos de redes neurales (MLP, CNN, RNN) para solventar problemas de aprendizaje supervisado, haciendo uso del framework de Tensorflow. 

### Estructura
Los archivos del proyecto se encuentran distribuidos de la siguiente manera:

**Modelo y funciones**
- **Carpeta de modelos**. Identificadas por el nombre de cada uno de los tres modelos contienen la lógica y estructura necesaria para cada uno de los modelos implementados.
  - **ModelType_Model.ipynb**. Notebook que contiene la lógica principal del modelo, así como los resultados y llamada a funciones auxiliares
  - **Archivos.py**. Clases o funciones utilizadas para organizar funciones de preprocesamiento de acuerdo al modelo y dataset
  - **models**. Directorio que contiene la bitácora de los distintos modelos utilizados (model_results.csv) así como carpetas con los IDs de cada modelo utilizado durante el entrenamiento, que a su vez contiene los checkpoints generados para el almacenamiento de los pesos (\*.ckpt) y la estructura inicial del modelo antes del entrenamiento (\*.h5) 
  - **input**. Directorio con el dataset utilizado (en caso de modelos como CNN y RNN la carpeta ha sido omitida dado el tamaño del dataset, ver sección de dataset para dirigirse a la URL)
  - **auxiliaryNotebooks**. Directorio con workbooks utilizados para evaluar la funciones o clases generadas en archivos \*.py para realizar tareas de preprocesamiento de datos

**Documentación**
- **SL2_Project_Paper.pdf**. Paper con resultados y descripción del proyecto
- **Poster SL2**. Poster para presentación del proyecto


**Datasets**
- **MLP**. https://www.kaggle.com/mirichoi0218/insurance
- **CNN**. https://www.kaggle.com/asdasdasasdas/garbage-classification
- **RNN**. Dataset presente en carpeta de Google Drive privada compartida por el docente


**Nota**. Por espacio no todos los modelos listados en la bitácora fueron subidos al repositorio, estos existen en copia local más no fue posible subirlos por lo cual no se conservan todos los modelos experimentales en el repositorio