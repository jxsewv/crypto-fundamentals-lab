# 🔐 Crypto Fundamentals Lab

**Autor:** Jose Hernández
**Lenguaje:** Python 3 | Bash
**Enfoque:** Criptografía aplicada | Integridad de archivos | Cracking de credenciales

---

## Descripción general

Proyectos de la Fase 1 de mi ruta de aprendizaje en ciberseguridad.
Cada script fue construido desde cero para entender qué pasa "debajo del cofre"
de los mecanismos de seguridad que herramientas modernas dan por sentado.

---

## Índice de proyectos

| Proyecto | Problema que resuelve | Estado |
|---|---|---|
| [Cifrador César / Vigenère](./cifrador-clasico/) | Implementación manual de cifrado simétrico por sustitución | ✅ Completado |
| [Hash Cracker](./hash-cracker/) | Auditoría de contraseñas débiles mediante fuerza bruta y diccionario | ✅ Completado |
| [File Integrity Monitor](./file-integrity-monitor/) | Detección de modificaciones no autorizadas en archivos del sistema | ✅ Completado |

---

## Cifrador César / Vigenère

**Problema:** Entender la lógica de cifrado simétrico antes de estudiar AES o RSA
requiere implementar desde cero los mecanismos más simples de sustitución.

**Solución:** Script de consola que cifra y descifra texto usando ambos algoritmos,
con análisis de frecuencia para romper César sin conocer la clave.

**Aplicación:** Base teórica para comprender por qué los cifrados modernos
necesitan ser computacionalmente irreversibles.

→ [`cifrador-clasico/`](./cifrador-clasico/)

---

## Hash Cracker

**Problema:** Las auditorías de seguridad requieren evaluar la fortaleza real de
contraseñas almacenadas. Sin herramientas propias, no se comprende el proceso.

**Solución:** Script Python con soporte para MD5, SHA1 y SHA256, capaz de
ataques por diccionario (RockYou) y fuerza bruta configurable.

**Aplicación:** Usado para demostrar en laboratorio por qué las políticas de
contraseñas y el salting son críticos en bases de datos.

→ [`hash-cracker/`](./hash-cracker/)

---

## File Integrity Monitor

**Problema:** Detectar si un atacante que ya obtuvo acceso modificó archivos
críticos del sistema sin dejar rastro visible.

**Solución:** Script Bash que genera una línea base de hashes SHA-256 para
archivos seleccionados y ejecuta verificación periódica vía cron.
Alerta inmediata si cualquier hash no coincide.

**Aplicación:** Concepto fundamental detrás de herramientas como Tripwire o AIDE,
usadas en entornos de producción reales.

→ [`file-integrity-monitor/`](./file-integrity-monitor/)

---

## Filosofía de desarrollo

**Primero el concepto, luego la herramienta** — cada script existe para entender
qué hace una herramienta profesional antes de usarla como caja negra.

**Output documentado** — cada script genera salida estructurada apta para
incluirse directamente en reportes de auditoría.

**Uso ético** — todos los proyectos se ejecutan en entornos propios y controlados.

---

## Repositorios relacionados

| Repositorio | Descripción |
|---|---|
| [network-security-tools](enlace) | Fase 2: reconocimiento y análisis de tráfico |
| [defense-and-web-lab](enlace) | Fase 3: defensa activa y seguridad web |

---

## Configuración

\`\`\`bash
git clone https://github.com/tu-usuario/crypto-fundamentals-lab.git
cd crypto-fundamentals-lab
pip install -r requirements.txt
\`\`\`

*Contacto: [LinkedIn](enlace) | Disponible para residencias/internships*
