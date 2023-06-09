#F4LC0NcheckGPU
F4LC0NcheckGPU
F4LC0NcheckGPU is a program written in Python that allows you to get detailed information about the CUDA devices present on a system. It provides relevant information about the maximum parameters supported by each device, such as the maximum grid size, the maximum block size, the maximum number of threads per block, the total global memory and the number of multiprocessors.

Characteristics
Support for multiple languages: The program allows the user to select the desired language when starting the execution. Currently, English (English) and Russian (Русский) are supported. This ensures that users can use the program in their preferred language.

Automatic device detection: The program automatically detects all CUDA devices present in the system and displays the corresponding information for each of them. This allows you to get a complete view of the resources available on each device.

Command line interface: The program is executed from the command line, which makes it easy to use and integrate into scripts or automated workflows.

"Maximum parameters supported by the device: <device_name>": This line displays the full name of the CUDA device. For example, if the device is named "GeForce RTX 2080 Ti", "Maximum parameters supported by the device: GeForce RTX 2080 Ti" will be displayed.

"Maximum grid size: <max_grid_size>": This line shows the maximum size of the grid (grid) in dimension X. The grid is a three-dimensional structure used to organize the thread blocks in a CUDA execution. Shown here is the maximum size in the X dimension.

"Maximum block size: <max_block_size>": This line displays the maximum block size in dimension X. A block is a pool of threads running concurrently on a CUDA multiprocessor. Shown here is the maximum size in the X dimension.

"Maximum threads per block: <max_threads_per_block>": This line shows the maximum number of threads that can be executed in a block. Threads are smaller processing units that run within a block on a CUDA multiprocessor.

"Total global memory: <total_memory> bytes": This line displays the total amount of global memory available on the CUDA device in bytes. Global memory is shared memory used by all threads on a CUDA device.

"Number of multiprocessors: <multiprocessor_count>": This line displays the number of multiprocessors on the CUDA device. Multiprocessors are parallel processing units on the device and are responsible for running blocks of threads.

-------------------------------------------------------------------------------------------------------------------

# F4LC0NcheckGPU
F4LC0NcheckGPU
F4LC0NcheckGPU es un programa escrito en Python que permite obtener información detallada sobre los dispositivos CUDA presentes en un sistema. Proporciona información relevante sobre los parámetros máximos soportados por cada dispositivo, como el tamaño máximo del grid, el tamaño máximo del bloque, el número máximo de hilos por bloque, la memoria global total y el número de multiprocesadores.

Características
Soporte para múltiples idiomas: El programa permite al usuario seleccionar el idioma deseado al iniciar la ejecución. Actualmente, se admite el inglés (English) y el ruso (Русский). Esto garantiza que los usuarios puedan utilizar el programa en su idioma preferido.

Detección automática de dispositivos: El programa detecta automáticamente todos los dispositivos CUDA presentes en el sistema y muestra la información correspondiente para cada uno de ellos. Esto permite obtener una visión completa de los recursos disponibles en cada dispositivo.

Interfaz de línea de comandos: El programa se ejecuta desde la línea de comandos, lo que facilita su uso e integración en scripts o flujos de trabajo automatizados.
