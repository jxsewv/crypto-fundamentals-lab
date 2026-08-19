# Cifrador y Descifrador César / Vigenère

### Criptografía clásica | Cifrado simétrico | Manipulación de strings | Python 3

**Autor:** José Jiménez  
**Lenguaje:** Python 3  
**Área:** Criptografía | Fundamentos de seguridad

---

## El Problema

Antes de estudiar AES, RSA o cualquier estándar criptográfico moderno, es necesario
entender por qué existen: cuál es la historia de los cifrados, cómo fallaron y qué
los hizo obsoletos.

Sin implementar un cifrado desde cero, herramientas como OpenSSL o GPG son cajas negras.
Este proyecto elimina esa opacidad.

---

## La Solución

Implementación en Python de los dos cifrados simétricos clásicos más importantes:
el Cifrado César (sustitución monoalfabética) y el Cifrado Vigenère (sustitución
polialfabética). El proyecto incluye tanto el cifrador como el descifrador para cada
algoritmo, y un módulo de análisis de frecuencia para romper César sin conocer la clave.

---

## Aplicación en seguridad

El Cifrado César se usa hoy como ejemplo didáctico en auditorías para demostrar
por qué la complejidad computacional importa. El Vigenère fue considerado "irrompible"
durante siglos — entender por qué falló es entender por qué los cifrados modernos
necesitan confusión y difusión (principios de Shannon, 1945), base teórica de AES.

→ [`docs/practica-cifrador.pdf`](./docs/practica-cifrador.pdf) — Documento completo con teoría y desarrollo paso a paso

---

## Capacidades implementadas

| Función | Descripción |
|---|---|
| Cifrado César | Desplazamiento configurable del 1 al 25 sobre el alfabeto |
| Descifrado César | Reversa exacta del desplazamiento |
| Análisis de frecuencia | Ataque de criptoanálisis para romper César sin la clave |
| Cifrado Vigenère | Sustitución polialfabética con clave de texto |
| Descifrado Vigenère | Requiere conocer la clave exacta |

---

## Versiones del proyecto

Este proyecto fue desarrollado en etapas para reflejar un ciclo de desarrollo real.

### Versión 1 — Cifrado César básico
**Archivo:** `src/cifrador_cesar.py`

Implementación mínima: cifra y descifra un texto recibiendo clave numérica.
Diseñado para entender la lógica de sustitución antes de agregar complejidad.

\`\`\`bash
python src/cifrador_cesar.py
\`\`\`

**Output de ejemplo:**
