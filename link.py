import unicodedata

def normalize(texto: str, max_len=25) -> str:
    texto = unicodedata.normalize("NFKD", texto)
    texto = texto.encode("ASCII", "ignore").decode("ASCII")
    return texto.upper()[:max_len]

def format_valor(valor: float) -> str:
    return f"{valor:.2f}"


def emv_field(tag: str, valor: str) -> str:
    return f"{tag}{len(valor):02d}{valor}"

def crc16_ccitt(payload: str) -> str:
    crc = 0xFFFF
    for b in payload.encode("utf-8"):
        crc ^= b << 8
        for _ in range(8):
            crc = ((crc << 1) ^ 0x1021) & 0xFFFF if crc & 0x8000 else (crc << 1) & 0xFFFF
    return f"{crc:04X}"

def genLink(chavePix: str, valor: float, nome: str, cidade: str, txtId: str = "***") -> str:
    nome = normalize(nome)
    cidade = normalize(cidade)
    txtId = normalize(txtId.replace(" ", ""))
    valor_str = format_valor(valor)

    payload = emv_field("00", "01")
    payload += emv_field("01", "12")
    mai = emv_field("00", "BR.GOV.BCB.PIX") + emv_field("01", chavePix)
    payload += emv_field("26", mai)
    payload += emv_field("52", "0000")
    payload += emv_field("53", "986")
    payload += emv_field("54", valor_str)
    payload += emv_field("58", "BR")
    payload += emv_field("59", nome)
    payload += emv_field("60", cidade)
    payload += emv_field("62", emv_field("05", txtId))
    payload_for_crc = payload + "6304"
    crc = crc16_ccitt(payload_for_crc)
    payload += emv_field("63", crc)

    return payload