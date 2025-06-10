El **Trabajo Práctico Integrador: Algoritmos de Búsqueda y Ordenamiento** tiene como objetivo analizar e implementar distintos métodos de búsqueda y ordenamiento en Python, evaluando su eficiencia y aplicabilidad en la gestión de datos.  

### **Estructura del Trabajo**  
1. **Introducción:** Explicación de la importancia de los algoritmos de búsqueda y ordenamiento en el desarrollo de software y la optimización de sistemas informáticos.  
2. **Marco Teórico:** Descripción de los principales algoritmos, incluyendo búsqueda lineal, búsqueda binaria, Bubble Sort, Quick Sort y Merge Sort, con análisis de su complejidad temporal.  
3. **Caso Práctico:** Implementación en Python de los algoritmos mencionados, aplicados a la organización de calificaciones de estudiantes. Se comparan tiempos de ejecución utilizando `datetime.now()` y `timeit`.  
4. **Metodología Utilizada:** Explicación del enfoque de desarrollo, pruebas realizadas y herramientas empleadas para evaluar el rendimiento de los algoritmos.  
5. **Resultados Obtenidos:** Comparación de la eficiencia de cada método, identificando ventajas y desventajas en distintos escenarios.  
6. **Conclusiones:** Reflexión sobre los hallazgos y posibles mejoras en la optimización de estos algoritmos.  
7. **Bibliografía y Anexos:** Fuentes consultadas y materiales adicionales, como repositorios de código y presentaciones explicativas.  

**instrucciones de uso** del código del **Trabajo Práctico Integrador: Algoritmos de Búsqueda y Ordenamiento** en Python:  

### **1. Instalación y Configuración**  
1. **Clonar el repositorio**  
   ```sh
   git clone https://github.com/usuario/repositorio.git
   cd repositorio
   ```
2. **Verificar dependencias**  
   - Asegúrate de tener **Python 3.x** instalado.  
   - No se requieren librerías externas, solo módulos estándar (`random`, `timeit`, `datetime`).  

### **2. Ejecución del Código**  
1. **Abrir el archivo principal**  
   ```sh
   python main.py
   ```
2. **Seleccionar el algoritmo de ordenamiento**  
   - Edita `config.py` para elegir entre **Bubble Sort, Quick Sort o Merge Sort**.  
3. **Seleccionar el algoritmo de búsqueda**  
   - Puedes optar por **Búsqueda Lineal o Búsqueda Binaria**.  

### **3. Análisis de Resultados**  
1. **Comparación de tiempos de ejecución**  
   - Los resultados se guardarán en `resultados.txt`.  
   - Se comparan mediciones con `datetime.now()` y `timeit`.  
2. **Validación de la correcta ejecución**  
   - Se verifica que la lista esté ordenada correctamente.  
   - Se comprueba que la búsqueda binaria encuentre el valor esperado.  

Reflexiones del Equipo:
Durante el trabajo práctico, comprobamos cómo la elección del algoritmo influye en la eficiencia del procesamiento de datos. **Bubble Sort** fue el más lento, mientras que **Quick Sort** y **Merge Sort** ofrecieron mejor rendimiento. **Búsqueda Binaria** mostró ser mucho más rápida que la búsqueda lineal en listas ordenadas. Además, `timeit` nos permitió obtener mediciones más precisas que `datetime.now()`.  

El trabajo en equipo fue clave para estructurar, probar y optimizar el código, permitiéndonos entender mejor la importancia de la modularidad y el análisis de rendimiento.

