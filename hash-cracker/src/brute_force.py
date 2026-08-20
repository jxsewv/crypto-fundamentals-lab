"""
brute_force.py

Fuerza bruta sobre un hash: genera todas las combinaciones posibles
hasta una longitud máxima y las compara contra el objetivo.

ADVERTENCIA: Solo práctica con contraseñas cortas (máx 5-6 chars).
Contraseñas largas tardan horas/días/años con hardware convencional.

Autor: [José Jiménez]
"""
import hashlib
import itertools
import string
import time

CHARSETS = {
    "numeros":    string.digits,
    "lowercase":  string.ascii_lowercase,
    "mixto":      string.ascii_letters + string.digits,
    "completo":   string.ascii_letters + string.digits + string.punctuation,
}

def brute_force(hash_objetivo: str, algoritmo: str, charset: str, longitud_max: int) -> str | None:
    """
    Genera combinaciones de 'charset' de longitud 1 a 'longitud_max'
    y compara su hash contra 'hash_objetivo'.

    Args:
        hash_objetivo (str): Hash en hexadecimal a crackear.
        algoritmo (str): "md5", "sha256", "sha1".
        charset (str): Conjunto de caracteres a usar.
        longitud_max (int): Longitud máxima a intentar.

    Returns:
        str | None: Contraseña encontrada o None.
    """
    func_hash = getattr(hashlib, algoritmo.lower(), None)
    if not func_hash:
        print(f"[-] Algoritmo no soportado: {algoritmo}")
        return None

    intentos = 0
    inicio = time.time()

    for longitud in range(1, longitud_max + 1):
        print(f"[*] Probando longitud {longitud}...")
        for combo in itertools.product(charset, repeat=longitud):
            candidato = "".join(combo)
            hash_candidato = func_hash(candidato.encode()).hexdigest()
            intentos += 1

            if hash_candidato == hash_objetivo:
                duracion = time.time() - inicio
                print(f"\n[+] ¡Contraseña encontrada!: {candidato}")
                print(f"[+] Intentos: {intentos:,}")
                print(f"[+] Tiempo: {duracion:.2f} segundos")
                return candidato

    print(f"\n[-] No encontrado. Intentos: {intentos:,}")
    return None

if __name__ == "__main__":
    print("=== Fuerza Bruta ===")
    print("ADVERTENCIA: Úsalo con contraseñas cortas (máx 5 chars) para ver resultados rápido.\n")
    hash_obj    = input("Hash objetivo: ").strip()
    algoritmo   = input("Algoritmo (md5 / sha256 / sha1): ").strip()
    print("Charset disponible: numeros | lowercase | mixto | completo")
    charset_key = input("Charset: ").strip()
    longitud    = int(input("Longitud máxima a probar: ").strip())

    charset = CHARSETS.get(charset_key, string.ascii_lowercase)
    brute_force(hash_obj, algoritmo, charset, longitud)