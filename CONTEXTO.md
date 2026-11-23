# Contexto del proyecto (para retomar en otra sesión de Claude)

Resumen de la conversación en la que se armó este repo. Angel (rol: **Logística**, equipo **DRN-DMUB**) lo usa para que otra sesión, por ejemplo en Claude Code, pueda seguir con el trabajo sin empezar de cero.

## El proyecto
- Proyecto Final U5 de Cálculo Vectorial (ACF-0904), TecNM Campus Ensenada, Dr. Tizoc Fernando Huerta García.
- Repo del profe: https://github.com/Thuerta2398/calculo-vectorial-u5-dron-sistemas (consola `index.html`, guía, ejemplo DEMO y plantilla).
- Modelo: E = ε·ℓ − W. Una ruta es factible si E ≤ 0.8·E_bat.
- Roles: Logística (W₁, W₂), Dinámica (div y rot en V), Zona (I₂ e I₃), Calidad (W₃ y Green). Python lo hace todo el equipo.
- Rotación en el video: Logística explica Dinámica, Dinámica explica Zona, Zona explica Calidad y Calidad explica Logística.
- Entrega: un PDF (portada con folio, enlace al video y enlace al código, más un reporte de máximo 4 cuartillas). La fecha que mencionó el equipo es el **miércoles 25 de noviembre de 2026**.
- La duración del video se contradice: el enunciado dice de 4:30 a 10 min, pero la guía y la penalización dicen 4:30–5:30. Pendiente de confirmar con el profe.

## Resultados de DMUB (verificados con integración numérica)
| Cantidad | Valor |
|---|---|
| W₁ | −6.25 kJ |
| W₂ | −0.50 kJ |
| W₃ | 23.80 kJ |
| div F(V), con V = (2.5, 0.75) | 0.375 N/km |
| rot F(V) | −2.75 N/km |
| I₂ | −5.75 kJ |
| I₃ | −30.05 kJ |
| E₁, E₂, E₃ | 46.25, 42.78, 39.03 kJ |
| Factibles (≤ 44 kJ) | Rutas 2 y 3 |
| Ruta más económica | **Ruta 3** (E_mín = 39.03 kJ) |

## Desarrollo de Logística (a mano)
- W₁: sobre y = 0, ∫₀⁵ (−2 + 0.3x) dx = −10 + 3.75 = −6.25
- W₂: con x = t, y = 0.12t(5 − t) y y′ = 0.6 − 0.24t, se separa en cuatro términos:
  ∫(−2 + 0.3t) = −6.25, ∫0.5y² = +0.75, ∫5y′ = 0, ∫0.05y²y′ = 0, ∫−2t·y′ = +5, total −0.50.
  Los dos ceros salen porque son derivadas exactas (de 5y y de 0.05y³/3) y y(0) = y(5) = 0.

## Estado del código
- `dron_dmub.py`: datos de DMUB pegados. Logística está completa. `F` tiene un stub temporal.
- `prueba_logistica.py`: aserciones que comparan W₁ y W₂ contra los valores a mano. Pasa.
- El programa completo truena con `NotImplementedError` hasta que todos los `TODO` estén hechos, porque el bloque `__main__` llama a todas las funciones.

## Preferencias de Angel al trabajar código
- Dar los rangos exactos de líneas antes de pegar código nuevo.
- Comparar el código original contra el corregido con comentarios `#`.
- Conservar sus comentarios y explicar el porqué en lenguaje sencillo.
