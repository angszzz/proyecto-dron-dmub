"""Prueba unitaria de Logística (W1 y W2) · equipo DRN-DMUB
Ejecutar:  python prueba_logistica.py
Compara lo que calcula dron_dmub.py contra el desarrollo a mano.
"""
from dron_dmub import trabajo

W1_mano = -6.25   # ∫(-2 + 0.3x) dx de 0 a 5
W2_mano = -0.50   # -6.25 + 0.75 + 0 + 0 + 5

W3_ref  = 23.80   # valor de la consola (el desarrollo a mano de W3 es de Calidad)

W1_py = trabajo(1)
W2_py = trabajo(2)
W3_py = trabajo(3)
print(f"W1: Python = {W1_py:.4f}   a mano = {W1_mano}")
print(f"W2: Python = {W2_py:.4f}   a mano = {W2_mano}")
print(f"W3: Python = {W3_py:.4f}   consola = {W3_ref}")

# assert: si la diferencia no es prácticamente cero, se detiene con el mensaje
assert abs(W1_py - W1_mano) < 1e-6, "W1 no coincide: revisa la Ruta 1 o F"
assert abs(W2_py - W2_mano) < 1e-6, "W2 no coincide: revisa r(t), r'(t) de la Ruta 2"
# W3 se compara con 2 decimales (como el verificador), por eso la tolerancia es 0.01
assert abs(W3_py - W3_ref) < 0.01, "W3 no coincide: revisa r(t), r'(t) o los límites de la Ruta 3"
print("✔ Logística verificada")
