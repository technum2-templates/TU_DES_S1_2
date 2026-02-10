#!/bin/bash

echo "---------------------------------------------------"
echo "🚀 Lancement de la vérification des exercices..."
echo "---------------------------------------------------"

# 1. Vérification de la structure
python3 check_exercises.py
if [ $? -ne 0 ]; then
    echo ""
    echo "❌ La structure de vos fichiers n'est pas correcte."
    echo "Vérifiez les messages ci-dessus avant de continuer."
    exit 1
fi

# 2. Exécution des tests avec pytest
echo ""
echo "✅ Structure validée. Exécution des tests unitaires..."
echo ""

pytest seance_unique/ --tb=short -v

if [ $? -eq 0 ]; then
    echo ""
    echo "---------------------------------------------------"
    echo "🎉 Félicitations ! Tous les tests sont passés."
    echo "N'oubliez pas de commit et push votre travail."
    echo "---------------------------------------------------"
else
    echo ""
    echo "---------------------------------------------------"
    echo "❌ Certains tests ont échoué."
    echo "Analysez les erreurs ci-dessus pour corriger votre code."
    echo "---------------------------------------------------"
fi
