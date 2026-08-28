# Verificador de Integridad de Archivos

### Hashing | Monitoreo Automatizado | Bash Scripting | Detección de Intrusión | Cron

**Autor:** Jose Jiménez 
**Lenguajes:** Bash · Python 3  
**Área:** Integridad de datos | Detección de cambios | Automatización | Fase 1 del roadmap

---

## El Problema

Cuando un atacante logra acceso a un sistema, una de sus primeras acciones es 
modificar archivos críticos: agregar una cuenta en `/etc/passwd`, alterar
configuraciones de SSH, plantar un backdoor. Sin un mecanismo de verificación
de integridad, ese cambio puede pasar desapercibido indefinidamente.

Herramientas como Tripwire o AIDE existen exactamente para este problema —
pero usarlas sin entender qué hacen internamente convierte la seguridad
en una caja negra. Este proyecto construye el mismo mecanismo desde cero.

---

## La Solución

Monitor de integridad de archivos en tres versiones de complejidad creciente:
desde Bash puro con `sha256sum` hasta un monitor en Python con soporte para
directorios completos, detección de archivos nuevos y exportación de reportes
en JSON para integración con pipelines de seguridad o SIEM.

El monitoreo se automatiza mediante `cron` para ejecutarse sin intervención manual.

---

## Aplicación en seguridad

La verificación de integridad de archivos es un control del dominio **DE.CM**
(Detect: Continuous Monitoring) del NIST Cybersecurity Framework y un
requerimiento explícito del estándar PCI-DSS (sección 11.5) en entornos que
procesan datos de tarjetas de pago.

Este proyecto implementa el concepto central de ese control: cualquier modificación
no autorizada a un archivo crítico genera una alerta inmediata y trazable.

→ [`docs/practica-file-integrity.pdf`](./docs/practica-file-integrity.pdf) — Documento completo con teoría y desarrollo

---

## Capacidades implementadas

| Función | Script | Descripción |
|---|---|---|
| Generación de baseline | `fim.sh` / `fim.py` | Registra hashes SHA-256 de archivos monitoreados |
| Detección de modificaciones | `fim.sh` / `fim.py` | Alerta si el hash actual difiere del original |
| Detección de eliminaciones | `fim.sh` / `fim.py` | Alerta si un archivo vigilado desaparece |
| Detección de archivos nuevos | `fim.py` | Alerta si aparece un archivo no registrado en baseline |
| Reporte con timestamp | `fim_report.sh` / `fim.py` | Log con fecha/hora de cada verificación |
| Monitoreo de directorios | `fim.py` | Expande directorios completos automáticamente |
| Export JSON | `fim.py --json` | Salida estructurada compatible con SIEM |
| Automatización | cron | Verificación periódica sin intervención manual |

---

## Versiones del proyecto

### Versión 1 — Monitor Bash básico
**Archivo:** `src/fim.sh`

La lógica más simple posible: genera una baseline de hashes con `sha256sum`
y compara en la siguiente ejecución. Output con colores para distinguir
estado OK vs alerta de un vistazo.

