# Toxic Text Detector - Sistema de Detección de Toxicidad

Sistema de análisis de toxicidad en textos que utiliza inteligencia artificial para identificar y clasificar contenido ofensivo, amenazante o dañino en tiempo real.

## Tabla de Contenidos

- [Descripción General](#descripción-general)
- [Características](#características)
- [Arquitectura del Sistema](#arquitectura-del-sistema)
- [Stack Tecnológico](#stack-tecnológico)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Documentación de la API](#documentación-de-la-api)
- [Rendimiento del Modelo](#rendimiento-del-modelo)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Despliegue con Docker](#despliegue-con-docker)
- [Ejemplos de Uso](#ejemplos-de-uso)
- [Desarrollo](#desarrollo)
- [Pruebas](#pruebas)
- [Contribuir](#contribuir)
- [Licencia](#licencia)
- [Contacto](#contacto)

## Descripción General

Toxic Text Detector es un sistema de clasificación de toxicidad en textos que analiza contenido de entrada y proporciona:

- **Clasificación de Toxicidad**: Detecta 6 tipos de contenido tóxico usando el modelo toxic-bert
- **Análisis en Tiempo Real**: Respuesta inmediata con porcentajes de confianza
- **Historial de Predicciones**: Almacenamiento persistente de análisis realizados
- **Interfaz Web Intuitiva**: Frontend moderno y responsive para fácil interacción
- **API REST**: Endpoints documentados para integración con otros sistemas

**Versión Actual**: 1.0.0  
**Modelo**: toxic-bert (Hugging Face)  
**Framework**: Transformers + PyTorch  
**Estado**: Listo para producción

## Características

### Funcionalidad Principal

#### Clasificación con Modelo Pre-entrenado
- Modelo toxic-bert de Hugging Face
- 6 categorías de toxicidad:
  - Toxic (Tóxico general)
  - Severe Toxic (Toxicidad severa)
  - Obscene (Obsceno)
  - Threat (Amenazas)
  - Insult (Insultos)
  - Identity Hate (Odio por identidad)
- Análisis multiclase con probabilidades por categoría
- Procesamiento con Transformers y PyTorch

#### Sistema de Historial
- Almacenamiento persistente en SQLite
- Registro de timestamp, texto, resultado y confianza
- Consulta de histórico mediante API
- Base de datos relacional con SQLAlchemy

#### Interfaz de Usuario
- Diseño responsive (escritorio, tablet, móvil)
- Degradado morado moderno y profesional
- Visualización detallada de resultados
- Historial en tiempo real con actualización automática
- Indicadores visuales por tipo de toxicidad

### Aspectos Técnicos Destacados

- Arquitectura API RESTful con FastAPI
- Documentación automática con Swagger
- Diseño sin estado para escalabilidad
- Manejo robusto de errores
- CORS habilitado para integración con frontend
- Containerización completa con Docker
- Imagen publicada en DockerHub

## Arquitectura del Sistema

```
┌─────────────────────────────────────────────────────────┐
│                     USUARIO                              │
│                  (Navegador Web)                         │
└────────────────────┬────────────────────────────────────┘
                     │
                     │ HTTP Request/Response
                     ▼
┌─────────────────────────────────────────────────────────┐
│                   FRONTEND                               │
│              (HTML + CSS + JavaScript)                   │
│  • Formulario de entrada de texto                        │
│  • Visualización de resultados                           │
│  • Historial de análisis                                 │
└────────────────────┬────────────────────────────────────┘
                     │
                     │ fetch/axios (JSON)
                     ▼
┌─────────────────────────────────────────────────────────┐
│                  BACKEND - API                           │
│                    (FastAPI)                             │
│                                                          │
│  Endpoints:                                              │
│  • GET  /           → Documentación                      │
│  • POST /predict    → Analizar texto                     │
│  • GET  /history    → Consultar historial               │
│  • GET  /health     → Estado del servicio               │
└─────────┬──────────────────────┬────────────────────────┘
          │                      │
          │                      │
          ▼                      ▼
┌──────────────────┐   ┌────────────────────────┐
│   MODELO IA      │   │   BASE DE DATOS        │
│  (toxic-bert)    │   │     (SQLite3)          │
│                  │   │                        │
│ • Transformers   │   │  Tabla: predictions    │
│ • PyTorch        │   │  • id                  │
│ • Pre-entrenado  │   │  • timestamp           │
│                  │   │  • text                │
│ Categorías:      │   │  • is_toxic            │
│ • toxic          │   │  • main_category       │
│ • severe_toxic   │   │  • confidence          │
│ • obscene        │   │  • labels (JSON)       │
│ • threat         │   │                        │
│ • insult         │   │                        │
│ • identity_hate  │   │                        │
└──────────────────┘   └────────────────────────┘
          │                      │
          └──────────┬───────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│                    DOCKER                                │
│              (Contenedor aislado)                        │
│  • Empaqueta toda la aplicación                          │
│  • Portabilidad garantizada                              │
│  • Imagen publicada en DockerHub                         │
└─────────────────────────────────────────────────────────┘
```

### Flujo de Datos

1. **Entrada del Usuario**: Mensaje recibido en el frontend
2. **Envío a Backend**: POST request a `/predict` con JSON
3. **Preprocesamiento**: Validación de entrada con Pydantic
4. **Análisis del Modelo**: toxic-bert procesa el texto
5. **Clasificación**: Predicción con probabilidades por categoría
6. **Almacenamiento**: Resultado guardado en SQLite
7. **Respuesta JSON**: Datos enviados al frontend
8. **Visualización**: Usuario ve resultados formateados

## Stack Tecnológico

### Backend

| Componente | Tecnología | Versión |
|------------|-----------|---------|
| Framework | FastAPI | 0.104.1 |
| Servidor ASGI | Uvicorn | 0.24.0 |
| ML Framework | Transformers | 4.35.2 |
| Deep Learning | PyTorch | 2.1.1 |
| ORM | SQLAlchemy | 2.0.23 |
| Validación | Pydantic | 2.5.0 |
| Base de Datos | SQLite3 | Built-in |
| Procesamiento Numérico | NumPy | <2.0 |

### Frontend

- **Marcado**: HTML5
- **Estilos**: CSS3 con gradientes personalizados
- **Scripting**: JavaScript Vanilla (ES6+)
- **Fuentes**: Sans-serif del sistema
- **Colores**: Degradado morado (#667eea → #764ba2)

### DevOps y Despliegue

- **Containerización**: Docker
- **Registry**: DockerHub (angiediazs/toxic-text-detector)
- **Control de Versiones**: Git/GitHub
- **Tamaño de Imagen**: 8.2GB (incluye modelo completo)

### Herramientas de Desarrollo

- **Editor de Código**: Visual Studio Code
- **Pruebas de API**: cURL, Postman
- **DevTools de Navegador**: Chrome/Safari Inspector
- **Gestión de Paquetes**: pip

## Instalación

### Prerequisitos

- Python 3.11 o superior
- pip (gestor de paquetes de Python)
- Git
- Docker (opcional, para deployment)

### Opción 1: Instalación Local

#### 1. Clonar el repositorio

```bash
git clone https://github.com/AngieDiaz25/Toxic_Text_Detector.git
cd Toxic_Text_Detector
```

#### 2. Crear entorno virtual

```bash
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

#### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

**Nota**: La primera vez que ejecutes la aplicación, el modelo toxic-bert se descargará automáticamente (~500MB). Esto puede tardar varios minutos.

#### 4. Ejecutar la aplicación

```bash
uvicorn app.main:app --reload
```

La aplicación estará disponible en `http://localhost:8000`

### Opción 2: Usando Docker

#### 1. Descargar imagen desde DockerHub

```bash
docker pull angiediazs/toxic-text-detector:latest
```

#### 2. Ejecutar contenedor

```bash
docker run -d -p 8000:8000 --name toxic-detector angiediazs/toxic-text-detector:latest
```

#### 3. Acceder a la aplicación

Abrir navegador en `http://localhost:8000`

#### 4. Detener contenedor

```bash
docker stop toxic-detector
docker rm toxic-detector
```

## Configuración

### Variables de Entorno

Actualmente no se requieren variables de entorno. La aplicación funciona out-of-the-box.

### Configuración de Base de Datos

La base de datos SQLite se crea automáticamente en la primera ejecución:

```
predictions.db
```

**Esquema de la tabla `predictions`:**

```sql
CREATE TABLE predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    text TEXT NOT NULL,
    is_toxic BOOLEAN NOT NULL,
    main_category VARCHAR(50),
    confidence FLOAT,
    labels TEXT  -- JSON serializado
);
```

## Documentación de la API

### URL Base

- **Local**: `http://localhost:8000`
- **Docker**: `http://localhost:8000`

### Endpoints

#### 1. Página Principal

```
GET /
```

**Respuesta**: HTML con interfaz web completa

---

#### 2. Verificación de Estado

```
GET /health
```

**Respuesta de Éxito (200 OK)**:

```json
{
  "status": "healthy",
  "model": "toxic-bert",
  "version": "1.0.0"
}
```

---

#### 3. Predecir Toxicidad

```
POST /predict
Content-Type: application/json
```

**Cuerpo de la Solicitud**:

```json
{
  "text": "You are stupid!"
}
```

**Respuesta de Éxito (200 OK)**:

```json
{
  "text": "You are stupid!",
  "is_toxic": true,
  "main_category": "toxic",
  "confidence": 0.9882,
  "labels": {
    "toxic": 0.9882,
    "insult": 0.9526,
    "obscene": 0.728,
    "severe_toxic": 0.0366,
    "identity_hate": 0.0124,
    "threat": 0.0013
  }
}
```

**Respuesta de Error (400 Bad Request)**:

```json
{
  "detail": "El texto no puede estar vacío"
}
```

**Respuesta de Error (500 Internal Server Error)**:

```json
{
  "detail": "Error interno del servidor"
}
```

---

#### 4. Obtener Historial

```
GET /history?limit=10
```

**Parámetros de Query**:
- `limit` (opcional): Número de resultados a retornar (default: 10, max: 100)

**Respuesta de Éxito (200 OK)**:

```json
{
  "total": 3,
  "predictions": [
    {
      "id": 3,
      "timestamp": "2024-12-04T12:30:45",
      "text": "You are stupid!",
      "is_toxic": true,
      "main_category": "toxic",
      "confidence": 0.9882,
      "labels": {
        "toxic": 0.9882,
        "insult": 0.9526,
        "obscene": 0.728,
        "severe_toxic": 0.0366,
        "identity_hate": 0.0124,
        "threat": 0.0013
      }
    },
    ...
  ]
}
```

---

#### 5. Documentación Interactiva (Swagger)

```
GET /docs
```

Interfaz interactiva de Swagger UI para probar todos los endpoints.

---

### Códigos de Estado HTTP

| Código | Significado |
|--------|-------------|
| 200 | OK - Solicitud exitosa |
| 400 | Bad Request - Datos inválidos |
| 500 | Internal Server Error - Error del servidor |

## Rendimiento del Modelo

### Modelo: toxic-bert (unitary/toxic-bert)

**Información General**:
- **Fuente**: Hugging Face Model Hub
- **Arquitectura**: BERT (Bidirectional Encoder Representations from Transformers)
- **Entrenamiento**: Pre-entrenado en datasets de toxicidad de gran escala
- **Parámetros**: ~110M parámetros
- **Idioma**: Optimizado para inglés (funciona con otros idiomas con menor precisión)

### Categorías de Clasificación

El modelo clasifica el texto en 6 categorías de toxicidad:

| Categoría | Descripción | Ejemplos |
|-----------|-------------|----------|
| **toxic** | Toxicidad general | Lenguaje rudo, agresivo |
| **severe_toxic** | Toxicidad severa | Contenido extremadamente ofensivo |
| **obscene** | Contenido obsceno | Lenguaje vulgar, sexual |
| **threat** | Amenazas | Amenazas de violencia |
| **insult** | Insultos | Ataques personales directos |
| **identity_hate** | Odio por identidad | Discriminación por raza, religión, etc. |

### Umbrales de Confianza

- **Alto** (>0.7): Clasificación muy confiable
- **Medio** (0.4-0.7): Clasificación moderadamente confiable
- **Bajo** (<0.4): Clasificación de baja confianza

### Limitaciones del Modelo

- Optimizado principalmente para texto en inglés
- Puede tener dificultad con sarcasmo o ironía
- El contexto cultural puede afectar la precisión
- Sesgo potencial hacia ciertos tipos de lenguaje o comunidades
- No detecta toxicidad implícita o muy sutil

## Estructura del Proyecto

```
Toxic_Text_Detector/
├── app/
│   ├── __init__.py              # Inicialización del paquete
│   ├── main.py                  # Aplicación FastAPI principal
│   ├── inference.py             # Clase ToxicityDetector
│   ├── database.py              # Configuración de SQLAlchemy
│   ├── models.py                # Modelos de base de datos
│   └── schemas.py               # Esquemas Pydantic
├── frontend/
│   ├── index.html               # Estructura HTML
│   ├── style.css                # Estilos CSS
│   └── script.js                # Lógica JavaScript
├── .dockerignore                # Archivos ignorados por Docker
├── .gitignore                   # Archivos ignorados por Git
├── Dockerfile                   # Instrucciones de construcción Docker
├── requirements.txt             # Dependencias Python
├── test_model.py                # Script de prueba del modelo
├── predictions.db               # Base de datos SQLite (generado)
└── README.md                    # Este archivo
```

### Descripción de Archivos Clave

**app/main.py**: 
- Aplicación principal de FastAPI
- Define endpoints REST
- Integra modelo, base de datos y frontend
- Configuración de CORS

**app/inference.py**:
- Clase `ToxicityDetector`
- Carga y gestión del modelo toxic-bert
- Método `predict()` para clasificación
- Procesamiento de resultados

**app/database.py**:
- Configuración de SQLAlchemy
- Creación de engine y sesiones
- Función `get_db()` para dependency injection

**app/models.py**:
- Modelo ORM `Prediction`
- Esquema de tabla de base de datos
- Métodos helper para JSON

**app/schemas.py**:
- Esquemas Pydantic para validación
- `TextInput`: Validación de entrada
- `PredictionOutput`: Formato de respuesta

**frontend/**: 
- Interfaz web completa
- Diseño responsive con CSS Grid
- Comunicación async con API mediante Fetch
- Actualización en tiempo real del historial

**Dockerfile**:
- Imagen base: `python:3.11-slim`
- Instalación de dependencias
- Copia de código fuente
- Exposición del puerto 8000
- Comando de inicio con uvicorn

## Despliegue con Docker

### Construcción de la Imagen

```bash
# Construir imagen localmente
docker build -t toxic-text-detector:latest .

# Etiquetar para DockerHub
docker tag toxic-text-detector:latest tu-usuario/toxic-text-detector:latest

# Subir a DockerHub
docker push tu-usuario/toxic-text-detector:latest
```

### Ejecución del Contenedor

```bash
# Ejecutar en modo detached
docker run -d -p 8000:8000 --name toxic-detector angiediazs/toxic-text-detector:latest

# Ver logs
docker logs toxic-detector

# Seguir logs en tiempo real
docker logs -f toxic-detector

# Detener contenedor
docker stop toxic-detector

# Eliminar contenedor
docker rm toxic-detector

# Ver contenedores en ejecución
docker ps

# Ver todas las imágenes
docker images
```

### Docker Compose (Opcional)

Crear `docker-compose.yml`:

```yaml
version: '3.8'

services:
  toxic-detector:
    image: angiediazs/toxic-text-detector:latest
    ports:
      - "8000:8000"
    restart: unless-stopped
    container_name: toxic-detector
```

Ejecutar:

```bash
docker-compose up -d
docker-compose down
```

## Ejemplos de Uso

### Ejemplos con cURL

#### Predicción Básica

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "Have a wonderful day!"}'
```

#### Detección de Contenido Tóxico

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "You are stupid and I hate you!"}'
```

#### Obtener Historial

```bash
curl http://localhost:8000/history?limit=5
```

#### Verificar Estado

```bash
curl http://localhost:8000/health
```

### Ejemplo en Python

```python
import requests

API_URL = "http://localhost:8000/predict"

def analizar_toxicidad(texto):
    response = requests.post(
        API_URL,
        json={"text": texto},
        headers={"Content-Type": "application/json"}
    )
    return response.json()

# Ejemplo de uso
resultado = analizar_toxicidad("You are amazing!")
print(f"Texto: {resultado['text']}")
print(f"Es tóxico: {resultado['is_toxic']}")
print(f"Categoría principal: {resultado['main_category']}")
print(f"Confianza: {resultado['confidence']:.2%}")
print(f"\nDesglose por categoría:")
for categoria, score in resultado['labels'].items():
    print(f"  {categoria}: {score:.2%}")
```

### Ejemplo en JavaScript

```javascript
const API_URL = 'http://localhost:8000/predict';

async function analizarToxicidad(texto) {
  try {
    const response = await fetch(API_URL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text: texto }),
    });
    
    if (!response.ok) {
      throw new Error('Error en la petición');
    }
    
    const datos = await response.json();
    return datos;
  } catch (error) {
    console.error('Error:', error);
    throw error;
  }
}

// Ejemplo de uso
analizarToxicidad('This is a test message')
  .then(resultado => {
    console.log('Es tóxico:', resultado.is_toxic);
    console.log('Categoría:', resultado.main_category);
    console.log('Confianza:', resultado.confidence);
    console.log('Labels:', resultado.labels);
  })
  .catch(error => {
    console.error('Error al analizar:', error);
  });
```

### Integración con React

```jsx
import { useState } from 'react';

function ToxicityChecker() {
  const [text, setText] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const checkToxicity = async () => {
    setLoading(true);
    try {
      const response = await fetch('http://localhost:8000/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text }),
      });
      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.error('Error:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <textarea 
        value={text} 
        onChange={(e) => setText(e.target.value)}
        placeholder="Escribe un texto para analizar..."
      />
      <button onClick={checkToxicity} disabled={loading}>
        {loading ? 'Analizando...' : 'Analizar'}
      </button>
      {result && (
        <div>
          <p>Resultado: {result.is_toxic ? 'Tóxico' : 'No tóxico'}</p>
          <p>Categoría: {result.main_category}</p>
          <p>Confianza: {(result.confidence * 100).toFixed(2)}%</p>
        </div>
      )}
    </div>
  );
}
```

## Desarrollo

### Prerequisitos para Desarrollo

- Python 3.11+
- pip
- Git
- Editor de código (VS Code recomendado)
- Docker (opcional)
- Postman o similar para pruebas de API

### Configurar Entorno de Desarrollo

#### 1. Fork y clonar repositorio

```bash
git clone https://github.com/TU_USUARIO/Toxic_Text_Detector.git
cd Toxic_Text_Detector
```

#### 2. Crear rama de característica

```bash
git checkout -b feature/nombre-de-tu-caracteristica
```

#### 3. Instalar en modo desarrollo

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### 4. Realizar cambios y probar

```bash
# Ejecutar servidor de desarrollo
uvicorn app.main:app --reload

# En otra terminal, probar cambios
curl http://localhost:8000/health
```

#### 5. Commit con mensajes descriptivos

```bash
git add .
git commit -m "feat: Añadir nueva funcionalidad"
```

#### 6. Push y crear pull request

```bash
git push origin feature/nombre-de-tu-caracteristica
```

### Guías de Estilo de Código

#### Python (Backend)

- Seguir guía de estilo PEP 8
- Usar type hints donde sea aplicable
- Documentar funciones con docstrings
- Longitud máxima de línea: 100 caracteres
- Usar f-strings para formateo de strings

```python
# Bueno
def predict(self, text: str) -> Dict:
    """
    Analiza un texto y devuelve predicción de toxicidad.
    
    Args:
        text: Texto a analizar
        
    Returns:
        Dict con resultados de la predicción
    """
    if not text or len(text.strip()) == 0:
        raise ValueError("El texto no puede estar vacío")
    ...
```

#### JavaScript (Frontend)

- Usar características ES6+
- Preferir `const` y `let` sobre `var`
- Usar funciones flecha para callbacks
- Documentar funciones complejas con comentarios JSDoc
- Nombres descriptivos de variables

```javascript
// Bueno
const analyzeText = async () => {
    const text = document.getElementById('textInput').value;
    if (!text.trim()) {
        alert('Por favor escribe un texto');
        return;
    }
    ...
};
```

#### CSS

- Usar convención de nomenclatura BEM donde sea aplicable
- Diseño responsive mobile-first
- Agrupar propiedades relacionadas
- Comentar selectores complejos

### Convención de Mensajes de Commit

- `feat:` Nueva característica
- `fix:` Corrección de bug
- `docs:` Cambios en documentación
- `style:` Cambios de estilo de código (formato, etc.)
- `refactor:` Refactorización de código
- `test:` Añadir o actualizar pruebas
- `chore:` Tareas de mantenimiento

## Pruebas

### Pruebas Manuales del Backend

```bash
# Probar endpoint de estado
curl http://localhost:8000/health

# Probar predicción con texto no tóxico
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "Have a nice day!"}'

# Probar predicción con texto tóxico
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "You are stupid!"}'

# Probar historial
curl http://localhost:8000/history?limit=5

# Probar caso de error (texto vacío)
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": ""}'
```

### Pruebas del Frontend

1. Abrir DevTools del navegador (F12)
2. Ir a la pestaña Console
3. Probar funcionalidad de chat manualmente:
   - Enviar texto vacío (debería validar)
   - Enviar texto tóxico
   - Enviar texto no tóxico
   - Verificar actualización del historial
   - Hacer clic en botón "Actualizar"
4. Verificar diseño responsive:
   - Desktop (>1024px)
   - Tablet (768px-1024px)
   - Móvil (<768px)

### Casos de Prueba Recomendados

#### Textos No Tóxicos

```
"Have a wonderful day!"
"This is a great project"
"I love learning new things"
"Thank you for your help"
"Machine learning is fascinating"
```

#### Textos Tóxicos

```
"You are stupid!"
"I hate you"
"You are worthless"
"Go to hell"
"You are an idiot"
```

#### Casos Extremos

```
""                          # Texto vacío
"a"                        # Un solo carácter
"😊😊😊"                    # Solo emojis
"AAAA" * 500              # Texto muy largo
"   "                     # Solo espacios
```

### Verificar Rendimiento

```bash
# Medir tiempo de respuesta
time curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "test"}'
```

**Tiempos esperados**:
- Primera predicción (carga del modelo): <3000ms
- Predicciones subsecuentes: <500ms
- Docker (primera vez): <5000ms
- Docker (subsecuente): <1000ms

## Contribuir

Las contribuciones son bienvenidas. Por favor, sigue estas pautas:

### Cómo Contribuir

1. Fork del repositorio
2. Crear una rama de característica (`git checkout -b feature/CaracteristicaAsombrosa`)
3. Realizar tus cambios
4. Probar exhaustivamente
5. Commit de tus cambios (`git commit -m 'feat: Añadir CaracteristicaAsombrosa'`)
6. Push a la rama (`git push origin feature/CaracteristicaAsombrosa`)
7. Abrir un Pull Request

### Pautas para Pull Requests

- Proporcionar descripción clara de los cambios
- Referenciar issues relacionados si aplica
- Incluir resultados de pruebas
- Actualizar documentación si es necesario
- Seguir el estilo de código existente
- Asegurar que todas las pruebas pasen

### Reportar Issues

Al reportar issues, por favor incluye:

- Descripción clara del problema
- Pasos para reproducir
- Comportamiento esperado vs real
- Detalles del entorno (SO, versión de Python, Docker, etc.)
- Mensajes de error o capturas de pantalla si aplica

### Solicitudes de Características

Para solicitudes de características, por favor describe:

- Caso de uso y motivación
- Solución propuesta o enfoque de implementación
- Impacto potencial en funcionalidad existente

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver abajo para detalles:

### Licencia MIT

Copyright (c) 2024 Angie Díaz

Por la presente se concede permiso, libre de cargos, a cualquier persona que obtenga una copia
de este software y de los archivos de documentación asociados (el "Software"), para utilizar
el Software sin restricción, incluyendo sin limitación los derechos de usar, copiar, modificar,
fusionar, publicar, distribuir, sublicenciar, y/o vender copias del Software, y para permitir
a las personas a las que se les proporcione el Software hacer lo mismo, sujeto a las siguientes
condiciones:

El aviso de copyright anterior y este aviso de permiso se incluirán en todas las copias o
porciones sustanciales del Software.

EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O IMPLÍCITA,
INCLUYENDO PERO NO LIMITADO A GARANTÍAS DE COMERCIALIZACIÓN, IDONEIDAD PARA UN PROPÓSITO
PARTICULAR Y NO INFRACCIÓN. EN NINGÚN CASO LOS AUTORES O TITULARES DEL COPYRIGHT SERÁN
RESPONSABLES DE NINGUNA RECLAMACIÓN, DAÑOS U OTRAS RESPONSABILIDADES, YA SEA EN UNA ACCIÓN
DE CONTRATO, AGRAVIO O CUALQUIER OTRO MOTIVO, QUE SURJA DE O EN CONEXIÓN CON EL SOFTWARE O
EL USO U OTROS TRATOS EN EL SOFTWARE.

## Consideraciones Éticas

### Disclaimers Importantes

**Esta es una herramienta de detección, no un sistema de censura:**

- El detector proporciona clasificaciones basadas en patrones aprendidos
- No es un juez absoluto de lo que es "aceptable" o no
- El contexto cultural y social es importante
- Los usuarios deben usar su propio juicio

**Limitaciones de Responsabilidad:**

- El sistema puede tener falsos positivos y falsos negativos
- No detecta todas las formas de toxicidad (sarcasmo, contexto implícito)
- Optimizado para inglés, puede tener menor precisión en otros idiomas
- No es un sustituto del juicio humano en moderación de contenido

### Privacidad y Datos

- **No se almacenan datos personales**: Solo se guarda el texto analizado y resultados
- **Sin tracking**: No se rastrea información del usuario
- **API sin estado**: No se mantiene sesión entre peticiones
- **Base de datos local**: Los datos permanecen en tu servidor/contenedor
- **Sin cookies**: La aplicación no usa cookies de terceros

### Uso Responsable

Este sistema está diseñado para:

✓ Moderación de contenido en plataformas
✓ Análisis de comentarios en redes sociales
✓ Detección de contenido ofensivo en chats
✓ Investigación sobre discurso tóxico online
✓ Educación sobre comunicación respetuosa

**No debe usarse para:**

✗ Censura indiscriminada sin revisión humana
✗ Discriminación o targeting de usuarios
✗ Violación de privacidad
✗ Aplicación de políticas sin contexto

## Agradecimientos

- **Hugging Face**: Por el modelo toxic-bert y la librería Transformers
- **FastAPI**: Por el excelente framework web
- **PyTorch**: Por el framework de deep learning
- **SQLAlchemy**: Por el ORM robusto
- **Docker**: Por la plataforma de containerización
- **Comunidad Open Source**: Por las innumerables herramientas y recursos

## Hoja de Ruta

### Versión 1.1 (Planificada)

- [ ] Soporte multiidioma (español, francés, alemán)
- [ ] Endpoint para análisis por lotes
- [ ] Exportar historial como CSV/JSON
- [ ] Dashboard de estadísticas
- [ ] Autenticación básica con API keys

### Versión 2.0 (Futuro)

- [ ] Fine-tuning del modelo para dominios específicos
- [ ] Detección de intensidad de toxicidad
- [ ] Sistema de reportes detallados
- [ ] Integración con sistemas de moderación
- [ ] Aplicación móvil (React Native)
- [ ] Panel de administración web

## Contacto

**Autora**: Angie Díaz

- **GitHub**: [@AngieDiaz25](https://github.com/AngieDiaz25)
- **Proyecto**: [Toxic_Text_Detector](https://github.com/AngieDiaz25/Toxic_Text_Detector)

**Enlaces del Proyecto**:

- **Repositorio**: https://github.com/AngieDiaz25/Toxic_Text_Detector
- **DockerHub**: https://hub.docker.com/r/angiediazs/toxic-text-detector
- **Issues**: https://github.com/AngieDiaz25/Toxic_Text_Detector/issues

---

**Versión**: 1.0.0  
**Última actualización**: Diciembre 2024  
**Estado**: Activo y en mantenimiento

---

⭐ Si este proyecto te ha sido útil, por favor dale una estrella en GitHub ⭐
