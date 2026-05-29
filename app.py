import streamlit as st
import time
import random
import pandas as pd
import plotly.graph_objects as go

# ─── Configuración de la página ───────────────────────────────────────────────
st.set_page_config(
    page_title="AdulTec – Aprendizaje digital para adultos mayores",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── CSS Global ───────────────────────────────────────────────────────────────
def aplicar_css(tema: str):
    if tema == "dark":
        bg        = "#0F1117"
        surface   = "#1C1E26"
        surface2  = "#252836"
        text      = "#F0F2FA"
        muted     = "#8B92A8"
        accent    = "#6C8EF5"
        accent2   = "#A78BFA"
        success   = "#34D399"
        warning   = "#FBBF24"
        danger    = "#F87171"
        border    = "#2E3145"
        card_shadow = "0 4px 24px rgba(0,0,0,0.5)"
    else:
        bg        = "#F7F8FC"
        surface   = "#FFFFFF"
        surface2  = "#EEF1FB"
        text      = "#1A1D2E"
        muted     = "#6B7280"
        accent    = "#4361EE"
        accent2   = "#7C3AED"
        success   = "#059669"
        warning   = "#D97706"
        danger    = "#DC2626"
        border    = "#E2E6F3"
        card_shadow = "0 2px 16px rgba(67,97,238,0.08)"

    st.markdown(f"""
    <style>
    /* ── Imports ── */
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&family=Lora:ital,wght@0,400;0,600;1,400&display=swap');

    /* ── Reset & Base ── */
    html, body, [class*="css"] {{
        font-family: 'Nunito', sans-serif;
        color: {text};
    }}
    .stApp {{ background-color: {bg}; }}
    .main .block-container {{ padding-top: 1.5rem; padding-bottom: 3rem; max-width: 1100px; }}

    /* ── Sidebar ── */
    section[data-testid="stSidebar"] {{
        background: {surface};
        border-right: 1px solid {border};
    }}
    section[data-testid="stSidebar"] .stButton button {{
        background: transparent;
        color: {text};
        border: none;
        border-radius: 12px;
        font-size: 15px;
        font-weight: 600;
        text-align: left;
        padding: 10px 14px;
        width: 100%;
        transition: background 0.2s;
    }}
    section[data-testid="stSidebar"] .stButton button:hover {{
        background: {surface2};
    }}

    /* ── Buttons ── */
    .stButton > button {{
        background: {accent};
        color: #fff;
        border: none;
        border-radius: 14px;
        font-size: 16px;
        font-weight: 700;
        padding: 10px 24px;
        width: 100%;
        transition: opacity 0.2s, transform 0.1s;
        letter-spacing: 0.02em;
    }}
    .stButton > button:hover {{ opacity: 0.88; transform: translateY(-1px); }}
    .stButton > button:active {{ transform: translateY(0); }}

    /* ── Inputs ── */
    .stTextInput input, .stTextArea textarea, .stSelectbox select {{
        background: {surface2} !important;
        border: 1.5px solid {border} !important;
        border-radius: 12px !important;
        color: {text} !important;
        font-size: 16px !important;
        font-family: 'Nunito', sans-serif !important;
    }}
    .stTextInput input:focus, .stTextArea textarea:focus {{
        border-color: {accent} !important;
        box-shadow: 0 0 0 3px {accent}22 !important;
    }}

    /* ── Progress bar ── */
    .stProgress > div > div > div {{ background: linear-gradient(90deg, {accent}, {accent2}); border-radius: 8px; }}
    .stProgress > div > div {{ background: {surface2}; border-radius: 8px; }}

    /* ── Tabs ── */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 8px;
        background: {surface2};
        border-radius: 14px;
        padding: 4px;
        border: none;
    }}
    .stTabs [data-baseweb="tab"] {{
        border-radius: 10px;
        font-size: 15px;
        font-weight: 700;
        color: {muted};
        padding: 8px 18px;
        background: transparent;
    }}
    .stTabs [aria-selected="true"] {{
        background: {accent} !important;
        color: #fff !important;
    }}

    /* ── Expanders ── */
    .streamlit-expanderHeader {{
        font-size: 17px !important;
        font-weight: 700 !important;
        color: {text} !important;
        background: {surface} !important;
        border-radius: 12px !important;
        border: 1.5px solid {border} !important;
    }}

    /* ── Radio ── */
    .stRadio label {{ font-size: 17px !important; font-weight: 600; }}
    .stRadio [data-testid="stMarkdownContainer"] p {{ font-size: 17px; }}

    /* ── Alerts ── */
    .stSuccess, .stError, .stWarning, .stInfo {{
        border-radius: 12px !important;
        font-size: 16px !important;
        font-weight: 600 !important;
    }}

    /* ── Divider ── */
    hr {{ border-color: {border}; margin: 1.5rem 0; }}

    /* ── Custom components ── */
    .hero-title {{
        font-family: 'Lora', serif;
        font-size: 2.6rem;
        font-weight: 600;
        line-height: 1.2;
        color: {text};
        margin-bottom: 0.3rem;
    }}
    .hero-sub {{
        font-size: 1.15rem;
        color: {muted};
        font-weight: 600;
        margin-bottom: 1.5rem;
    }}
    .badge {{
        display: inline-block;
        padding: 3px 12px;
        border-radius: 99px;
        font-size: 12px;
        font-weight: 800;
        letter-spacing: 0.05em;
        text-transform: uppercase;
    }}
    .badge-premium {{ background: linear-gradient(90deg,{accent},{accent2}); color:#fff; }}
    .badge-free {{ background: {success}22; color: {success}; border: 1px solid {success}44; }}
    .badge-new {{ background: {warning}22; color: {warning}; border: 1px solid {warning}44; }}

    .card {{
        background: {surface};
        border: 1.5px solid {border};
        border-radius: 20px;
        padding: 22px 24px;
        box-shadow: {card_shadow};
        margin-bottom: 18px;
        transition: box-shadow 0.2s;
    }}
    .card:hover {{ box-shadow: 0 6px 32px {accent}22; }}

    .plan-card {{
        background: {surface};
        border: 2px solid {border};
        border-radius: 22px;
        padding: 28px 22px;
        text-align: center;
        height: 100%;
        transition: border-color 0.2s, box-shadow 0.2s;
    }}
    .plan-card.featured {{
        border-color: {accent};
        box-shadow: 0 0 0 4px {accent}18;
    }}
    .plan-price {{
        font-size: 2.2rem;
        font-weight: 900;
        color: {accent};
        line-height: 1;
    }}
    .plan-period {{ font-size: 14px; color: {muted}; font-weight: 600; }}
    .plan-name {{ font-size: 1.1rem; font-weight: 800; color: {text}; margin-bottom: 6px; }}
    .plan-feature {{
        display: flex;
        align-items: flex-start;
        gap: 8px;
        text-align: left;
        margin: 8px 0;
        font-size: 15px;
        color: {text};
        font-weight: 600;
    }}
    .plan-feature .check {{ color: {success}; font-size: 17px; flex-shrink: 0; }}

    .testimonial {{
        background: {surface};
        border-left: 4px solid {accent};
        border-radius: 0 16px 16px 0;
        padding: 18px 20px;
        margin-bottom: 14px;
        font-style: italic;
        color: {text};
        font-size: 16px;
    }}
    .testimonial-author {{
        font-style: normal;
        font-weight: 800;
        color: {accent};
        margin-top: 8px;
        font-size: 14px;
    }}

    .stat-box {{
        background: {surface};
        border: 1.5px solid {border};
        border-radius: 16px;
        padding: 18px;
        text-align: center;
    }}
    .stat-number {{
        font-size: 2rem;
        font-weight: 900;
        color: {accent};
        line-height: 1;
    }}
    .stat-label {{ font-size: 13px; color: {muted}; font-weight: 700; margin-top: 4px; }}

    .modulo-nav {{
        background: {surface2};
        border-radius: 14px;
        padding: 6px;
        display: flex;
        gap: 6px;
        flex-wrap: wrap;
        margin-bottom: 20px;
    }}

    .footer {{
        text-align: center;
        margin-top: 40px;
        padding: 16px;
        font-size: 13px;
        color: {muted};
        border-top: 1px solid {border};
    }}

    .whatsapp-btn {{
        position: fixed;
        bottom: 24px;
        right: 24px;
        width: 56px;
        height: 56px;
        background: #25D366;
        color: white;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 28px;
        box-shadow: 0 4px 16px rgba(37,211,102,0.4);
        z-index: 9999;
        text-decoration: none;
        transition: transform 0.2s;
    }}
    .whatsapp-btn:hover {{ transform: scale(1.1); }}

    .quiz-card {{
        background: {surface};
        border: 2px solid {border};
        border-radius: 18px;
        padding: 28px;
        margin-bottom: 16px;
    }}
    .quiz-question {{
        font-size: 1.2rem;
        font-weight: 800;
        color: {text};
        margin-bottom: 20px;
        line-height: 1.4;
    }}
    .result-circle {{
        width: 140px;
        height: 140px;
        border-radius: 50%;
        background: conic-gradient({accent} var(--pct), {surface2} 0);
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 20px;
        position: relative;
    }}
    .result-inner {{
        width: 110px;
        height: 110px;
        border-radius: 50%;
        background: {surface};
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.6rem;
        font-weight: 900;
        color: {accent};
    }}

    /* hide default streamlit menu & footer */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    </style>

    <a href="https://wa.me/5492644000000?text=Hola,%20necesito%20ayuda%20con%20AdulTec" target="_blank">
        <div class="whatsapp-btn">💬</div>
    </a>
    """, unsafe_allow_html=True)


# ─── Datos del curso ───────────────────────────────────────────────────────────
CURSO_INTERNET = {
    "titulo": "Internet para principiantes",
    "descripcion": "Aprenda qué es Internet, cómo navegar con seguridad y comunicarse con sus seres queridos.",
    "nivel": "Básico",
    "duracion": "4 módulos · ~2 horas",
    "modulos": [
        {
            "titulo": "¿Qué es Internet?",
            "icono": "🌐",
            "contenido": """
## 🌐 ¿Qué es Internet?

Internet es una **red mundial de computadoras** conectadas entre sí que permite compartir información y comunicarse al instante, sin importar la distancia.

Piense en Internet como una **gran biblioteca y oficina de correos combinadas**, donde puede:

- 📖 Buscar información sobre cualquier tema
- 💬 Comunicarse con familiares y amigos
- 📋 Realizar trámites y pagos sin salir de casa
- 🎵 Ver fotos, videos y escuchar música

---

### ¿Cómo nos conectamos?

Para conectarnos a Internet necesitamos **tres cosas**:

1. **Un dispositivo** — computadora, celular o tablet
2. **Una conexión** — WiFi del hogar o datos móviles del celular
3. **Un navegador web** — Chrome, Firefox o Edge

> 💡 **Actividad práctica:** Encuentre el ícono del navegador en su dispositivo y practique cómo abrirlo.
            """,
            "video": "https://www.youtube.com/embed/JrF33N9zTCU",
            "quiz": [
                {
                    "pregunta": "¿Qué es Internet?",
                    "opciones": ["Un programa para computadoras", "Una red mundial de computadoras conectadas", "Una compañía de telefonía", "Un tipo de teléfono moderno"],
                    "correcta": 1,
                    "explicacion": "Internet es exactamente eso: una enorme red que conecta millones de computadoras en todo el mundo."
                },
                {
                    "pregunta": "¿Qué necesitamos para conectarnos a Internet?",
                    "opciones": ["Solo un teléfono celular", "Una computadora y un televisor", "Un dispositivo, una conexión y un navegador web", "Una radio y una antena"],
                    "correcta": 2,
                    "explicacion": "Los tres elementos son necesarios: el dispositivo, la conexión (WiFi o datos) y el navegador."
                },
                {
                    "pregunta": "¿Cuál de estos es un navegador web?",
                    "opciones": ["WhatsApp", "Chrome", "Word", "Calculadora"],
                    "correcta": 1,
                    "explicacion": "Chrome es un navegador web. WhatsApp es una app de mensajería, Word es un procesador de texto y Calculadora es una app matemática."
                },
            ],
        },
        {
            "titulo": "Navegación y búsqueda",
            "icono": "🔍",
            "contenido": """
## 🔍 Cómo navegar y buscar información

### Partes del navegador web

El navegador es su **ventana a Internet**. Consta de:

| Parte | Para qué sirve |
|---|---|
| **Barra de direcciones** | Escribir la dirección de una página |
| **Botones ◀ ▶** | Ir hacia atrás o adelante |
| **🔄 Recargar** | Actualizar la página |
| **Pestañas** | Abrir varias páginas a la vez |

---

### Cómo buscar en Google

1. Abra su navegador
2. Escriba **www.google.com** en la barra de direcciones
3. En el cuadro de búsqueda, escriba lo que desea encontrar
4. Presione **Enter** o toque la lupa 🔍
5. Haga clic en el resultado que más le interese

> 💡 **Consejo:** Use palabras clave cortas y específicas. En lugar de "quiero saber el clima de hoy en mi ciudad", escriba simplemente **"clima San Juan"**.
            """,
            "video": "https://www.youtube.com/embed/uy_zQAFx_gQ",
            "quiz": [
                {
                    "pregunta": "¿Dónde escribimos la dirección de una página web?",
                    "opciones": ["En el teclado", "En la barra de direcciones del navegador", "En un mensaje de WhatsApp", "En un papel"],
                    "correcta": 1,
                    "explicacion": "La barra de direcciones, ubicada en la parte superior del navegador, es donde escribimos la dirección (URL) de la página que queremos visitar."
                },
                {
                    "pregunta": "¿Cuál es un motor de búsqueda popular?",
                    "opciones": ["Facebook", "Microsoft Word", "Google", "WhatsApp"],
                    "correcta": 2,
                    "explicacion": "Google es el motor de búsqueda más usado en el mundo. Facebook es una red social, Word es un procesador de texto y WhatsApp es de mensajería."
                },
                {
                    "pregunta": "¿Qué debemos hacer para buscar información efectivamente?",
                    "opciones": ["Escribir oraciones muy largas", "Usar palabras clave específicas", "Usar solo mayúsculas", "Buscar solo imágenes"],
                    "correcta": 1,
                    "explicacion": "Las palabras clave cortas y específicas dan mejores resultados. Las oraciones largas pueden confundir al buscador."
                },
            ],
        },
        {
            "titulo": "Comunicación en línea",
            "icono": "💬",
            "contenido": """
## 💬 Comunicación en línea

### Correo electrónico (Email)

El correo electrónico es como una **carta digital instantánea**. Sus partes son:

- **Dirección:** similar a `su.nombre@gmail.com`
- **Asunto:** breve descripción del mensaje
- **Cuerpo:** el contenido principal
- **Archivos adjuntos:** fotos, documentos, etc.

---

### Videollamadas

Las videollamadas le permiten **ver y escuchar** a sus seres queridos a distancia:

| App | Ideal para |
|---|---|
| **WhatsApp** | Llamadas desde el celular |
| **Zoom** | Reuniones grupales |
| **Google Meet** | Desde el navegador, sin instalar nada |

---

### Redes sociales

- **Facebook** — La más popular entre adultos mayores. Ideal para ver fotos y noticias de la familia.
- **Instagram** — Para compartir fotos y videos.
- **YouTube** — Para ver videos de cualquier tema.

> 💡 **Consejo:** Empiece con WhatsApp. Es la herramienta que más va a usar para comunicarse con su familia.
            """,
            "video": "https://www.youtube.com/embed/Ak6ywKvv3vw",
            "quiz": [
                {
                    "pregunta": "¿Qué es un correo electrónico?",
                    "opciones": ["Un mensaje de texto de celular", "Una carta digital instantánea", "Una llamada telefónica", "Una reunión presencial"],
                    "correcta": 1,
                    "explicacion": "El correo electrónico funciona como una carta, pero se envía y recibe de forma instantánea por Internet."
                },
                {
                    "pregunta": "¿Qué aplicación es ideal para hacer videollamadas desde el celular?",
                    "opciones": ["Microsoft Word", "Calculadora", "WhatsApp", "Bloc de notas"],
                    "correcta": 2,
                    "explicacion": "WhatsApp es la aplicación más popular para videollamadas desde el celular, especialmente para comunicarse con familia."
                },
                {
                    "pregunta": "¿Cuál red social es la más popular entre adultos mayores?",
                    "opciones": ["Facebook", "TikTok", "Snapchat", "LinkedIn"],
                    "correcta": 0,
                    "explicacion": "Facebook es la red social preferida por adultos mayores porque permite estar al tanto de la familia y amigos de forma simple."
                },
            ],
        },
        {
            "titulo": "Seguridad en Internet",
            "icono": "🔒",
            "contenido": """
## 🔒 Seguridad en Internet

### Contraseñas seguras

Una buena contraseña es su **primera línea de defensa**:

✅ Al menos **8 caracteres**
✅ Combine **letras + números + símbolos** (ej: `Casa2024!`)
✅ **Diferente** para cada servicio
❌ Evite fechas de nacimiento, nombres de mascotas o "1234"

---

### ⚠️ Señales de alerta: posibles estafas

Desconfíe si recibe mensajes con:
- Ofertas **demasiado buenas** para ser verdad ("ganó un premio")
- Pedidos **urgentes** de dinero o datos personales
- Errores de ortografía o redacción extraña
- Remitentes desconocidos

---

### Consejos de navegación segura

🔐 No comparta datos bancarios en sitios no confiables
🚪 Cierre sesión cuando termine de usar un servicio
🔄 Mantenga su dispositivo actualizado
📲 Instale solo aplicaciones oficiales (App Store / Play Store)

> ⚠️ **Regla de oro:** Si algo parece sospechoso, no haga clic. Consulte con un familiar antes de actuar.
            """,
            "video": "https://www.youtube.com/embed/PSrKw2R1B9A",
            "quiz": [
                {
                    "pregunta": "¿Qué debe tener una contraseña segura?",
                    "opciones": ["Ser corta y fácil de recordar", "Contener solo números", "Combinar letras, números y símbolos", "Ser la misma para todas las cuentas"],
                    "correcta": 2,
                    "explicacion": "Una contraseña segura combina letras mayúsculas, minúsculas, números y símbolos. La longitud y variedad la hacen difícil de adivinar."
                },
                {
                    "pregunta": "¿Cuál es una señal de posible estafa por Internet?",
                    "opciones": ["Un mensaje de un familiar conocido", "Una oferta demasiado buena para ser verdad", "Un correo de su banco con su logo", "Una factura de un servicio que usa"],
                    "correcta": 1,
                    "explicacion": "Las estafas frecuentemente prometen premios o beneficios exagerados. Si algo parece demasiado bueno, probablemente lo es."
                },
                {
                    "pregunta": "¿Qué debe hacer cuando termina de usar un servicio en línea?",
                    "opciones": ["Apagar el dispositivo inmediatamente", "Guardar la contraseña en un papel visible", "Cerrar sesión", "Dejar la sesión abierta para la próxima vez"],
                    "correcta": 2,
                    "explicacion": "Cerrar sesión evita que otras personas accedan a su cuenta si alguien más usa el dispositivo."
                },
            ],
        },
    ],
}

OTROS_CURSOS = [
    {
        "titulo": "WhatsApp desde cero",
        "descripcion": "Envíe mensajes, fotos y haga videollamadas con familia y amigos. El curso más pedido.",
        "emoji": "📱",
        "progreso": 0.0,
        "premium": False,
        "tag": "Más popular",
    },
    {
        "titulo": "Cómo usar su smartphone",
        "descripcion": "Domine las funciones básicas y avanzadas de su teléfono inteligente.",
        "emoji": "📲",
        "progreso": 0.0,
        "premium": True,
        "tag": "Nuevo",
    },
    {
        "titulo": "Trámites online: ANSES, AFIP y más",
        "descripcion": "Realice gestiones gubernamentales desde la comodidad de su hogar.",
        "emoji": "🏛️",
        "progreso": 0.0,
        "premium": True,
        "tag": None,
    },
    {
        "titulo": "Compras seguras en Internet",
        "descripcion": "Aprenda a comprar en Mercado Libre, supermercados online y más, sin riesgos.",
        "emoji": "🛒",
        "progreso": 0.0,
        "premium": True,
        "tag": "Nuevo",
    },
    {
        "titulo": "Privacidad y seguridad digital",
        "descripcion": "Consejos y herramientas para proteger sus datos personales y navegar sin miedo.",
        "emoji": "🔐",
        "progreso": 0.1,
        "premium": False,
        "tag": None,
    },
]

PLANES = [
    {
        "nombre": "Básico",
        "precio_mes": 8_000,
        "precio_anual": 80_000,
        "mix": 0.311,
        "featured": False,
        "color": "free",
        "emoji": "🌱",
        "features": [
            "3 clases gratuitas para empezar",
            "Acceso a 2 cursos básicos",
            "Comunidad de apoyo",
            "Evaluaciones y quizzes",
            "Contenido con publicidad",
        ],
        "no_incluye": ["Tutorías en grupo", "Certificados", "Soporte prioritario"],
    },
    {
        "nombre": "Estándar",
        "precio_mes": 13_000,
        "precio_anual": 130_000,
        "mix": 0.356,
        "featured": True,
        "color": "premium",
        "emoji": "⭐",
        "features": [
            "Todo el catálogo de cursos",
            "Sin publicidad",
            "Tutorías grupales semanales",
            "Certificados de finalización",
            "Descuento jubilados 20%",
            "7 días de prueba gratis",
        ],
        "no_incluye": ["Tutorías personalizadas", "Soporte prioritario"],
    },
    {
        "nombre": "Premium",
        "precio_mes": 20_000,
        "precio_anual": 200_000,
        "mix": 0.333,
        "featured": False,
        "color": "premium",
        "emoji": "👑",
        "features": [
            "Todo lo del plan Estándar",
            "2 tutorías personalizadas al mes",
            "Soporte técnico prioritario",
            "Configuración remota inicial",
            "Descuento jubilados 20%",
            "Plan familiar (hasta 3 personas)",
        ],
        "no_incluye": [],
    },
]

ARPU = 13_776  # ARS ponderado por mix de encuesta


# ─── Estado de sesión ─────────────────────────────────────────────────────────
def init_state():
    defaults = {
        "pagina": "inicio",
        "tema": "light",
        "logueado": False,
        "nombre": "",
        "modulo": 1,
        "pregunta": 0,
        "correctas": 0,
        "quiz_done": False,
        "quiz_respondida": False,
        "respuesta_elegida": None,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


init_state()
aplicar_css(st.session_state.tema)


# ─── Helpers ──────────────────────────────────────────────────────────────────
def ir(pagina: str):
    st.session_state.pagina = pagina
    st.rerun()


def nav_btn(label: str, pagina: str, key: str = None):
    if st.button(label, key=key or label):
        ir(pagina)


def fmt_ars(n: int) -> str:
    return f"$ {n:,.0f}".replace(",", ".")


def progress_ring_html(pct: int, color: str = "#4361EE") -> str:
    deg = int(pct * 3.6)
    return f"""
    <div style="width:120px;height:120px;border-radius:50%;
                background:conic-gradient({color} {deg}deg,#EEF1FB 0);
                display:flex;align-items:center;justify-content:center;margin:0 auto 12px;">
        <div style="width:88px;height:88px;border-radius:50%;background:#fff;
                    display:flex;align-items:center;justify-content:center;
                    font-size:1.4rem;font-weight:900;color:{color};">{pct}%</div>
    </div>"""


def footer():
    st.markdown("""<div class="footer">AdulTec © 2025 · La experiencia de toda una vida, ahora también en digital</div>""", unsafe_allow_html=True)


# ─── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="text-align:center;padding:10px 0 4px;">
        <span style="font-size:2.4rem;">🎓</span>
        <div style="font-size:1.5rem;font-weight:900;letter-spacing:-0.5px;margin-top:2px;">AdulTec</div>
        <div style="font-size:12px;color:#8B92A8;font-weight:600;margin-bottom:6px;">La academia digital para adultos mayores</div>
    </div>
    """, unsafe_allow_html=True)

    tema_label = "🌙 Modo oscuro" if st.session_state.tema == "light" else "☀️ Modo claro"
    if st.button(tema_label, key="toggle_tema"):
        st.session_state.tema = "dark" if st.session_state.tema == "light" else "light"
        st.rerun()

    st.markdown("---")

    nav_btn("🏠  Inicio", "inicio", "sb_inicio")
    nav_btn("📚  Mis cursos", "cursos", "sb_cursos")
    nav_btn("👥  Comunidad", "comunidad", "sb_comunidad")
    nav_btn("💳  Planes y precios", "planes", "sb_planes")

    st.markdown("---")

    if st.session_state.logueado:
        st.markdown(f"<div style='font-size:14px;font-weight:700;padding:4px 14px;'>👤 {st.session_state.nombre}</div>", unsafe_allow_html=True)
        if st.button("Cerrar sesión", key="sb_logout"):
            st.session_state.logueado = False
            st.session_state.nombre = ""
            ir("inicio")
    else:
        nav_btn("✅  Iniciar sesión", "login", "sb_login")
        nav_btn("📝  Registrarse", "registro", "sb_registro")

    st.markdown("---")
    st.markdown("""
    <div style="font-size:12px;color:#8B92A8;padding:0 14px;font-weight:600;">
        📞 0800-ADULTEC<br>
        📧 ayuda@adultec.com<br>
        Lun–Vie · 9 a 18 hs
    </div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# PÁGINA: INICIO
# ══════════════════════════════════════════════════════════════════════════════
if st.session_state.pagina == "inicio":
    saludo = f"Bienvenido/a, {st.session_state.nombre}! 😊" if st.session_state.logueado else "Bienvenido/a a AdulTec 😊"

    st.markdown(f"""
    <div class="hero-title">{saludo}</div>
    <div class="hero-sub">La academia online de habilidades digitales pensada para adultos mayores 🇦🇷</div>
    """, unsafe_allow_html=True)

    # Stats
    c1, c2, c3, c4 = st.columns(4)
    for col, (num, label) in zip(
        [c1, c2, c3, c4],
        [("1.200+", "Estudiantes activos"), ("18", "Cursos disponibles"), ("4,9 ★", "Calificación promedio"), ("72 años", "Edad promedio")]
    ):
        with col:
            st.markdown(f"""<div class="stat-box"><div class="stat-number">{num}</div><div class="stat-label">{label}</div></div>""", unsafe_allow_html=True)

    st.markdown("")

    # Por qué AdulTec
    st.markdown("## ¿Por qué elegir AdulTec?")
    fc1, fc2, fc3 = st.columns(3)
    features = [
        ("👴👵", "Diseñado para usted", "Letra grande, colores claros, ritmo pausado. Sin tecnicismos innecesarios."),
        ("🤝", "Apoyo constante", "Tutores especializados, comunidad amigable y soporte por WhatsApp."),
        ("🎯", "Contenido práctico", "Aprenda exactamente lo que necesita para su día a día digital."),
    ]
    for col, (ico, titulo, desc) in zip([fc1, fc2, fc3], features):
        with col:
            st.markdown(f"""
            <div class="card" style="text-align:center;">
                <div style="font-size:2.4rem;margin-bottom:10px;">{ico}</div>
                <div style="font-size:1rem;font-weight:800;margin-bottom:6px;">{titulo}</div>
                <div style="font-size:14px;color:#6B7280;">{desc}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("---")

    # Curso destacado
    st.markdown("## 🌟 Curso recomendado para empezar")
    with st.container():
        st.markdown(f"""
        <div class="card">
            <div style="display:flex;align-items:flex-start;gap:18px;flex-wrap:wrap;">
                <div style="font-size:3rem;">🌐</div>
                <div style="flex:1;">
                    <span class="badge badge-free">Gratis · 3 clases</span>
                    <div style="font-size:1.2rem;font-weight:800;margin:8px 0 4px;">{CURSO_INTERNET['titulo']}</div>
                    <div style="font-size:15px;color:#6B7280;margin-bottom:12px;">{CURSO_INTERNET['descripcion']}</div>
                    <div style="font-size:13px;color:#6B7280;font-weight:600;">📖 {CURSO_INTERNET['duracion']} &nbsp;·&nbsp; 🏅 Nivel {CURSO_INTERNET['nivel']}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("▶️  Comenzar curso gratuito", key="cta_curso"):
            st.session_state.modulo = 1
            st.session_state.pregunta = 0
            st.session_state.correctas = 0
            st.session_state.quiz_done = False
            st.session_state.quiz_respondida = False
            ir("curso")

    st.markdown("---")

    # Testimonios
    st.markdown("## 💬 Lo que dicen nuestros estudiantes")
    tc1, tc2 = st.columns(2)
    testimonios = [
        ("María, 72 años · San Juan", "Gracias a AdulTec ahora hago videollamadas con mis nietos sin pedir ayuda. Las explicaciones son clarísimas y los profesores muy pacientes."),
        ("Jorge, 68 años · Mendoza", "Nunca pensé que podría usar un smartphone con tanta facilidad. Los cursos tienen el ritmo perfecto para mí."),
        ("Ana, 75 años · Córdoba", "Me enseñaron a hacer los trámites del ANSES desde casa. ¡No saben cuánto tiempo me ahorraron!"),
        ("Roberto, 70 años · Buenos Aires", "La comunidad es increíble. Siempre hay alguien dispuesto a ayudar con cualquier duda."),
    ]
    for col, (autor, texto) in zip([tc1, tc2, tc1, tc2], testimonios):
        with col:
            st.markdown(f"""
            <div class="testimonial">
                "{texto}"
                <div class="testimonial-author">— {autor}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("---")
    cta1, cta2 = st.columns(2)
    with cta1:
        if st.button("📚  Ver todos los cursos", key="cta_cursos"):
            ir("cursos")
    with cta2:
        if st.button("💳  Ver planes y precios", key="cta_planes"):
            ir("planes")
    footer()


# ══════════════════════════════════════════════════════════════════════════════
# PÁGINA: MIS CURSOS
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.pagina == "cursos":
    st.markdown('<div class="hero-title">📚 Catálogo de cursos</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-sub">Aprenda a su ritmo · Sin presiones · Con apoyo real</div>', unsafe_allow_html=True)

    # Filtros simples
    filtro = st.radio("Mostrar:", ["Todos", "Gratuitos", "Premium"], horizontal=True, key="filtro_cursos")

    st.markdown("### Curso en progreso")

    # Curso principal
    st.markdown(f"""
    <div class="card">
        <div style="display:flex;align-items:flex-start;gap:18px;flex-wrap:wrap;">
            <div style="font-size:2.8rem;">🌐</div>
            <div style="flex:1;">
                <span class="badge badge-free">Gratis</span>
                <div style="font-size:1.1rem;font-weight:800;margin:8px 0 4px;">{CURSO_INTERNET['titulo']}</div>
                <div style="font-size:14px;color:#6B7280;margin-bottom:10px;">{CURSO_INTERNET['descripcion']}</div>
            </div>
        </div>
    </div>""", unsafe_allow_html=True)
    prog_actual = (st.session_state.modulo - 1) / len(CURSO_INTERNET["modulos"])
    st.progress(prog_actual)
    st.caption(f"Módulo {st.session_state.modulo} de {len(CURSO_INTERNET['modulos'])} · {int(prog_actual*100)}% completado")
    if st.button("▶️  Continuar curso", key="continuar_curso"):
        ir("curso")

    st.markdown("---")
    st.markdown("### Otros cursos disponibles")

    for curso in OTROS_CURSOS:
        if filtro == "Gratuitos" and curso["premium"]:
            continue
        if filtro == "Premium" and not curso["premium"]:
            continue

        tag_html = ""
        if curso["tag"]:
            tag_html = f'<span class="badge badge-new">{curso["tag"]}</span> '
        prem_html = '<span class="badge badge-premium">Premium</span>' if curso["premium"] else '<span class="badge badge-free">Gratis</span>'

        st.markdown(f"""
        <div class="card">
            <div style="display:flex;align-items:flex-start;gap:16px;flex-wrap:wrap;">
                <div style="font-size:2.4rem;">{curso['emoji']}</div>
                <div style="flex:1;">
                    <div style="margin-bottom:6px;">{tag_html}{prem_html}</div>
                    <div style="font-size:1rem;font-weight:800;margin-bottom:4px;">{curso['titulo']}</div>
                    <div style="font-size:14px;color:#6B7280;">{curso['descripcion']}</div>
                </div>
            </div>
        </div>""", unsafe_allow_html=True)
        btn_label = "🔒  Ver en planes Premium" if curso["premium"] else "▶️  Comenzar curso"
        btn_key = f"btn_curso_{curso['titulo']}"
        if st.button(btn_label, key=btn_key):
            if curso["premium"]:
                ir("planes")

    footer()


# ══════════════════════════════════════════════════════════════════════════════
# PÁGINA: CURSO
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.pagina == "curso":
    total_modulos = len(CURSO_INTERNET["modulos"])
    modulo_idx = st.session_state.modulo - 1
    modulo = CURSO_INTERNET["modulos"][modulo_idx]

    # Header
    st.markdown(f"""
    <div style="font-size:13px;font-weight:700;color:#8B92A8;margin-bottom:4px;">
        {CURSO_INTERNET['titulo']} · Módulo {st.session_state.modulo} de {total_modulos}
    </div>
    <div style="font-size:1.5rem;font-weight:900;margin-bottom:12px;">
        {modulo['icono']} {modulo['titulo']}
    </div>""", unsafe_allow_html=True)

    # Barra de progreso del curso
    prog = modulo_idx / total_modulos
    st.progress(prog)

    # Navegación entre módulos
    nav_cols = st.columns(total_modulos)
    for i, (col, m) in enumerate(zip(nav_cols, CURSO_INTERNET["modulos"])):
        with col:
            estado = "✅" if i < modulo_idx else ("▶️" if i == modulo_idx else "○")
            if st.button(f"{estado} {m['icono']}", key=f"nav_mod_{i}", help=m["titulo"]):
                st.session_state.modulo = i + 1
                st.session_state.pregunta = 0
                st.session_state.correctas = 0
                st.session_state.quiz_done = False
                st.session_state.quiz_respondida = False
                st.rerun()

    st.markdown("")
    tab_contenido, tab_quiz = st.tabs(["📖  Contenido", "🎯  Evaluación"])

    # ── TAB CONTENIDO ──────────────────────────────────────────────────────────
    with tab_contenido:
        st.markdown(modulo["contenido"])

        st.markdown("### 🎬 Video explicativo")
        st.markdown(f"""
        <div style="display:flex;justify-content:center;margin:16px 0;">
            <iframe width="640" height="360" src="{modulo['video']}"
                title="Video del módulo" frameborder="0"
                allow="accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture"
                allowfullscreen style="border-radius:16px;max-width:100%;"></iframe>
        </div>""", unsafe_allow_html=True)

        col_prev, col_next = st.columns(2)
        with col_prev:
            if st.session_state.modulo > 1:
                if st.button("◀  Módulo anterior", key="prev_mod"):
                    st.session_state.modulo -= 1
                    st.session_state.pregunta = 0
                    st.session_state.correctas = 0
                    st.session_state.quiz_done = False
                    st.session_state.quiz_respondida = False
                    st.rerun()
        with col_next:
            if st.session_state.modulo < total_modulos:
                if st.button("Módulo siguiente  ▶", key="next_mod"):
                    st.session_state.modulo += 1
                    st.session_state.pregunta = 0
                    st.session_state.correctas = 0
                    st.session_state.quiz_done = False
                    st.session_state.quiz_respondida = False
                    st.rerun()

    # ── TAB QUIZ ───────────────────────────────────────────────────────────────
    with tab_quiz:
        preguntas = modulo["quiz"]
        total_preg = len(preguntas)

        if not st.session_state.quiz_done:
            p_idx = st.session_state.pregunta
            preg = preguntas[p_idx]

            st.markdown(f"""
            <div style="font-size:13px;font-weight:700;color:#8B92A8;margin-bottom:10px;">
                Pregunta {p_idx+1} de {total_preg}
            </div>""", unsafe_allow_html=True)
            st.progress((p_idx) / total_preg)

            st.markdown(f"""
            <div class="quiz-card">
                <div class="quiz-question">{preg['pregunta']}</div>
            </div>""", unsafe_allow_html=True)

            respuesta = st.radio(
                "Elija su respuesta:",
                preg["opciones"],
                key=f"q_{st.session_state.modulo}_{p_idx}",
                index=None,
            )

            if not st.session_state.quiz_respondida:
                if st.button("Comprobar respuesta ✓", key=f"check_{p_idx}"):
                    if respuesta is None:
                        st.warning("Por favor, seleccione una respuesta antes de continuar.")
                    else:
                        idx_elegido = preg["opciones"].index(respuesta)
                        st.session_state.respuesta_elegida = idx_elegido
                        st.session_state.quiz_respondida = True
                        if idx_elegido == preg["correcta"]:
                            st.session_state.correctas += 1
                        st.rerun()
            else:
                idx_elegido = st.session_state.respuesta_elegida
                if idx_elegido == preg["correcta"]:
                    st.success(f"✅ ¡Correcto! {preg['explicacion']}")
                else:
                    st.error(f"❌ Respuesta incorrecta. La correcta era: **{preg['opciones'][preg['correcta']]}**")
                    st.info(f"💡 {preg['explicacion']}")

                sig_label = "Ver resultados 🎉" if p_idx == total_preg - 1 else "Siguiente pregunta ▶"
                if st.button(sig_label, key=f"next_q_{p_idx}"):
                    if p_idx < total_preg - 1:
                        st.session_state.pregunta += 1
                        st.session_state.quiz_respondida = False
                        st.session_state.respuesta_elegida = None
                        st.rerun()
                    else:
                        st.session_state.quiz_done = True
                        st.rerun()

        else:
            # Resultados
            correctas = st.session_state.correctas
            pct = int((correctas / total_preg) * 100)
            aprobado = pct >= 70

            st.markdown(f"""
            <div style="text-align:center;padding:20px 0;">
                {progress_ring_html(pct)}
                <div style="font-size:1.3rem;font-weight:900;margin-bottom:6px;">
                    {'¡Excelente! 🎉' if pct==100 else '¡Aprobado! 👏' if aprobado else 'Casi lo logra 💪'}
                </div>
                <div style="font-size:15px;color:#6B7280;">
                    Respondió correctamente <strong>{correctas} de {total_preg}</strong> preguntas
                </div>
            </div>""", unsafe_allow_html=True)

            if aprobado:
                st.success(f"Aprobó el módulo con {pct}% de aciertos. ¡Siga así!")
                if st.session_state.modulo < total_modulos:
                    if st.button("▶  Continuar al siguiente módulo", key="sig_mod_ok"):
                        st.session_state.modulo += 1
                        st.session_state.pregunta = 0
                        st.session_state.correctas = 0
                        st.session_state.quiz_done = False
                        st.session_state.quiz_respondida = False
                        st.rerun()
                else:
                    st.balloons()
                    st.success("🏆 ¡Felicitaciones! Completó el curso completo. Puede descargar su certificado desde su perfil.")
            else:
                st.warning(f"Obtuvo {pct}%. Necesita al menos 70% para aprobar. ¡No se rinda!")
                if st.button("🔄  Intentar nuevamente", key="retry_quiz"):
                    st.session_state.pregunta = 0
                    st.session_state.correctas = 0
                    st.session_state.quiz_done = False
                    st.session_state.quiz_respondida = False
                    st.session_state.respuesta_elegida = None
                    st.rerun()

            if st.button("📖  Repasar el contenido", key="repasar"):
                st.session_state.quiz_done = False
                st.session_state.pregunta = 0
                st.session_state.correctas = 0
                st.session_state.quiz_respondida = False
                st.rerun()

    if st.button("← Volver al catálogo", key="volver_cursos"):
        ir("cursos")
    footer()


# ══════════════════════════════════════════════════════════════════════════════
# PÁGINA: COMUNIDAD
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.pagina == "comunidad":
    st.markdown('<div class="hero-title">👥 Comunidad AdulTec</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-sub">Un espacio amigable para aprender juntos, hacer preguntas y compartir experiencias.</div>', unsafe_allow_html=True)

    tab_faq, tab_pregunta, tab_foro = st.tabs(["❓ Preguntas frecuentes", "📨 Hacer una consulta", "💬 Foro de estudiantes"])

    with tab_faq:
        st.markdown("### Preguntas frecuentes")
        faqs = [
            ("¿Cómo puedo cambiar mi contraseña?",
             "Haga clic en su nombre de usuario → 'Mi perfil' → 'Cambiar contraseña'. Siga las instrucciones en pantalla."),
            ("¿Cómo accedo a mis cursos?",
             "Desde el menú lateral toque '📚 Mis cursos', o desde la página de inicio en 'Curso en progreso'."),
            ("¿Los cursos tienen vencimiento?",
             "No. Una vez inscripto, tiene acceso de por vida. Avance a su propio ritmo."),
            ("¿Cómo obtengo el descuento para jubilados?",
             "Envíe una foto de su carnet de jubilado o pensionado a ayuda@adultec.com y le aplicamos el 20% de descuento en 24 hs."),
            ("¿Puedo cancelar cuando quiero?",
             "Sí. No hay contratos ni permanencia mínima. Cancele desde 'Mi perfil' o escribiéndonos por WhatsApp."),
            ("¿Qué pasa si tengo problemas técnicos?",
             "Use el botón verde 💬 de WhatsApp (abajo a la derecha), llame al 0800-ADULTEC o escriba a ayuda@adultec.com. Atendemos Lun–Vie de 9 a 18 hs."),
        ]
        for pregunta, respuesta in faqs:
            with st.expander(f"🔹 {pregunta}"):
                st.write(respuesta)

    with tab_pregunta:
        st.markdown("### Envíe su consulta")
        st.write("Le responderemos dentro de las **24 horas hábiles**.")

        categoria = st.selectbox(
            "Categoría:",
            ["Seleccione una categoría", "Problemas técnicos", "Contenido de los cursos", "Facturación y pagos", "Descuento jubilados", "Otros"],
            key="cat_consulta"
        )
        titulo_q = st.text_input("Título de su consulta:", placeholder="Ej: No puedo abrir el video del módulo 2", key="titulo_consulta")
        detalle_q = st.text_area(
            "Describa su consulta:",
            height=130,
            placeholder="Cuanto más detalle nos dé, más rápido podremos ayudarle.",
            key="detalle_consulta"
        )
        if st.button("📨  Enviar consulta", key="enviar_consulta"):
            if categoria == "Seleccione una categoría" or not titulo_q or not detalle_q:
                st.error("Por favor, complete todos los campos.")
            else:
                st.success("✅ ¡Consulta enviada! Le responderemos pronto en su correo registrado.")

    with tab_foro:
        st.markdown("### Conversaciones recientes")

        busqueda_f = st.text_input("🔍  Buscar en el foro:", placeholder="Ej: WhatsApp, contraseña...", key="busqueda_foro")

        posts = [
            {"autor": "Marta G.", "hace": "Ayer", "titulo": "¿Cómo guardo una foto de WhatsApp en la galería?", "resp": 3, "ultima": "Hace 2 hs"},
            {"autor": "Roberto P.", "hace": "Hace 3 días", "titulo": "Recomendación de teclado con letras más grandes", "resp": 7, "ultima": "Hoy"},
            {"autor": "Carmen L.", "hace": "Hace 5 días", "titulo": "Problema para comprar en Mercado Libre", "resp": 5, "ultima": "Hace 2 días"},
            {"autor": "José M.", "hace": "Hace 1 semana", "titulo": "¿Cómo activo el WiFi en mi tablet Samsung?", "resp": 4, "ultima": "Hace 3 días"},
        ]

        filtrados = [p for p in posts if not busqueda_f or busqueda_f.lower() in p["titulo"].lower()]

        if not filtrados:
            st.info("No se encontraron resultados para su búsqueda.")
        for p in filtrados:
            st.markdown(f"""
            <div class="card">
                <div style="font-size:1rem;font-weight:800;margin-bottom:6px;">{p['titulo']}</div>
                <div style="font-size:13px;color:#8B92A8;font-weight:600;">
                    ✍️ {p['autor']} · {p['hace']} &nbsp;·&nbsp;
                    💬 {p['resp']} respuestas &nbsp;·&nbsp;
                    🕐 Última actividad: {p['ultima']}
                </div>
            </div>""", unsafe_allow_html=True)

        if st.button("✏️  Crear nuevo tema", key="nuevo_tema"):
            st.info("Esta función estará disponible próximamente. Por ahora, use la pestaña 'Hacer una consulta'.")

    footer()


# ══════════════════════════════════════════════════════════════════════════════
# PÁGINA: PLANES
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.pagina == "planes":
    st.markdown('<div class="hero-title">💳 Planes y precios</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-sub">Precios calibrados para el bolsillo argentino · 7 días de prueba gratis en planes pagos</div>', unsafe_allow_html=True)

    # Toggle mensual/anual
    facturacion = st.radio("Facturación:", ["Mensual", "Anual (2 meses gratis)", ], horizontal=True, key="facturacion")
    anual = facturacion == "Anual (2 meses gratis)"

    st.markdown("")
    cols = st.columns(3)
    for col, plan in zip(cols, PLANES):
        with col:
            precio = plan["precio_anual"] // 12 if anual else plan["precio_mes"]
            periodo = "/mes · facturado anualmente" if anual else "/mes"
            featured_class = " featured" if plan["featured"] else ""
            rec_label = '<div style="font-size:12px;font-weight:800;color:#4361EE;margin-bottom:8px;">⭐ MÁS ELEGIDO</div>' if plan["featured"] else ""

            features_html = "".join(
                f'<div class="plan-feature"><span class="check">✅</span>{f}</div>'
                for f in plan["features"]
            )
            no_html = "".join(
                f'<div class="plan-feature"><span style="color:#D1D5DB;">✗</span><span style="color:#9CA3AF;">{f}</span></div>'
                for f in plan.get("no_incluye", [])
            )

            st.markdown(f"""
            <div class="plan-card{featured_class}">
                {rec_label}
                <div style="font-size:2rem;margin-bottom:6px;">{plan['emoji']}</div>
                <div class="plan-name">{plan['nombre']}</div>
                <div class="plan-price">{fmt_ars(precio)}</div>
                <div class="plan-period">{periodo}</div>
                <hr style="margin:14px 0;">
                {features_html}
                {no_html}
            </div>
            """, unsafe_allow_html=True)
            st.markdown("")
            btn_label = "Comenzar gratis" if plan["nombre"] == "Básico" else f"Probar 7 días gratis"
            if st.button(btn_label, key=f"btn_plan_{plan['nombre']}"):
                if not st.session_state.logueado:
                    ir("registro")
                else:
                    st.success(f"✅ Plan {plan['nombre']} activado. ¡Bienvenido/a!")

    st.markdown("---")

    # ARPU y distribución — gráfico con plotly
    st.markdown("### 📊 Distribución de usuarios por plan")
    df_planes = pd.DataFrame([
        {"Plan": p["nombre"], "Mix (%)": round(p["mix"] * 100, 1), "Precio (ARS/mes)": p["precio_mes"]}
        for p in PLANES
    ])

    col_g1, col_g2 = st.columns([1, 1])
    with col_g1:
        fig_pie = go.Figure(go.Pie(
            labels=df_planes["Plan"],
            values=df_planes["Mix (%)"],
            hole=0.55,
            marker_colors=["#34D399", "#4361EE", "#7C3AED"],
            textfont_size=14,
        ))
        fig_pie.update_layout(
            title="Mix de planes (encuesta real, n=45)",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font_family="Nunito",
            showlegend=True,
            margin=dict(t=40, b=20, l=0, r=0),
        )
        st.plotly_chart(fig_pie, use_container_width=True)

    with col_g2:
        fig_bar = go.Figure(go.Bar(
            x=df_planes["Plan"],
            y=df_planes["Precio (ARS/mes)"],
            marker_color=["#34D399", "#4361EE", "#7C3AED"],
            text=[fmt_ars(p) for p in df_planes["Precio (ARS/mes)"]],
            textposition="outside",
        ))
        fig_bar.update_layout(
            title=f"Precios por plan · ARPU ponderado: {fmt_ars(ARPU)}/mes",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font_family="Nunito",
            yaxis_title="ARS/mes",
            margin=dict(t=40, b=20, l=0, r=0),
            yaxis=dict(showgrid=True, gridcolor="#E2E6F3"),
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    st.markdown("---")

    # Descuentos y beneficios
    st.markdown("### 🎁 Descuentos especiales")
    d1, d2 = st.columns(2)
    with d1:
        st.markdown("""
        <div class="card">
            <div style="font-size:1.6rem;margin-bottom:8px;">👴👵</div>
            <div style="font-weight:800;font-size:1rem;margin-bottom:4px;">Descuento jubilados y pensionados</div>
            <div style="font-size:14px;color:#6B7280;">Presentando su carnet de jubilado/a obtenga un <strong>20% de descuento</strong> en cualquier plan. Envíe una foto a ayuda@adultec.com.</div>
        </div>""", unsafe_allow_html=True)
    with d2:
        st.markdown("""
        <div class="card">
            <div style="font-size:1.6rem;margin-bottom:8px;">👨‍👩‍👧‍👦</div>
            <div style="font-weight:800;font-size:1rem;margin-bottom:4px;">Plan familiar</div>
            <div style="font-size:14px;color:#6B7280;">Comparta su suscripción Premium con hasta <strong>3 miembros de su familia</strong> y ahorre un 30% del valor total.</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("### ❓ Preguntas frecuentes sobre planes")
    plan_faqs = [
        ("¿Puedo cancelar en cualquier momento?", "Sí. No hay permanencia mínima ni penalización. Cancele cuando lo desee desde su perfil."),
        ("¿Qué métodos de pago aceptan?", "Tarjetas de crédito y débito (Visa, Mastercard, Amex), transferencia bancaria y Mercado Pago."),
        ("¿Hay período de prueba?", "Sí. Los planes Estándar y Premium incluyen 7 días de prueba gratuita sin necesidad de tarjeta de crédito."),
        ("¿Hay becas?", "Sí. Contamos con un programa de becas para personas con bajos recursos. Escriba a becas@adultec.com para más información."),
    ]
    for p, r in plan_faqs:
        with st.expander(f"🔹 {p}"):
            st.write(r)

    footer()


# ══════════════════════════════════════════════════════════════════════════════
# PÁGINA: LOGIN
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.pagina == "login":
    _, col, _ = st.columns([1, 2, 1])
    with col:
        st.markdown("""
        <div style="text-align:center;margin-bottom:20px;">
            <span style="font-size:3rem;">🔑</span>
            <div style="font-size:1.5rem;font-weight:900;margin-top:6px;">Iniciar sesión</div>
            <div style="font-size:14px;color:#8B92A8;font-weight:600;margin-top:4px;">Bienvenido/a de vuelta</div>
        </div>""", unsafe_allow_html=True)

        with st.form("form_login"):
            usuario = st.text_input("Correo electrónico:", placeholder="ejemplo@gmail.com")
            contrasena = st.text_input("Contraseña:", type="password")
            recordar = st.checkbox("Recordar mi acceso")
            enviar = st.form_submit_button("Ingresar →")

            if enviar:
                if usuario and contrasena:
                    st.session_state.logueado = True
                    st.session_state.nombre = usuario.split("@")[0].capitalize()
                    st.success("¡Bienvenido/a! Redirigiendo...")
                    time.sleep(1)
                    ir("inicio")
                else:
                    st.error("Complete todos los campos.")

        st.markdown("<div style='text-align:center;margin-top:12px;'>¿No tiene cuenta aún?</div>", unsafe_allow_html=True)
        if st.button("📝  Crear cuenta gratis", key="ir_registro_desde_login"):
            ir("registro")

    footer()


# ══════════════════════════════════════════════════════════════════════════════
# PÁGINA: REGISTRO
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.pagina == "registro":
    _, col, _ = st.columns([1, 2, 1])
    with col:
        st.markdown("""
        <div style="text-align:center;margin-bottom:20px;">
            <span style="font-size:3rem;">📝</span>
            <div style="font-size:1.5rem;font-weight:900;margin-top:6px;">Crear mi cuenta</div>
            <div style="font-size:14px;color:#8B92A8;font-weight:600;margin-top:4px;">Es rápido, fácil y gratuito</div>
        </div>""", unsafe_allow_html=True)

        with st.form("form_registro"):
            c1, c2 = st.columns(2)
            with c1:
                nombre = st.text_input("Nombre*:", placeholder="Juan")
            with c2:
                apellido = st.text_input("Apellido*:", placeholder="Pérez")

            email = st.text_input("Correo electrónico*:", placeholder="ejemplo@gmail.com")
            telefono = st.text_input("Teléfono (opcional):", placeholder="+54 264 000-0000")

            c1, c2 = st.columns(2)
            with c1:
                contrasena = st.text_input("Contraseña*:", type="password")
            with c2:
                conf_contrasena = st.text_input("Confirmar contraseña*:", type="password")

            nacimiento = st.date_input("Fecha de nacimiento:")
            jubilado = st.checkbox("Soy jubilado/a o pensionado/a (20% de descuento)")
            terminos = st.checkbox("Acepto los términos y condiciones*")
            novedades = st.checkbox("Quiero recibir novedades y promociones")

            enviar = st.form_submit_button("Crear mi cuenta gratis →")

            if enviar:
                if not (nombre and apellido and email and contrasena and conf_contrasena and terminos):
                    st.error("Complete todos los campos obligatorios (*).")
                elif contrasena != conf_contrasena:
                    st.error("Las contraseñas no coinciden.")
                elif len(contrasena) < 6:
                    st.error("La contraseña debe tener al menos 6 caracteres.")
                else:
                    st.session_state.logueado = True
                    st.session_state.nombre = nombre
                    st.success(f"¡Cuenta creada con éxito! Bienvenido/a, {nombre}. 🎉")
                    if jubilado:
                        st.info("Recuerde enviarnos su carnet de jubilado a ayuda@adultec.com para activar el 20% de descuento.")
                    time.sleep(2)
                    ir("inicio")

        st.markdown("<div style='text-align:center;margin-top:12px;'>¿Ya tiene cuenta?</div>", unsafe_allow_html=True)
        if st.button("✅  Iniciar sesión", key="ir_login_desde_registro"):
            ir("login")

    footer()