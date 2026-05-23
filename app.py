import os
import smtplib
import time
import random
import threading
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from flask import Flask

# Inicializamos la app de Flask
app = Flask(__name__)

# ===================== CONFIGURACION =====================
CORREO_REMITENTE   = "c56360164@gmail.com"
CONTRASENA_APP     = "mccjywfujgqngtcv"
CORREO_DESTINO     = "nonig0684@gmail.com"
INTERVALO_SEGUNDOS = 45
APPS_SCRIPT_URL    = os.environ.get("APPS_SCRIPT_URL", "")
# =========================================================

EMOJIS = ["🌹", "💖", "💕", "💘", "💌", "🌟", "💫", "🎵", "🎸", "🔥", "🌸", "💎", "🔮"]

# Historial para ver qué pasa en tiempo real desde la web
HISTORIAL_LOGS = []

def registrar_log(mensaje):
    hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea = f"[{hora}] {mensaje}"
    HISTORIAL_LOGS.append(linea)
    if len(HISTORIAL_LOGS) > 100:
        HISTORIAL_LOGS.pop(0)
    print(linea)

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
    
    # --- RIMAS ---
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

@app.route('/')
def home():
    logs_html = "".join(f"<li style='margin-bottom: 5px;'>{log}</li>" for log in reversed(HISTORIAL_LOGS))
    return f"""
    <html>
    <body style="font-family: sans-serif; background-color: #0b020a; color: #ff1493; padding: 40px; margin: 0; text-align: center;">
        <h1>🌹 BOT DE FERNANDA ACTIVADO 🌹</h1>
        <p style="color: #fff; font-size: 18px;">El bot está corriendo 24/7 en la nube enviando la canción infinita cada {INTERVALO_SEGUNDOS}s.</p>
        <div style="border: 2px solid #ff1493; padding: 15px; display: inline-block; border-radius: 10px; margin-top: 10px; box-shadow: 0 0 15px #ff1493; background-color: #1a0518;">
            <span style="font-size: 20px; font-weight: bold; text-transform: uppercase;">Estado: En línea ⚡</span>
        </div>
        
        <h2 style="color: #fff; margin-top: 40px; text-align: left; max-width: 800px; margin-left: auto; margin-right: auto;">📋 Consola de Eventos (Últimos sucesos):</h2>
        <div style="background-color: #150514; border: 1px solid #330c30; border-radius: 8px; padding: 20px; max-width: 800px; margin: 0 auto; text-align: left; height: 300px; overflow-y: scroll; color: #00ffcc; font-family: monospace; font-size: 14px; box-shadow: inset 0 0 10px #000;">
            <ul style="list-style-type: none; padding: 0; margin: 0;">
                {logs_html if HISTORIAL_LOGS else "<li>Esperando que inicie el primer envío...</li>"}
            </ul>
        </div>
    </body>
    </html>
    """

def enviar_verso(letra, numero_verso):
    try:
        emoji = random.choice(EMOJIS)
        asunto_unico = f"{emoji} {numero_verso}"

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
        
        if APPS_SCRIPT_URL:
            # Enviar usando la API de Google Apps Script (HTTP POST)
            import requests
            response = requests.post(APPS_SCRIPT_URL, json={
                "to": CORREO_DESTINO,
                "subject": asunto_unico,
                "htmlBody": html
            }, timeout=15)
            
            res_json = response.json()
            if response.status_code == 200 and res_json.get("status") == "success":
                registrar_log(f"✅ EXITO: Verso #{numero_verso} enviado vía Apps Script como '{asunto_unico}'")
                return True
            else:
                registrar_log(f"❌ ERROR: Apps Script falló al enviar #{numero_verso}. Razón: {res_json.get('message')}")
                return False
        else:
            # Caer de vuelta a SMTP por si no está configurado Apps Script
            msg = MIMEMultipart('alternative')
            msg['From']    = CORREO_REMITENTE
            msg['To']      = CORREO_DESTINO
            msg['Subject'] = asunto_unico
            
            parte_html = MIMEText(html, 'html', 'utf-8')
            msg.attach(parte_html)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=10) as servidor:
                servidor.login(CORREO_REMITENTE, CONTRASENA_APP)
                servidor.sendmail(CORREO_REMITENTE, CORREO_DESTINO, msg.as_string())

            registrar_log(f"✅ EXITO: Verso #{numero_verso} enviado vía SMTP como '{asunto_unico}'")
            return True
            
    except Exception as e:
        registrar_log(f"❌ ERROR: No se pudo enviar el verso #{numero_verso}. Razón: {e}")
        return False

# Bucle infinito del bot
def bot_loop():
    registrar_log("Iniciando hilo del bot...")
    
    # Render puede iniciar múltiples trabajadores, agregamos un pequeño delay aleatorio inicial 
    # para evitar envíos duplicados al arrancar
    time.sleep(random.uniform(2, 5))
    
    try:
        with open("progreso.txt", "r") as f:
            indice = int(f.read().strip())
    except:
        indice = 0

    while True:
        letra = VERSOS[indice % len(VERSOS)]
        enviar_verso(letra, indice + 1)
        indice += 1
        
        try:
            with open("progreso.txt", "w") as f:
                f.write(str(indice % len(VERSOS)))
        except Exception as e:
            registrar_log(f"⚠️ Alerta progreso.txt: {e}")
            
        time.sleep(INTERVALO_SEGUNDOS)

# Lanzar el bucle del bot en segundo plano al cargar el módulo
threading.Thread(target=bot_loop, daemon=True).start()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
