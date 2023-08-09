import unittest
import xmlrunner
from qaMain import test_challenge  # Reemplaza con el nombre de tu módulo de pruebas

if __name__ == "__main__":
    # Crea una suite de pruebas
    test_suite = unittest.TestLoader().loadTestsFromTestCase(test_challenge)

    # Ejecuta las pruebas y genera el informe XML
    runner = xmlrunner.XMLTestRunner(output="reports")  # Crea la carpeta "reports" si no existe
    runner.run(test_suite)