"""
dict_attack.py

Ataque de diccionario contra un hash MD5 o SHA256.
Compara cada palabra de una wordlist hasheada contra el objetivo.


Uso: python dict_attack.py
Autor: [José Jiménez]

"""
import hashlib
import sys
import time

ALGORITMOS = {
    "md5":    hashlib.md5,
    "sha256": hashlib.sha256,
    "sha1":   hashlib.sha1,
}

def ataque_diccionario(hash_objetivo: str, ruta_wordlist: str, algoritmo: str) -> str | None:
    """
    Itera sobre cada línea de la wordlist, hashea la palabra
    y la compara contra el hash objetivo.

    Args:
        hash_objetivo (str): Hash en hexadecimal a crackear.
        ruta_wordlist (str): Ruta al archivo de wordlist.
        algoritmo (str): Nombre del algoritmo ("md5", "sha256", "sha1").

    Returns:
        str | None: La contraseña encontrada, o None si no se encontró.
    """
    func_hash = ALGORITMOS.get(algoritmo.lower())
    if not func_hash:
        print(f"[-] Algoritmo '{algoritmo}' no soportado.")
        return None

    intentos = 0
    inicio = time.time()

    try:
        with open(ruta_wordlist, "r", encoding="utf-8", errors="ignore") as f:
            for linea in f:
                palabra = linea.strip()
                hash_candidato = func_hash(palabra.encode()).hexdigest()
                intentos += 1

                if hash_candidato == hash_objetivo:
                    duracion = time.time() - inicio
                    print(f"\n[+] ¡Contraseña encontrada!: {palabra}")
                    print(f"[+] Intentos realizados: {intentos:,}")
                    print(f"[+] Tiempo: {duracion:.2f} segundos")
                    return palabra

                if intentos % 100_000 == 0:
                    print(f"[*] {intentos:,} palabras probadas...", end="\r")

    except FileNotFoundError:
        print(f"[-] Wordlist no encontrada: {ruta_wordlist}")
        return None

    print(f"\n[-] Hash no encontrado en la wordlist ({intentos:,} palabras probadas).")
    return None

if __name__ == "__main__":
    print("=== Ataque de Diccionario ===\n")
    hash_obj  = input("Hash objetivo: ").strip()
    wordlist  = input("Ruta a wordlist (ej: wordlists/rockyou.txt): ").strip()
    algoritmo = input("Algoritmo (md5 / sha256 / sha1): ").strip()
    ataque_diccionario(hash_obj, wordlist, algoritmo)