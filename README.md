# IC6200_AI_P2

Este proyecto está diseñado para utilizar TensorFlow, que requiere una versión máxima de Python 3.10. Dado que actualmente tengo Python 3.12.1, decidí utilizar Miniconda para gestionar el entorno.

[Documentación de Miniconda](https://docs.anaconda.com/miniconda/)


## Configuración de Conda

### Instalación Predeterminada

La ruta de instalación predeterminada es:
```
C:\ProgramData\miniconda3
```

### Rutas Necesarias en el PATH

Asegúrate de agregar las siguientes rutas al PATH:
```
C:\ProgramData\miniconda3
C:\ProgramData\miniconda3\Scripts
C:\ProgramData\miniconda3\Library\bin
```

### Verificar Instalación de Conda

Para verificar que Conda está instalado correctamente, ejecuta:
```bash
conda --version
```

### Listar Entornos de Conda

Para ver los entornos de Conda disponibles:
```bash
conda info --envs
```

### Crear un Nuevo Entorno

Para crear un nuevo entorno con Python 3.8:
```bash
conda create --name <env_name> python=3.8
```
*Nota: Python 3.10 es compatible con TensorFlow, pero no con TensorFlow-GPU.*

### Eliminar un Entorno

Para eliminar un entorno específico:
```bash
conda remove --name <env_name> --all
```

### Ubicación del Entorno

Los entornos se encuentran en:
```
C:\Users\<user_name>\.conda\envs\<env_name>
```

### Activar un Entorno

Para activar un entorno:
```bash
conda activate <env_name>
```


## Instalación de TensorFlow

Una vez activado el entorno, instala TensorFlow con el siguiente comando:
```bash
conda install tensorflow
```

Si necesitas la versión GPU, instala también:
```bash
conda install tensorflow-gpu
```

### Listar Paquetes Instalados

Para ver los paquetes instalados en el entorno:
```bash
conda list
```

También puedes obtener información general sobre Conda con:
```bash
conda info
```

*Nota: Visual Studio Code puede requerir la instalación de `ipykernel`.*


## Problemas de Incompatibilidad

### TensorFlow y NumPy
Es importante tener en cuenta que TensorFlow 2.6.0 solo es compatible con versiones de NumPy en el rango de [1.19.x, 1.21.x]. Las versiones fuera de este rango pueden causar problemas de compatibilidad.

Para verificar las versiones instaladas de TensorFlow y NumPy, utiliza:
```bash
pip show tensorflow
pip show numpy
```

#### Instalar la versión específica de NumPy
Para instalar la versión de NumPy compatible con TensorFlow, ejecuta:
```bash
pip install numpy==1.19.5
```

Esto puede requerir desinstalar y reinstalar TensorFlow:
```bash
pip install tensorflow==2.6.0
```

#### Probar la instalación
Para verificar que TensorFlow se ha instalado correctamente, prueba el siguiente código:
```python
import tensorflow as tf
print(tf.__version__)
```

### NumPy y Matplotlib
Asegurarse de instalar Matplotlib 3.4.3 para que funcione con la versión de NumPy.
```bash
pip install matplotlib==3.4.3
```

May be required uninstall and reinstall Matplotlib
```bash 
pip uninstall matplotlib
pip install matplotlib
```
# Uso con PyTorch

Se crea un entorno limpio
```bash
conda create --name env_IC6200_AI_P2_pytorch python=3.8
```
Se setea
```bash
conda activate env_IC6200_AI_P2_pytorch
```
Para instalar pytorch (2.4.1) para cuda (11.8)
```bash
conda install pytorch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1  pytorch-cuda=11.8 -c pytorch -c 
nvidia
```
Para verlo
```bash
pip list | findstr torch
```
Para ver la versión del compilador de CUDA instalada en tu sistema para trabajar con GPUs NVIDIA.
```bash
nvcc --version
```
Para ver información sobre la GPU de NVIDIA instalada, su uso actual, versión de driver y versión de CUDA.
```bash
nvidia-smi
```
Para obtener el instalador de cuda ir a la pagina
https://developer.nvidia.com/cuda-11-8-0-download-archive

Aqui se descomprime metio ahi
C:\Users\aleja\AppData\Local\Temp\cuda

Se suele usar Matplotlib
```bash
conda install matplotlib
```


```bash
conda install numpy
```


```bash
conda install -c conda-forge opencv
o
pip install opencv-python
```
Instalarlo con conda no me sirvió así que lo isntalé con pip.





