#!/usr/bin/env bash
# fim.sh — File Integrity Monitor v1
# Genera baseline o verifica integridad comparando hashes SHA-256
#
# Uso:
#   ./fim.sh baseline   → genera la línea base
#   ./fim.sh check      → verifica integridad contra la línea base
#
# Autor: José Jiménez

WATCHLIST="config/watchlist.txt"
BASELINE="baseline/baseline.sha256"
VERDE="\033[0;32m"
ROJO="\033[0;31m"
AMARILLO="\033[1;33m"
RESET="\033[0m"

# -------------------------------------------------------
generar_baseline() {
    echo -e "${AMARILLO}[*] Generando línea base de hashes...${RESET}"
    mkdir -p baseline

    > "$BASELINE"  # limpiar archivo anterior

    while IFS= read -r archivo || [[ -n "$archivo" ]]; do
        # Ignorar comentarios y líneas vacías
        [[ "$archivo" =~ ^#.*$ || -z "$archivo" ]] && continue

        if [ -f "$archivo" ]; then
            sha256sum "$archivo" >> "$BASELINE"
            echo -e "  ${VERDE}[+]${RESET} $archivo"
        else
            echo -e "  ${ROJO}[-]${RESET} No encontrado: $archivo"
        fi
    done < "$WATCHLIST"

    echo -e "\n${VERDE}[✓] Línea base guardada en: $BASELINE${RESET}"
    echo -e "${AMARILLO}[!] Guarda este archivo en un lugar seguro — es tu referencia de integridad.${RESET}\n"
}

# -------------------------------------------------------
verificar_integridad() {
    if [ ! -f "$BASELINE" ]; then
        echo -e "${ROJO}[✗] No existe línea base. Ejecuta primero: ./fim.sh baseline${RESET}"
        exit 1
    fi

    echo -e "${AMARILLO}[*] Verificando integridad...${RESET}\n"
    ALERTAS=0

    while IFS= read -r linea; do
        hash_original=$(echo "$linea" | awk '{print $1}')
        archivo=$(echo "$linea" | awk '{print $2}')

        if [ ! -f "$archivo" ]; then
            echo -e "  ${ROJO}[✗ ELIMINADO]${RESET} $archivo"
            ((ALERTAS++))
            continue
        fi

        hash_actual=$(sha256sum "$archivo" | awk '{print $1}')

        if [ "$hash_actual" != "$hash_original" ]; then
            echo -e "  ${ROJO}[✗ MODIFICADO]${RESET} $archivo"
            echo -e "       Esperado: $hash_original"
            echo -e "       Actual:   $hash_actual"
            ((ALERTAS++))
        else
            echo -e "  ${VERDE}[✓ OK]${RESET} $archivo"
        fi
    done < "$BASELINE"

    echo ""
    if [ "$ALERTAS" -eq 0 ]; then
        echo -e "${VERDE}[✓] Integridad verificada — sin cambios detectados.${RESET}\n"
    else
        echo -e "${ROJO}[!] ALERTA: $ALERTAS archivo(s) comprometido(s).${RESET}\n"
    fi
}

# -------------------------------------------------------
case "$1" in
    baseline) generar_baseline ;;
    check)    verificar_integridad ;;
    *)
        echo "Uso: $0 [baseline|check]"
        echo "  baseline → genera línea base de hashes"
        echo "  check    → verifica integridad contra la línea base"
        exit 1
        ;;
esac