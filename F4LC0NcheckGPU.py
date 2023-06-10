import pycuda.autoinit
import pycuda.driver as drv
from pycuda.tools import DeviceData

print(".########.##........##........######....#####...##....##\n.##.......##....##..##.......##....##..##...##..###...##\n.##.......##....##..##.......##.......##.....##.####..##\n.######...##....##..##.......##.......##.....##.##.##.##\n.##.......#########.##.......##.......##.....##.##..####\n.##.............##..##.......##....##..##...##..##...###\n.##.............##..########..######....#####...##....##")
print("Donate: 1FALCoN194bPQELKGxz2vdZyrPRoSVxGmR" )
print("see graphics card settings v1" )
print("посмотреть настройки видеокарты" )
print("" )


# Definir diccionario de traducciones
translations = {
    "en": {
        "max_params_info": "Maximum parameters supported by the device:",
        "max_grid_size": "Maximum grid size:",
        "max_block_size": "Maximum block size:",
        "max_threads_per_block": "Maximum threads per block:",
        "total_memory": "Total global memory:",
        "multiprocessor_count": "Number of multiprocessors:"
    },
    "ru": {
        "max_params_info": "Максимальные параметры, поддерживаемые устройством:",
        "max_grid_size": "Максимальный размер сетки:",
        "max_block_size": "Максимальный размер блока:",
        "max_threads_per_block": "Максимальное количество потоков в блоке:",
        "total_memory": "Общая память устройства:",
        "multiprocessor_count": "Количество мультипроцессоров:"
    }
}

# Función para obtener la cadena traducida
def translate(key):
    if language in translations and key in translations[language]:
        return translations[language][key]
    else:
        return key  # Devolver la clave original si no hay traducción disponible

# Obtener el número de dispositivos CUDA disponibles
device_count = drv.Device.count()

# Solicitar al usuario que seleccione el idioma
print("Select language:")
print("1. English")
print("2. Русский")
choice = input("Enter your choice (1 or 2): ")

# Establecer el idioma según la elección del usuario
if choice == "1":
    language = "en"
elif choice == "2":
    language = "ru"
else:
    language = "en"  # Idioma predeterminado en caso de una opción inválida

# Recorrer todos los dispositivos y obtener la información de cada uno
for i in range(device_count):
    device = drv.Device(i)
    device_name = device.name()
    device_props = device.get_attributes()

    max_grid_size = device_props[drv.device_attribute.MAX_GRID_DIM_X]
    max_block_size = device_props[drv.device_attribute.MAX_BLOCK_DIM_X]
    max_threads_per_block = device_props[drv.device_attribute.MAX_THREADS_PER_BLOCK]
    total_memory = device.total_memory()
    multiprocessor_count = device_props[drv.device_attribute.MULTIPROCESSOR_COUNT]


    # Imprimir la información obtenida del dispositivo actual en el idioma seleccionado
    print(f"\n{translate('max_params_info')} {device_name}")
    print(translate("max_grid_size"), max_grid_size)
    print(translate("max_block_size"), max_block_size)
    print(translate("max_threads_per_block"), max_threads_per_block)
    print(translate("total_memory"), total_memory, "bytes")
    print(translate("multiprocessor_count"), multiprocessor_count)
    
    # Esperar entrada del usuario para mantener la consola abierta
    input("Presione Enter para salir...")   