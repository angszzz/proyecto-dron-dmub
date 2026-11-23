# Proyecto Final U5 · Cálculo Vectorial · Equipo DRN-DMUB

Dron de reparto en un campo de viento: elegir, entre tres rutas (recta, parábola y semicircunferencia), la que gasta menos batería.

- Consola de Vuelo: https://thuerta2398.github.io/calculo-vectorial-u5-dron-sistemas/ (código `DRN-DMUB`)
- Plantilla original del profe: https://github.com/Thuerta2398/calculo-vectorial-u5-dron-sistemas

## Datos del equipo

F(x, y) = ⟨ −2 + 0.3x + 0.5y² ,  5 + 0.05y² − 2x ⟩ · L = 5 km · k = 0.12 · ε = 8 kJ/km · E_bat = 55 kJ (máximo por vuelo: 44 kJ)

## Archivos

| Archivo | Qué es |
|---|---|
| `dron_dmub.py` | Plantilla con los datos de DMUB. Cada integrante llena los `TODO` de su rol. |
| `prueba_logistica.py` | Prueba unitaria de Logística (W₁ y W₂ contra el desarrollo a mano). |

## Avance por rol

| Rol | Funciones | Estado |
|---|---|---|
| Logística | Ruta 2, `trabajo()` | ✅ Listo y verificado (W₁ = −6.25, W₂ = −0.50) |
| Dinámica | `F`, `div`, `rot` | ⏳ `F` tiene un stub temporal; falta `div` y `rot` |
| Análisis de Zona | `doble_D2`, `doble_D3` | ⏳ Pendiente |
| Calidad | Ruta 3, `verificar_green` | ⏳ Pendiente |
| Equipo | `longitud`, `energia`, gráfica de barras de energía | ⏳ Pendiente |

## Cómo correr

```bash
pip install numpy scipy matplotlib
python prueba_logistica.py   # prueba solo Logística
python dron_dmub.py          # programa completo (solo corre cuando todos los TODO estén hechos)
```

El programa completo genera `mapa_DRN-DMUB.png`, `energia_DRN-DMUB.png` y `vuelo_DRN-DMUB.gif`.

## Reglas del equipo

1. Antes de subir su bloque, cada quien compara su resultado con el verificador de la consola.
2. Una fórmula equivocada no hace tronar el programa: da números incorrectos sin avisar. Por eso hay que comparar con la consola.
3. Dinámica: al subir `F`, borren el stub temporal.
