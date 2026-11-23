"""Prueba unitaria de Logística (W1 y W2) · equipo DRN-DMUB
Ejecutar:  python prueba_logistica.py
Compara lo que calcula dron_dmub.py contra el desarrollo a mano.
"""
from dron_dmub import trabajo

W1_mano = -6.25   # ∫(-2 + 0.3x) dx de 0 a 5
W2_mano = -0.50   # -6.25 + 0.75 + 0 + 0 + 5

W1_py = trabajo(1)
W2_py = trabajo(2)
print(f"W1: Python = {W1_py:.4f}   a mano = {W1_mano}")
print(f"W2: Python = {W2_py:.4f}   a mano = {W2_mano}")

# assert: si la diferencia no es prácticamente cero, se detiene con el mensaje
assert abs(W1_py - W1_mano) < 1e-6, "W1 no coincide: revisa la Ruta 1 o F"
assert abs(W2_py - W2_mano) < 1e-6, "W2 no coincide: revisa r(t), r'(t) de la Ruta 2"
print("✔ Logística verificada")
