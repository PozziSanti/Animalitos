# Mascota Virtual

Este es un sencillo juego de mascota virtual escrito en Python, donde puedes interactuar con una mascota digital, alimentarla, jugar con ella y monitorear su estado de ánimo.

## Características

* **Nombre Personalizado:** Asigna un nombre único a tu mascota virtual.
* **Alimentación:** Mantén a tu mascota satisfecha y saludable alimentándola. Una mascota llena no comerá más y mostrará su disgusto.
* **Interacción de Juego:** Juega con tu mascota para aumentar su felicidad. Ten en cuenta que una mascota muy hambrienta no podrá jugar.
* **Monitor de Ánimo:** Verifica el estado de ánimo de tu mascota para saber si está feliz, hambrienta, triste o una combinación de estos estados.
* **Arte ASCII:** Disfruta de representaciones visuales de tu mascota en diferentes estados de ánimo y acciones a través de arte ASCII.

## Cómo Jugar

1.  **Clona el Repositorio:**
    ```bash
    git clone [https://github.com/tu_usuario/MascotaVirtual.git](https://github.com/tu_usuario/MascotaVirtual.git)
    cd MascotaVirtual
    ```
2.  **Ejecuta el Script:**
    ```bash
    python Mascota_virtual_resuelto.py
    ```
    (Se recomienda usar `Mascota_virtual_resuelto.py` ya que contiene la lógica completa para jugar y mostrar el estado de ánimo).

3.  **Interactúa con tu Mascota:**
    * Al iniciar, se te pedirá que elijas un nombre para tu mascota.
    * Un menú de opciones aparecerá continuamente, permitiéndote:
        * Ingresar `1` para **Alimentar** a tu mascota.
        * Ingresar `2` para **Jugar** con tu mascota.
        * Ingresar `3` para **Mostrar información** (estado de ánimo) sobre tu mascota.
        * Ingresar `4` para **Salir** del juego.

## Estructura del Código

* `Mascota_virtual_resuelto.py`: Este es el archivo principal que contiene la lógica del juego, la clase `MascotaVirtual` con sus métodos para alimentar, jugar, verificar el estado de ánimo, y el bucle principal de interacción.
* `Mascota_virtual_desafio.py`: Una versión inicial o "desafío" del juego, con algunas funcionalidades aún por implementar (ej. `jugar` y `estado_animo` marcados con `pass`).
* `mascota.py`: Define la clase `ImagenMascota`, que almacena las representaciones en arte ASCII de la mascota para diferentes estados (inicio, feliz, disgustado, triste, muerto).

### Clase `MascotaVirtual` (en `Mascota_virtual_resuelto.py`)

* `__init__(self, nombre)`: Constructor que inicializa a la mascota con un nombre, y establece los niveles de `hambre` y `felicidad` en 0. También carga las imágenes ASCII para los diferentes estados.
* `alimentar(self)`: Reduce el hambre de la mascota y disminuye ligeramente su felicidad. Si la mascota ya está llena, mostrará disgusto.
* `jugar(self)`: Aumenta la felicidad y el hambre de la mascota. Si la mascota tiene mucha hambre (hambre >= 70), no podrá jugar.
* `estado_animo(self)`: Evalúa los niveles de hambre y felicidad para imprimir el estado de ánimo actual de la mascota, como "muy hambrienta y muy triste" o "contenta y satisfecha".
* `presentacion(self)`: Muestra un mensaje de bienvenida y la imagen inicial de la mascota junto con su nombre.
* `despedida(self)`: Presenta un mensaje de despedida al salir del juego.

## Requisitos

* Python 3.x

## Contribución

¡Las contribuciones son bienvenidas! Si deseas mejorar este proyecto, puedes:

* Forkear el repositorio.
* Crear una nueva rama (`git checkout -b feature/nueva-caracteristica`).
* Realizar tus cambios y hacer commit (`git commit -am 'Agrega nueva característica'`).
* Empujar a la rama (`git push origin feature/nueva-caracteristica`).
* Abrir un Pull Request.

---

¡Disfruta cuidando a tu mascota virtual!
