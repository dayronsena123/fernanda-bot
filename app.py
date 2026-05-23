import os
import smtplib
import time
import random
import threading
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from flask import Flask

# Inicializamos la app de Flask para Render
app = Flask(__name__)

# ===================== CONFIGURACION =====================
CORREO_REMITENTE   = "c56360164@gmail.com"
CONTRASENA_APP     = "mccjywfujgqngtcv"
CORREO_DESTINO     = "nonig0684@gmail.com"
INTERVALO_SEGUNDOS = 45  # cada 45 segundos
# =========================================================

EMOJIS = ["🌹", "💖", "💕", "💘", "💌", "🌟", "💫", "🎵", "🎸", "🔥", "🌸", "💎", "🔮"]

# Versos ampliados con más rimas súper divertidas sobre Fernanda 😂
VERSOS = [
    "...hay un nombre...",
    "...que no me deja en paz...",
    "FERNANDA... 💕",
    "Desde que te vi por primera vez...",
    "no hay día que no piense en ti...",
    "FER-NAN-DA! 😍",
    "Tu risa ilumina el cuarto entero...",
    "tu nombre suena como un lucero...",
    "¡FERNANDA! 🌹",
    "¡FERNANDA! 🌹",
    "¡No puedo dejar de pensar en ti! 💘",
    "¡FERNANDA! 😍",
    "Por las mañanas despierto y pienso...",
    "¿Qué estará haciendo Fernanda hoy? 👀",
    "Por las noches me duermo pensando...",
    "Fernanda... Fernanda... ay... 🥺",
    "Fernanda Valle de la Cruz... 💫",
    "Si Fernanda me mirara un segundo...",
    "se me detendría el mundo entero... 🌎",
    "Fer... nan... da...",
    "Fer... nan... DA! 🎶",
    "¿Sabes cuántas veces al día?",
    "digo tu nombre en mi cabeza...",
    "¡INFINITAS, FERNANDA! 💀",
    "¡IN-FI-NI-TAS! 💀",
    "Fernanda si vieras este correo...",
    "sabrías que alguien te admira mucho... 👀",
    "Fernanda con F de fantástica... 🌟",
    "con E de especial y única... 🌟",
    "con R de radiante y romántica... 💕",
    "con N de... nada, solo Fernanda. 🌟",
    "con A de asombrosa... 💕",
    "con N de nunca la olvidaré... 🥺",
    "con D de demasiado hermosa... 🌹",
    "con A de... ayyyy Fernanda. 💕",
    "¡¡¡FERNANDA!!! 🌹🌹🌹",
    "¡¡¡FERNANDA!!! 🌹🌹🌹",
    "¡¡¡FERNANDAAAAAAAA!!! 🌹🌹🌹",
    "Si esta canción llegara a tus oídos...",
    "¿qué pensarías tú, Fernanda? 🥺",
    "¿Que estás en el corazón de alguien?",
    "Porque sí, Fernanda. Sí estás... 🥺",
    "Y aunque el tiempo pase y pase...",
    "y aunque los correos sigan llegando...",
    "Fernanda. Fernanda. Fernanda. 😂",
    
    # --- NUEVAS RIMAS Y VERSOS CREATIVOS ---
    "Fernanda Valle de la Cruz... 🌟",
    "eres como mi señal de wi-fi... 📶",
    "Me conecto a ti y no me quiero desconectar... 😍",
    "Si la belleza fuera un delito... ⚖️",
    "¡Fernanda tendría cadena perpetua! 🚔",
    "Fernanda, si fueras código de Python... 💻",
    "serías un bucle infinito de perfección... 🐍",
    "En el diccionario del amor... 📖",
    "la definición de perfección es Fernanda. 🌹",
    "Fernanda, eres el azúcar de mi café... ☕",
    "la melodía que quiero escuchar otra vez... 🎵",
    "Con tu sonrisa detienes el tiempo... ⏳",
    "y pones a latir mi corazón al cien por ciento... 💕",
    
    "Fernanda...",
    "Fernanda...",
    "...",
    "FERNANDA. (y vuelve a empezar... 😈)"
]

# Servir una página web simple para que Render mantenga el bot activo
@app.route('/')
def home():
    return """
    <html>
    <body style="font-family: sans-serif; text-align: center; background-color: #0b020a; color: #ff1493; padding: 50px;">
        <h1>🌹 BOT DE FERNANDA ACTIVADO 🌹</h1>
        <p style="color: #fff; font-size: 18px;">El bot está corriendo 24/7 en la nube enviando la canción infinita.</p>
        <div style="border: 2px solid #ff1493; padding: 20px; display: inline-block; border-radius: 10px; margin-top: 20px;
                    box-shadow: 0 0 15px #ff1493;">
            <span style="font-size: 24px; font-weight: bold; text-transform: uppercase;">¡Bucle Activo! ⚡</span>
        </div>
    </body>
    </html>
    """

def enviar_verso(letra, numero_verso):
    hora = datetime.now().strftime("%H:%M:%S")
    try:
        msg = MIMEMultipart('alternative')
        msg['From']    = CORREO_REMITENTE
        msg['To']      = CORREO_DESTINO
        
        # Asunto dinámico para evitar hilos de Gmail
        emoji = random.choice(EMOJIS)
        asunto_unico = f"{emoji} {numero_verso}"
        msg['Subject'] = asunto_unico

        # Estilo Neón Premium en HTML
        html = f"""
        <html>
        <body style="font-family: 'Arial Black', Impact, sans-serif; text-align: center; background-color: #0b020a; padding: 50px; margin: 0;">
            <div style="font-size: 38px; font-weight: 900; color: #fff; text-transform: uppercase; line-height: 1.4; letter-spacing: 3px; 
                        text-shadow: 0 0 5px #fff, 0 0 10px #ff1493, 0 0 20px #ff1493, 0 0 30px #ff1493, 0 0 40px #ff1493;">
                {letra}
            </div>
        </body>
        </html>
        """
        
        parte_html = MIMEText(html, 'html', 'utf-8')
        msg.attach(parte_html)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as servidor:
            servidor.login(CORREO_REMITENTE, CONTRASENA_APP)
            servidor.sendmail(CORREO_REMITENTE, CORREO_DESTINO, msg.as_string())

        print(f"[{hora}] Enviado verso #{numero_verso} (Asunto: {asunto_unico}): {letra}")
        return True
    except Exception as e:
        print(f"[{hora}] Error al enviar: {e}")
        return False

# Bucle infinito que correrá en segundo plano
def bot_loop():
    # Intentamos leer progreso anterior si existe
    try:
        with open("progreso.txt", "r") as f:
            indice = int(f.read().strip())
    except:
        indice = 0

    print("Iniciando bucle del bot en segundo plano...")
    while True:
        letra = VERSOS[indice % len(VERSOS)]
        enviar_verso(letra, indice + 1)
        indice += 1
        
        # Guardar progreso
        try:
            with open("progreso.txt", "w") as f:
                f.write(str(indice % len(VERSOS)))
        except Exception as e:
            print(f"Error guardando progreso: {e}")
            
        time.sleep(INTERVALO_SEGUNDOS)

# Lanzar el bot en un hilo separado antes de arrancar Flask
threading.Thread(target=bot_loop, daemon=True).start()

if __name__ == '__main__':
    # Render asigna dinámicamente un puerto en la variable PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
