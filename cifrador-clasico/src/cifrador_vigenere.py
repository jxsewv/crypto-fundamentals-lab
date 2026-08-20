#!/usr/bin/env python3
"""Versión 2: Cifrador y Descifrador Vigenère Polialfabético"""

def cifrar_vigenere(texto: str, clave: str) -> str:
    resultado = []
    clave = clave.upper()
    idx = 0
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(clave[idx % len(clave)]) - ord('A')
            resultado.append(chr((ord(char) - base + shift) % 26 + base))
            idx += 1
        else:
            resultado.append(char)
    return "".join(resultado)

def descifrar_vigenere(texto: str, clave: str) -> str:
    resultado = []
    clave = clave.upper()
    idx = 0
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(clave[idx % len(clave)]) - ord('A')
            resultado.append(chr((ord(char) - base - shift) % 26 + base))
            idx += 1
        else:
            resultado.append(char)
    return "".join(resultado)

if __name__ == "__main__":
    mensaje = "Ataque al amanecer a las 05:00 AM!"
    clave = "SECRETO"
    cifrado = cifrar_vigenere(mensaje, clave)
    descifrado = descifrar_vigenere(cifrado, clave)
    
    print(f"Texto Original : {mensaje}")
    print(f"Clave          : {clave}")
    print(f"Texto Cifrado  : {cifrado}")
    print(f"Texto Descifrado: {descifrado}")