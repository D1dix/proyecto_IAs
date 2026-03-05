# Fundamentos de IA Generativa
### Unidad 1 · Sesión 1 — De Clasificar Patrones a Crear Realidades

Repositorio de ejercicios prácticos de la asignatura **Fundamentos de IA Generativa**.  
Todos los ejercicios están basados en el material de la sesión 1 (diapositivas y guía de ejercicios proporcionados por el profesor).

---

## Materiales de referencia

| Documento | Descripción |
|---|---|
| `U1S1_IAG_ejercicios.pdf` | Guía completa de ejercicios prácticos |
| `U1_S1_Modelos_Generativos.pdf` | Diapositivas teóricas de la sesión (GANs, VAEs, Difusión, LLMs) |

---

## Herramientas utilizadas

| Herramienta | Uso | Enlace |
|---|---|---|
| This Person Does Not Exist | Generación de rostros con GANs | [thispersondoesnotexist.com](https://thispersondoesnotexist.com) |
| Stable Diffusion Web | Generación de imágenes con modelos de difusión | [stablediffusionweb.com](https://stablediffusionweb.com) |
| ConvNetJS VAE Demo | Exploración del espacio latente de un VAE | [cs.stanford.edu/people/karpathy/convnetjs/demo/vae.html](https://cs.stanford.edu/people/karpathy/convnetjs/demo/vae.html) |

---

## Resumen de ejercicios

### Ejercicio 1 — Explorando Modelos Generativos de Imágenes
Exploración práctica de dos tipos de modelos generativos. Se generaron rostros con GANs observando artefactos típicos en zonas como orejas, dientes y pelo. Con Stable Diffusion se generaron tres imágenes a partir de prompts de texto, evaluando calidad y adherencia. Se concluye con una comparativa entre ambas técnicas.

**Prompts utilizados:**
- *"A cat sitting on a laptop, photorealistic"*
- *"A futuristic city at sunset, cyberpunk style"*
- *"A medieval knight riding a horse, oil painting"*

---

### Ejercicio 2 — Análisis de Arquitectura GAN
Análisis del diagrama de entrenamiento de una GAN. Se estudió el flujo de información entre Generador y Discriminador, la dinámica de entrenamiento y los problemas más comunes como el **Mode Collapse** y los **Vanishing Gradients**.

---

### Ejercicio 3 — Espacio Latente en VAEs
Exploración visual del espacio latente de un VAE entrenado sobre MNIST. Se observó cómo los dígitos similares se agrupan en zonas cercanas y cómo las fronteras entre clusters producen transiciones suaves. Se implementó el siguiente código de interpolación lineal:

```python
import numpy as np

def interpolate_latent(z1, z2, steps=10):
    interpolated = []
    for i in range(steps):
        t = i / (steps - 1)
        z_interp = z1 * (1 - t) + z2 * t
        interpolated.append(z_interp)
    return interpolated

z1 = np.array([1.0, 0.5])   # Punto que genera un "3"
z2 = np.array([-0.5, -1.0]) # Punto que genera un "8"

puntos = interpolate_latent(z1, z2, steps=5)
for i, z in enumerate(puntos):
    print(f"Paso {i}: {z}")
```

---

### Ejercicio 4 — Comparativa de Técnicas Generativas
Análisis de 4 casos de uso reales para determinar qué técnica generativa es más adecuada en cada contexto.

| Caso | Técnica recomendada |
|---|---|
| App de filtros en tiempo real | GANs |
| Generación de arte para NFTs | Modelos de Difusión |
| Aumento de datos médicos | VAEs |
| Compresión de imágenes para archivo | VAEs |

---

### Ejercicio 5 — Quiz de Conceptos
Evaluación de conceptos clave. Todas las respuestas correctas:

- **P1:** Los generativos aprenden P(X,Y), los discriminativos P(Y|X)
- **P2:** El Generador recibe gradientes muy pequeños y deja de aprender
- **P3:** La función de pérdida promedia sobre variaciones, perdiendo detalles
- **P4:** La divergencia KL regulariza el espacio latente hacia N(0,1)
- **P5:** Requieren múltiples pasos de denoising iterativo (20-1000 pasos)

---

### Ejercicio Extra — Investigación: DALL-E 3
Investigación sobre DALL-E 3 de OpenAI, el modelo text-to-image más usado actualmente al estar integrado en ChatGPT. Combina un modelo de difusión con GPT-4 para la optimización automática de prompts. Disponible vía ChatGPT Plus y API de OpenAI.

**Fuentes:** [openai.com/dall-e-3](https://openai.com/dall-e-3) · Betker et al. (2023) — *Improving Image Generation with Better Captions*

---

## Lo aprendido

- Diferencia entre modelos discriminativos y generativos
- Cómo funcionan internamente las GANs, VAEs y modelos de difusión
- Problemas típicos del entrenamiento de GANs (Mode Collapse, Vanishing Gradients)
- Qué es el espacio latente y por qué permite interpolación coherente
- Cómo elegir la técnica generativa adecuada según el caso de uso
- Limitaciones éticas de las herramientas de generación de imágenes

---

*Unidad 1 · Sesión 1 | Fundamentos de IA Generativa*
