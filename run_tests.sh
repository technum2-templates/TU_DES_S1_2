#!/bin/bash

# Script wrapper pour exécuter les tests avec feedback progressif
# Usage: ./run_tests.sh [seance_1|seance_2] [exercice_number]

export PYTHONPATH=$PYTHONPATH:.

# Couleurs
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}=== Runner de Tests GitHub Classroom ===${NC}"

if [ -z "$1" ]; then
    echo "Exécution de tous les tests..."
    python3 -m pytest seance_1/ seance_2/
else
    SESSION=$1
    if [ -z "$2" ]; then
        echo -e "Exécution des tests pour ${GREEN}${SESSION}${NC}..."
        # Trouver tous les fichiers de test dans la séance
        for test_file in ${SESSION}/test_exercice_*.py; do
            echo -e "\n${BLUE}--- Test: $(basename $test_file) ---${NC}"
            python3 $test_file
        done
    else
        EXERCICE=$2
        TEST_FILE="${SESSION}/test_exercice_${EXERCICE}.py"
        if [ -f "$TEST_FILE" ]; then
            echo -e "Exécution du test ${GREEN}${TEST_FILE}${NC}..."
            python3 $TEST_FILE
        else
            echo "Erreur: Fichier $TEST_FILE non trouvé."
        fi
    fi
fi
