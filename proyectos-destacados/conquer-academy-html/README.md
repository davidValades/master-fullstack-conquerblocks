# 🎓 Conquer Academy | HTML Semantic Structure

![Status](https://img.shields.io/badge/Estado-Completado_✅-2ea44f?style=for-the-badge)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)

Primer proyecto práctico del **Master en Desarrollo Web Full Stack** de ConquerBlocks. Este proyecto se centra exclusivamente en la arquitectura, semántica y estructuración de la información mediante HTML5, sentando bases sólidas antes de introducir la capa de presentación (CSS) o interactividad (JavaScript).

## 🎯 Objetivo del Proyecto

Construir el esqueleto completo de una plataforma web para una academia online ("Conquer Academy"). El reto principal ha consistido en estructurar múltiples vistas interconectadas, asegurando una navegación lógica mediante rutas relativas, el uso correcto de etiquetas para SEO básico y una accesibilidad semántica estricta.

## 🧠 Conocimientos Aplicados y Retos Superados

Durante el desarrollo de este proyecto, he consolidado las siguientes habilidades técnicas:

- **Estructura Semántica Avanzada:** Sustitución de `<div>` genéricos por etiquetas con valor semántico (`<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<address>`, `<footer>`) para mejorar la accesibilidad y el SEO.
- **Navegación Relativa (File System):** Dominio de las rutas relativas (`./` y `../`) para interconectar de forma robusta un árbol de directorios con múltiples niveles de profundidad.
- **Formularios e Integridad de Datos:** Maquetación de vistas de Login, Registro y Contacto. Uso avanzado de atributos `type` (`email`, `password`, `date`, `url`, `file`) para forzar la validación nativa del navegador, y configuración del atributo `enctype="multipart/form-data"` para permitir la subida de archivos.
- **Incrustación de Terceros:** Integración de un mapa interactivo de Google Maps utilizando la etiqueta `<iframe>` sin depender de scripts externos.

## 📂 Arquitectura del Proyecto

El proyecto sigue una organización modular de directorios para separar las vistas por su contexto funcional:

```text
conquer-academy-html/
├── assets/                 # Recursos estáticos
│   └── images/             # Imágenes optimizadas (banner.webp)
├── pages/                  # Vistas secundarias agrupadas por dominio
│   ├── auth/
│   │   ├── login.html
│   │   └── registro.html
│   ├── blog/
│   │   ├── blog.html
│   │   ├── noticia1.html
│   │   └── noticia2.html
│   ├── courses/
│   │   ├── cursos.html
│   │   ├── curso-diseno-grafico.html
│   │   ├── curso-javascript.html
│   │   ├── curso-programacion-web.html
│   │   └── curso-python.html
│   ├── legal/
│   │   ├── aviso-legal.html
│   │   ├── politica-privacidad.html
│   │   └── terminos-uso.html
│   ├── contacto.html
│   └── quienes-somos.html
├── index.html              # Landing page principal (Home)
└── README.md               # Documentación del proyecto
```

## 🛠️ Tecnologías Utilizadas

- **Estructura:** HTML5
- **Entorno:** Visual Studio Code
- **Control de Versiones:** Git & GitHub

⭐ Proyecto desarrollado por [David Valadés Navarro](https://github.com/davidValades) como parte del currículo de ConquerBlocks.
