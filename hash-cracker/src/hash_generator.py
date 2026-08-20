"""
hash_generator.py

Genera hashes de un texto en múltiples algoritmos simultáneamente.
Sirve para demostrar determinismo, avalancha y diferencias entre algoritmos.

Autor: [José Jiménez]
"""
import hashlib

def generar_hashes(texto: str) -> dict:
    """
    Toma un string y devuelve un diccionario con sus hashes
    en MD5, SHA1, SHA256 y SHA512.

    Args:
        texto (str): El texto a hashear.

    Returns:
        dict: Algoritmo → hash en hexadecimal.
    """
    encoded = texto.encode('utf-8')
    return {
        "MD5":    hashlib.md5(encoded).hexdigest(),
        "SHA1":   hashlib.sha1(encoded).hexdigest(),
        "SHA256": hashlib.sha256(encoded).hexdigest(),
        "SHA512": hashlib.sha512(encoded).hexdigest(),
    }

if __name__ == "__main__":
    texto = input("Texto a hashear: ")
    hashes = generar_hashes(texto)
    print("\n[+] Hashes generados:")
    for algo, valor in hashes.items():
        print(f"    {algo:8} → {valor}")
    print("\n[!] Prueba cambiar una sola letra — todos los hashes serán completamente distintos.")
    print("    Eso es el efecto avalancha.\n")