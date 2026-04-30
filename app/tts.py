from omnivoice import OmniVoice
import torch


model = OmniVoice.from_pretrained(
    "k2-fsa/OmniVoice",
    device_map="cpu",
    dtype=torch.float32
)

# texto base (puedes dejarlo fijo o hacerlo dinámico)
TEXTO_REFERENCIA = "Te apoyamos sin importar el tamaño de tu negocio, con montos desde ciento sesenta mil hasta seiscientos noventa y seis millones. No es necesario contar con historial crediticio, ya que te brindamos la oportunidad de iniciar y crecer"

RUTA_AUDIO_REFERENCIA = "AudioOrigen.wav"


def generar_audio(texto: str):
    audio = model.generate(
        text=texto,
        ref_audio=RUTA_AUDIO_REFERENCIA,
        ref_text=TEXTO_REFERENCIA,
    )
    return audio[0]
