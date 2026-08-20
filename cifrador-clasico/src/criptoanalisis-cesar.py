#!/usr/bin/env python3
"""Versión 3: Criptoanálisis de Fuerza Bruta y Análisis de Frecuencia para César"""

from cifrador_cesar import descifrar_cesar

# Frecuencias relativas promedio de letras en español
FREQ_ES = {'E': 13.68, 'A': 12.53, 'O': 8.68, 'L': 8.37, 'S': 7.98, 'N': 6.71, 'D': 5.86, 'R': 6.87, 'I': 6.25, 'U': 3.93}

def puntuar_texto(texto: str) -> float:
    return sum(FREQ_ES.get(char.upper(), 0) for char in texto)

def romper_cesar(texto_cifrado: str):
    candidatos = []
    for shift in range(1, 26):
        intento = descifrar_cesar(texto_cifrado, shift)
        score = puntuar_texto(intento)
        candidatos.append((score, shift, intento))
    
    candidatos.sort(reverse=True, key=lambda x: x[0])
    
    print("=== ATAQUE DE FUERZA BRUTA Y RANKING DE FRECUENCIA ===")
    for score, shift, texto in candidatos[:5]:
        print(f"[Puntaje: {score:6.2f}] Desplazamiento {shift:02d} -> {texto}")

if __name__ == "__main__":
    texto_interceptado = "KROD PXQGR"
    romper_cesar(texto_interceptado)