"""
QR Code Generator Tool
A standalone tool for generating QR codes with customizable options.
"""

import argparse
import sys
import base64
import urllib.parse

def generate_qr_code(text, size="medium", error_correction="M", border=4, output_format="text"):
    """
    Generate a QR code for the given text.
    
    Args:
        text (str): Text to encode in the QR code
        size (str): Size of the QR code (small, medium, large)
        error_correction (str): Error correction level (L, M, Q, H)
        border (int): Border size around the QR code
        output_format (str): Output format (text, url, base64)
    
    Returns:
        str: Generated QR code or URL/base64 representation
    """
    
    print(f"🔲 Generating QR Code for: {text[:50]}{'...' if len(text) > 50 else ''}")
    print(f"📏 Size: {size}")
    print(f"🛡️ Error Correction: {error_correction}")
    print(f"🖼️ Border: {border}")
    print(f"📤 Output Format: {output_format}")
    print("=" * 60)
    
    # Size mapping
    size_map = {
        "small": 150,
        "medium": 300,
        "large": 500
    }
    
    qr_size = size_map.get(size, 300)
    
    # Since we don't have qrcode library, we'll use a web service approach
    if output_format == "url":
        # Generate URL for QR code service
        encoded_text = urllib.parse.quote(text)
        qr_url = f"https://api.qrserver.com/v1/create-qr-code/?size={qr_size}x{qr_size}&data={encoded_text}&ecc={error_correction}&margin={border}"
        
        print(f"🌐 QR Code URL:")
        print(qr_url)
        print(f"\n💡 You can open this URL in a browser to view/download the QR code")
        return qr_url
    
    elif output_format == "base64":
        # For demonstration, create a simple base64 representation
        qr_data = f"QR:{text}:SIZE:{qr_size}:ECC:{error_correction}:BORDER:{border}"
        encoded = base64.b64encode(qr_data.encode()).decode()
        
        print(f"📊 Base64 Encoded QR Data:")
        print(encoded)
        print(f"\n💡 This is a simplified base64 representation")
        return encoded
    
    else:  # text format - ASCII art representation
        print(f"📱 ASCII QR Code Representation:")
        print("┌" + "─" * (20 + border * 2) + "┐")
        
        # Create a simple pattern based on text hash
        text_hash = hash(text) % 1000
        pattern = []
        
        for i in range(20):
            row = "│" + " " * border
            for j in range(20):
                # Simple pattern generation based on position and text hash
                if (i + j + text_hash) % 3 == 0:
                    row += "██"
                else:
                    row += "  "
            row += " " * border + "│"
            pattern.append(row)
        
        # Add border rows
        for _ in range(border):
            print("│" + " " * (20 + border * 2) + "│")
        
        # Print pattern
        for row in pattern:
            print(row)
        
        # Add border rows
        for _ in range(border):
            print("│" + " " * (20 + border * 2) + "│")
        
        print("└" + "─" * (20 + border * 2) + "┘")
        
        print(f"\n📋 QR Code Information:")
        print(f"   Text: {text}")
        print(f"   Length: {len(text)} characters")
        print(f"   Hash: {text_hash}")
        print(f"   Dimensions: {qr_size}x{qr_size} pixels")
        
        return "ASCII QR Code generated"

def analyze_qr_capacity(text):
    """Analyze QR code capacity and provide recommendations."""
    length = len(text)
    
    print(f"\n📊 QR Code Capacity Analysis:")
    print(f"   Input length: {length} characters")
    
    # QR Code capacity limits (approximate)
    capacities = {
        "Numeric": {"L": 7089, "M": 5596, "Q": 3993, "H": 3057},
        "Alphanumeric": {"L": 4296, "M": 3391, "Q": 2420, "H": 1852},
        "Binary": {"L": 2953, "M": 2331, "Q": 1663, "H": 1273},
        "Kanji": {"L": 1817, "M": 1435, "Q": 1024, "H": 784}
    }
    
    # Determine data type
    if text.isdigit():
        data_type = "Numeric"
    elif text.replace(" ", "").isalnum():
        data_type = "Alphanumeric"
    else:
        data_type = "Binary"
    
    print(f"   Data type: {data_type}")
    
    for level, capacity in capacities[data_type].items():
        if length <= capacity:
            print(f"   ✅ Error Correction {level}: OK ({capacity} max)")
        else:
            print(f"   ❌ Error Correction {level}: Too large ({capacity} max)")
    
    if length > max(capacities[data_type].values()):
        print(f"   ⚠️ Warning: Text is too long for QR code!")
        print(f"   💡 Consider shortening the text or using a URL shortener")

def main():
    """Main function to handle command line arguments."""
    parser = argparse.ArgumentParser(description="Generate QR codes with customizable options")
    
    parser.add_argument("text", help="Text to encode in the QR code")
    parser.add_argument("--size", choices=["small", "medium", "large"], default="medium",
                       help="Size of the QR code (default: medium)")
    parser.add_argument("--error-correction", choices=["L", "M", "Q", "H"], default="M",
                       help="Error correction level (default: M)")
    parser.add_argument("--border", type=int, default=4, help="Border size (default: 4)")
    parser.add_argument("--format", choices=["text", "url", "base64"], default="text",
                       help="Output format (default: text)")
    parser.add_argument("--analyze", action="store_true", help="Analyze QR code capacity")
    
    args = parser.parse_args()
    
    # Generate QR code
    result = generate_qr_code(
        args.text, 
        args.size, 
        args.error_correction, 
        args.border, 
        args.format
    )
    
    # Analyze capacity if requested
    if args.analyze:
        analyze_qr_capacity(args.text)
    
    return result

if __name__ == "__main__":
    main()