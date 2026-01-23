def genLink():
    # Entradas
    print("ATENÇÃO! Para casos de números de telefone, INCLUIR O +55(seu DDD), para números nacionais")
    chavePix = input("Digite a chave pix:")
    valor = float(input("Digite o valor do pix: "))
    nome = input("Digite o nome do recebedor: ")
    cidade = input("Digite a cidade do recebedor: ")
    txtId = input("Digite o identificador da transferência (opcional): ")
    if txtId == "":
        txtId = "***"  # valor padrão ou gerado automaticamente



    valor_str = f"{valor:.2f}"

    def emv_field(tag, valor):
        valor = str(valor)
        tamanho = f"{len(valor):02d}"
        return f"{tag}{tamanho}{valor}"


    # Versão
    payload = emv_field("00", "01")

    # Merchant Account Info (MAI)
    mai = emv_field("00", "BR.GOV.BCB.PIX") + emv_field("01", chavePix)
    payload += emv_field("26", mai)

    # 3 Campos constantes
    payload += emv_field("52", "0000")
    payload += emv_field("53", "986")
    payload += emv_field("54", valor_str)
    payload += emv_field("58", "BR")

    # Dados do usuário
    payload +=  emv_field("59", nome)
    payload +=  emv_field("60", cidade)

    # TxtId
    payload += emv_field("62", emv_field("05", txtId))

    # 6. Placeholder CRC16 (ainda não entendi o que é isso)
    payload_for_crc = payload + "6304"

    def crc16_ccitt(payload: str) -> str:
        data = payload.encode('utf-8')
        crc = 0xFFFF
        for b in data:
            crc ^= b << 8
            for _ in range(8):
                if crc & 0x8000:
                    crc = ((crc << 1) ^ 0x1021) & 0xFFFF
                else:
                    crc = (crc << 1) & 0xFFFF
        return f"{crc:04X}"

    crc16 = crc16_ccitt(payload_for_crc)
    payload += emv_field("63", crc16)

    return payload