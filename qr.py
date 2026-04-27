import qrcode

def link_to_qr(link, output_file="qr_code.png"):
    qr = qrcode.make(link)
    qr.save(output_file)
    print(f"QR code saved as {output_file}")

# Example usage
link = "https://gus-hypertonic-otto.ngrok-free.dev/"
link_to_qr(link)
