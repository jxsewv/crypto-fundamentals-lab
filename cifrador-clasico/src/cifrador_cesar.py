#!/usr/bin/env python3
"""Versión 1: Cifrador y Descifrador César Básico"""

def cifrar_cesar(texto: str, clave: int) -> str:
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            resultado += chr((ord(char) - base + clave) % 26 + base)
        else:
            resultado += char
    return resultado

def descifrar_cesar(texto: str, clave: int) -> str:
    return cifrar_cesar(texto, -clave)

if __name__ == "__main__":
    mensaje = "HOLA MUNDO"
    clave = 3
    cifrado = cifrar_cesar(mensaje, clave)
    descifrado = descifrar_cesar(cifrado, clave)
    
    print(f"Texto original: {mensaje} | Clave: {clave} | Texto cifrado: {cifrado} | Descifrado: {descifrado}")