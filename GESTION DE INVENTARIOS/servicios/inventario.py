from modelos.producto import Producto


class Inventario:
    def __init__(self):
        self._productos = []

    def agregar_producto(self, producto):
        if any(p.get_id() == producto.get_id() for p in self._productos):
            return False
        self._productos.append(producto)
        return True

    def eliminar_producto(self, producto_id: int):
        for producto in self._productos:
            if producto.get_id() == producto_id:
                self._productos.remove(producto)
                return True
        return False

    def actualizar_producto(self, producto_id: int, nueva_cantidad=None, nuevo_precio=None):
        for producto in self._productos:
            if producto.get_id() == producto_id:
                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)
                return True
        return False

    def buscar_por_nombre(self, nombre: str):
        nombre = nombre.lower()
        return [
            producto
            for producto in self._productos
            if nombre in producto.get_nombre().lower()
        ]

    def listar_productos(self):
        return self._productos
