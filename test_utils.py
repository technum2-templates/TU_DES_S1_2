"""
Utilitaires pour les feedbacks optimisés des tests
Fournit des messages d'erreur détaillés, des indices et des comparaisons
"""
import unittest
import re
from typing import Any, Callable, List, Tuple


class OptimizedTestCase(unittest.TestCase):
    """Classe de test avec feedbacks optimisés et indices progressifs"""
    
    # Couleurs et symboles pour le feedback visuel
    PASS = "✅"
    FAIL = "❌"
    HINT = "💡"
    INFO = "ℹ️"
    WARN = "⚠️"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hints_given = 0
        self.max_hints = 3
    
    def assertPatternMatches(self, pattern: str, text: str, should_match: bool = True, 
                            hint_level: int = 1):
        """
        Assertion avancée pour les patterns regex avec feedback détaillé
        
        Args:
            pattern: Le pattern regex à tester
            text: Le texte à tester
            should_match: True si le pattern doit matcher, False sinon
            hint_level: Niveau d'indice (1=basique, 2=moyen, 3=détaillé)
        """
        try:
            match = re.match(pattern, text) if should_match else re.search(pattern, text)
            result = match is not None
            expected = should_match
            
            if result == expected:
                print(f"{self.PASS} Pattern valide")
                return
            
            # Feedback d'erreur détaillé
            error_msg = self._build_regex_error_message(
                pattern, text, result, expected, hint_level
            )
            self.fail(error_msg)
            
        except re.error as e:
            self.fail(
                f"{self.FAIL} Erreur de pattern regex:\n"
                f"  Pattern: {pattern}\n"
                f"  Erreur: {str(e)}\n"
                f"{self.HINT} Conseil: Vérifiez la syntaxe de votre pattern"
            )
    
    def _build_regex_error_message(self, pattern: str, text: str, 
                                   result: bool, expected: bool, hint_level: int) -> str:
        """Construit un message d'erreur détaillé pour les patterns regex"""
        msg = f"\n{self.FAIL} Pattern regex invalide\n"
        msg += f"  Pattern: {pattern}\n"
        msg += f"  Texte testé: {text}\n"
        msg += f"  Résultat: {'Matche ✓' if result else 'Ne matche pas ✗'}\n"
        msg += f"  Attendu: {'Doit matcher' if expected else 'Ne doit pas matcher'}\n"
        
        # Indices progressifs
        if hint_level >= 1:
            msg += f"\n{self.HINT} Indice 1: Vérifiez que votre pattern couvre tous les cas\n"
        
        if hint_level >= 2:
            msg += f"{self.HINT} Indice 2: Testez votre pattern avec des cas limites\n"
            msg += f"  - Cas vide: ''\n"
            msg += f"  - Cas spéciaux: caractères spéciaux, espaces\n"
        
        if hint_level >= 3:
            msg += f"{self.HINT} Indice 3: Composants du pattern:\n"
            msg += f"  - ^ : début de chaîne\n"
            msg += f"  - $ : fin de chaîne\n"
            msg += f"  - . : n'importe quel caractère\n"
            msg += f"  - * : 0 ou plus\n"
            msg += f"  - + : 1 ou plus\n"
            msg += f"  - ? : 0 ou 1\n"
            msg += f"  - [abc] : l'un de a, b, ou c\n"
            msg += f"  - [a-z] : plage de caractères\n"
        
        return msg
    
    def assertFunctionReturns(self, func: Callable, args: tuple, expected: Any,
                             hint_level: int = 1):
        """
        Assertion pour les fonctions avec comparaison attendu/réel
        
        Args:
            func: La fonction à tester
            args: Les arguments à passer à la fonction
            expected: La valeur attendue
            hint_level: Niveau d'indice (1-3)
        """
        try:
            result = func(*args)
            
            if result == expected:
                print(f"{self.PASS} Résultat correct")
                return
            
            # Feedback détaillé
            error_msg = self._build_function_error_message(
                func, args, result, expected, hint_level
            )
            self.fail(error_msg)
            
        except Exception as e:
            error_msg = (
                f"\n{self.FAIL} Erreur lors de l'exécution de {func.__name__}\n"
                f"  Arguments: {args}\n"
                f"  Erreur: {type(e).__name__}: {str(e)}\n"
                f"{self.HINT} Conseil: Vérifiez que votre fonction gère tous les cas"
            )
            self.fail(error_msg)
    
    def _build_function_error_message(self, func: Callable, args: tuple, 
                                      result: Any, expected: Any, hint_level: int) -> str:
        """Construit un message d'erreur détaillé pour les fonctions"""
        msg = f"\n{self.FAIL} Résultat incorrect\n"
        msg += f"  Fonction: {func.__name__}\n"
        msg += f"  Arguments: {args}\n"
        msg += f"  Résultat obtenu: {result!r}\n"
        msg += f"  Résultat attendu: {expected!r}\n"
        
        # Comparaison détaillée
        if isinstance(result, (int, float)) and isinstance(expected, (int, float)):
            diff = abs(result - expected)
            msg += f"  Différence: {diff}\n"
        
        if isinstance(result, str) and isinstance(expected, str):
            msg += f"  Longueur obtenue: {len(result)}, attendue: {len(expected)}\n"
        
        # Indices progressifs
        if hint_level >= 1:
            msg += f"\n{self.HINT} Indice 1: Vérifiez la logique de votre fonction\n"
        
        if hint_level >= 2:
            msg += f"{self.HINT} Indice 2: Testez avec des cas simples d'abord\n"
            msg += f"  - Cas minimal\n"
            msg += f"  - Cas normal\n"
            msg += f"  - Cas limite\n"
        
        if hint_level >= 3:
            msg += f"{self.HINT} Indice 3: Vérifiez:\n"
            msg += f"  - Les types de données\n"
            msg += f"  - Les conditions if/else\n"
            msg += f"  - Les boucles\n"
            msg += f"  - Les valeurs de retour\n"
        
        return msg
    
    def assertObjectHasAttribute(self, obj: Any, attr: str, hint_level: int = 1):
        """
        Assertion pour vérifier les attributs d'objet avec feedback
        
        Args:
            obj: L'objet à tester
            attr: Le nom de l'attribut
            hint_level: Niveau d'indice (1-3)
        """
        if hasattr(obj, attr):
            print(f"{self.PASS} Attribut '{attr}' trouvé")
            return
        
        error_msg = f"\n{self.FAIL} Attribut manquant\n"
        error_msg += f"  Classe: {obj.__class__.__name__}\n"
        error_msg += f"  Attribut attendu: {attr}\n"
        error_msg += f"  Attributs disponibles: {dir(obj)}\n"
        
        if hint_level >= 1:
            error_msg += f"\n{self.HINT} Indice 1: Assurez-vous que l'attribut est défini\n"
        
        if hint_level >= 2:
            error_msg += f"{self.HINT} Indice 2: Vérifiez l'orthographe et la casse\n"
        
        if hint_level >= 3:
            error_msg += f"{self.HINT} Indice 3: Pour les classes:\n"
            error_msg += f"  - Attributs d'instance: définis dans __init__\n"
            error_msg += f"  - Attributs de classe: définis au niveau de la classe\n"
        
        self.fail(error_msg)
    
    def assertCoverage(self, test_cases: List[Tuple[Any, Any]], 
                      func: Callable, coverage_types: List[str]):
        """
        Rapport de couverture pour les cas de test
        
        Args:
            test_cases: Liste de tuples (input, expected_output)
            func: La fonction à tester
            coverage_types: Types de cas couverts (normal, limite, erreur, etc.)
        """
        print(f"\n{self.INFO} Rapport de couverture:\n")
        
        passed = 0
        failed = 0
        
        for i, (input_val, expected) in enumerate(test_cases, 1):
            try:
                result = func(input_val)
                if result == expected:
                    print(f"  {self.PASS} Cas {i}: OK")
                    passed += 1
                else:
                    print(f"  {self.FAIL} Cas {i}: Obtenu {result!r}, attendu {expected!r}")
                    failed += 1
            except Exception as e:
                print(f"  {self.FAIL} Cas {i}: Erreur - {str(e)}")
                failed += 1
        
        coverage_pct = (passed / len(test_cases)) * 100 if test_cases else 0
        print(f"\n  Couverture: {passed}/{len(test_cases)} ({coverage_pct:.0f}%)")
        print(f"  Types couverts: {', '.join(coverage_types)}\n")
        
        if failed > 0:
            self.fail(f"{failed} cas de test ont échoué")


class TestReporter:
    """Génère des rapports de test détaillés"""
    
    @staticmethod
    def print_test_summary(test_name: str, passed: int, failed: int, total: int):
        """Affiche un résumé des tests"""
        pct = (passed / total * 100) if total > 0 else 0
        status = "✅ RÉUSSI" if failed == 0 else "❌ ÉCHOUÉ"
        
        print(f"\n{'='*60}")
        print(f"Test: {test_name}")
        print(f"Status: {status}")
        print(f"Résultats: {passed}/{total} ({pct:.0f}%)")
        print(f"{'='*60}\n")
    
    @staticmethod
    def print_hint(level: int, hints: List[str]):
        """Affiche un indice progressif"""
        if level <= len(hints):
            print(f"\n💡 Indice niveau {level}:")
            print(f"   {hints[level-1]}\n")