\`\`\`bash
# Generar línea base
bash src/fim.sh baseline

# Verificar integridad
bash src/fim.sh check
\`\`\`

![Baseline creation](./images/baseline-creation.png)

---

### Versión 2 — Reporte con logging persistente
**Archivo:** `src/fim_report.sh`

Añade logging automático en `logs/` con timestamp en cada verificación
y un resumen ejecutivo al final: total de archivos, modificados, eliminados
y alertas. Cada ejecución genera su propio archivo de log.

\`\`\`bash
bash src/fim_report.sh baseline
bash src/fim_report.sh check
\`\`\`

**Nuevo en V2:**
- Log persistente guardado en `logs/fim_YYYY-MM-DD_HH-MM-SS.log`
- Resumen ejecutivo con contadores al final de cada verificación
- Función `tee` para escribir simultáneamente en pantalla y en archivo

![No changes detected](./images/no-changes-detected.png)
![Tamper detected](./images/tamper-detected.png)

---

### Versión 3 — Monitor Python con soporte completo
**Archivo:** `src/fim.py`

Versión completa en Python: monitorea archivos individuales y directorios
enteros, detecta archivos nuevos que no estaban en la baseline y exporta
el reporte en JSON para integración con pipelines de análisis o SIEM.

\`\`\`bash
# Generar baseline
python src/fim.py baseline

# Verificar integridad
python src/fim.py check

# Verificar y exportar reporte JSON
python src/fim.py check --json
\`\`\`

**Nuevo en V3:**
- Soporte para directorios completos en `watchlist.txt`
- Detección de archivos **nuevos** no presentes en la baseline
- Lectura de archivos grandes en bloques de 64 KB (sin cargar en memoria)
- Export a `logs/fim_report_TIMESTAMP.json` compatible con SIEM

---

## Automatización con cron

La diferencia entre un script de práctica y un monitor real es la ejecución automática.

\`\`\`bash
# Abrir editor de cron
crontab -e

# Ejecutar verificación cada 30 minutos
*/30 * * * * /ruta/al/proyecto/src/fim_report.sh check >> /ruta/al/proyecto/logs/cron.log 2>&1

# Verificar que quedó activo
crontab -l
\`\`\`

![Cron setup](./images/cron-setup.png)

---

## Cómo probar el monitor (simulación de ataque)

\`\`\`bash
# 1. Crear archivo de prueba y registrar su baseline
echo "estado original del archivo" > ~/lab/archivo_prueba.txt
bash src/fim.sh baseline

# 2. Simular modificación no autorizada
echo "modificacion no autorizada" >> ~/lab/archivo_prueba.txt

# 3. El monitor detecta el cambio
bash src/fim.sh check
# Output esperado: [✗ MODIFICADO] ~/lab/archivo_prueba.txt
\`\`\`

---

## Uso completo

\`\`\`bash
git clone https://github.com/tu-usuario/crypto-fundamentals-lab.git
cd crypto-fundamentals-lab/file-integrity-monitor

# Editar la lista de archivos a vigilar
nano config/watchlist.txt

# Elegir versión a usar:
bash src/fim.sh baseline && bash src/fim.sh check         # V1 — Bash básico
bash src/fim_report.sh baseline && bash src/fim_report.sh check  # V2 — Con logging
python src/fim.py baseline && python src/fim.py check --json     # V3 — Python + JSON
\`\`\`

---

## Conexión con los proyectos anteriores

Este proyecto reutiliza directamente el concepto de hash del Proyecto 2, pero
con un objetivo distinto: no se trata de **romper** un hash, sino de usar su
**determinismo** como garantía de que nada cambió.

| Proyecto 2 | Proyecto 3 |
|---|---|
| El hash como problema: contraseñas débiles | El hash como solución: integridad de archivos |
| Atacar hashes → fuerza bruta y diccionario | Confiar en hashes → detección de cambios |
| Confidencialidad | Integridad |

---

## Mejoras planeadas

- **Notificación por email** cuando se detecte una alerta — integrar con `mail` o `sendmail`
- **Algoritmo HMAC** en lugar de hash plano para que la baseline sea resistente a manipulación
- **Modo daemon** con `inotifywait` para detección en tiempo real en lugar de verificación periódica
- **Reporte HTML** autogenerado para visualización más legible que el JSON crudo

---

## Habilidades demostradas

- Bash scripting con manejo de archivos, bucles y salida con colores ANSI
- Python para automatización de seguridad con output estructurado
- Uso de `sha256sum` y `hashlib` para verificación de integridad
- Configuración de tareas programadas con `cron`
- Diseño de herramientas de monitoreo con logging trazable
- Comprensión de los pilares CIA: aplicación práctica de **Integridad**

---

*Parte de [`crypto-fundamentals-lab`](../) · Proyecto 3 de 15 · Fase 1 — Fundamentos*  
*Proyecto anterior: [Hash Cracker](../hash-cracker/) · Siguiente fase: [Escáner de Puertos](../../network-security-tools/port-scanner/)*