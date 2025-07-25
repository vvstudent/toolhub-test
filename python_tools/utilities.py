"""
Additional utility tools for ToolHub testing
"""

def base64_encoder():
    """
    Encode and decode Base64 data with format validation.
    
    Returns:
        dict: Tool definition for Base64 operations
    """
    return {
        "name": "Base64 Encoder/Decoder",
        "description": "Encode text to Base64 or decode Base64 to text with validation",
        "category": "Data Processing",
        "parameters": [
            {
                "name": "input_data",
                "type": "textarea",
                "description": "Text to encode or Base64 to decode",
                "required": True,
                "placeholder": "Enter text or Base64 data..."
            },
            {
                "name": "operation",
                "type": "select",
                "description": "Operation to perform",
                "options": ["encode", "decode", "auto"],
                "default": "auto"
            },
            {
                "name": "line_wrap",
                "type": "number",
                "description": "Wrap encoded output at specified length (0 = no wrap)",
                "default": 76,
                "min": 0,
                "max": 200
            }
        ],
        "implementation": """
import base64
import re

def process_base64(input_data, operation="auto", line_wrap=76):
    print(f"📝 Input Data Length: {len(input_data)} characters")
    
    # Auto-detect operation
    if operation == "auto":
        # Check if input looks like Base64
        base64_pattern = r'^[A-Za-z0-9+/]*={0,2}$'
        clean_input = re.sub(r'\\s', '', input_data)
        if re.match(base64_pattern, clean_input) and len(clean_input) % 4 == 0:
            operation = "decode"
        else:
            operation = "encode"
        print(f"🤖 Auto-detected operation: {operation}")
    
    print("\\n" + "=" * 50)
    
    if operation == "encode":
        try:
            # Encode to Base64
            encoded_bytes = base64.b64encode(input_data.encode('utf-8'))
            encoded_str = encoded_bytes.decode('ascii')
            
            # Apply line wrapping if specified
            if line_wrap > 0:
                wrapped = '\\n'.join(encoded_str[i:i+line_wrap] 
                                   for i in range(0, len(encoded_str), line_wrap))
                print(f"📤 Base64 Encoded (wrapped at {line_wrap}):")
                print(wrapped)
            else:
                print(f"📤 Base64 Encoded:")
                print(encoded_str)
            
            print(f"\\n📊 Encoding Stats:")
            print(f"   Original: {len(input_data)} characters")
            print(f"   Encoded: {len(encoded_str)} characters")
            print(f"   Size increase: {((len(encoded_str) / len(input_data)) - 1) * 100:.1f}%")
            
        except Exception as e:
            print(f"❌ Encoding Error: {str(e)}")
    
    elif operation == "decode":
        try:
            # Clean input (remove whitespace)
            clean_input = re.sub(r'\\s', '', input_data)
            
            # Decode from Base64
            decoded_bytes = base64.b64decode(clean_input)
            decoded_str = decoded_bytes.decode('utf-8')
            
            print(f"📥 Base64 Decoded:")
            print(decoded_str)
            
            print(f"\\n📊 Decoding Stats:")
            print(f"   Encoded: {len(clean_input)} characters")
            print(f"   Decoded: {len(decoded_str)} characters")
            print(f"   Size reduction: {((len(clean_input) / len(decoded_str)) - 1) * 100:.1f}%")
            
        except Exception as e:
            print(f"❌ Decoding Error: {str(e)}")
            print("💡 Tip: Make sure the input is valid Base64 data")

# Process the data
process_base64(input_data, operation, line_wrap)
"""
    }

def color_palette_generator():
    """
    Generate color palettes for design projects.
    
    Returns:
        dict: Tool definition for color palette generation
    """
    return {
        "name": "Color Palette Generator",
        "description": "Generate harmonious color palettes for design projects",
        "category": "Design",
        "parameters": [
            {
                "name": "base_color",
                "type": "text",
                "description": "Base color (hex, rgb, or color name)",
                "required": True,
                "default": "#3498db",
                "placeholder": "#3498db or rgb(52,152,219) or blue"
            },
            {
                "name": "palette_type",
                "type": "select",
                "description": "Type of color harmony",
                "options": ["monochromatic", "analogous", "complementary", "triadic", "tetradic"],
                "default": "complementary"
            },
            {
                "name": "color_count",
                "type": "number",
                "description": "Number of colors to generate",
                "default": 5,
                "min": 3,
                "max": 10
            },
            {
                "name": "output_format",
                "type": "multiselect",
                "description": "Output formats",
                "options": ["hex", "rgb", "hsl", "css"],
                "default": ["hex", "rgb"]
            }
        ],
        "implementation": """
import colorsys
import re

def parse_color(color_str):
    \"\"\"Parse color from various formats\"\"\"
    color_str = color_str.strip().lower()
    
    # Hex format
    if color_str.startswith('#'):
        hex_color = color_str[1:]
        if len(hex_color) == 3:
            hex_color = ''.join([c*2 for c in hex_color])
        r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
        return r/255, g/255, b/255
    
    # RGB format
    rgb_match = re.match(r'rgb\\((\\d+),\\s*(\\d+),\\s*(\\d+)\\)', color_str)
    if rgb_match:
        r, g, b = map(int, rgb_match.groups())
        return r/255, g/255, b/255
    
    # Named colors
    named_colors = {
        'red': (1, 0, 0), 'green': (0, 1, 0), 'blue': (0, 0, 1),
        'yellow': (1, 1, 0), 'cyan': (0, 1, 1), 'magenta': (1, 0, 1),
        'black': (0, 0, 0), 'white': (1, 1, 1), 'gray': (0.5, 0.5, 0.5)
    }
    if color_str in named_colors:
        return named_colors[color_str]
    
    raise ValueError(f"Invalid color format: {color_str}")

def rgb_to_hex(r, g, b):
    \"\"\"Convert RGB to hex\"\"\"
    return f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}"

def rgb_to_hsl(r, g, b):
    \"\"\"Convert RGB to HSL\"\"\"
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    return int(h*360), int(s*100), int(l*100)

def generate_palette(base_color, palette_type="complementary", color_count=5, output_format=["hex", "rgb"]):
    try:
        # Parse base color
        r, g, b = parse_color(base_color)
        h, l, s = colorsys.rgb_to_hls(r, g, b)
        
        print(f"🎨 Base Color: {base_color}")
        print(f"🔧 Palette Type: {palette_type}")
        print(f"📊 Color Count: {color_count}")
        print("\\n" + "=" * 60)
        
        colors = []
        
        if palette_type == "monochromatic":
            # Vary lightness
            for i in range(color_count):
                new_l = max(0.1, min(0.9, l + (i - color_count//2) * 0.15))
                new_r, new_g, new_b = colorsys.hls_to_rgb(h, new_l, s)
                colors.append((new_r, new_g, new_b))
        
        elif palette_type == "analogous":
            # Vary hue by small amounts
            for i in range(color_count):
                new_h = (h + (i - color_count//2) * 0.08) % 1
                new_r, new_g, new_b = colorsys.hls_to_rgb(new_h, l, s)
                colors.append((new_r, new_g, new_b))
        
        elif palette_type == "complementary":
            # Base color and its complement, with variations
            colors.append((r, g, b))
            comp_h = (h + 0.5) % 1
            comp_r, comp_g, comp_b = colorsys.hls_to_rgb(comp_h, l, s)
            colors.append((comp_r, comp_g, comp_b))
            
            # Add variations
            for i in range(color_count - 2):
                if i % 2 == 0:
                    var_h = h
                else:
                    var_h = comp_h
                new_l = max(0.1, min(0.9, l + (i - 1) * 0.2))
                new_r, new_g, new_b = colorsys.hls_to_rgb(var_h, new_l, s)
                colors.append((new_r, new_g, new_b))
        
        elif palette_type == "triadic":
            # Three colors equally spaced
            for i in range(color_count):
                new_h = (h + i * (1/3)) % 1
                new_r, new_g, new_b = colorsys.hls_to_rgb(new_h, l, s)
                colors.append((new_r, new_g, new_b))
        
        elif palette_type == "tetradic":
            # Four colors in two complementary pairs
            hues = [h, (h + 0.25) % 1, (h + 0.5) % 1, (h + 0.75) % 1]
            for i in range(color_count):
                use_h = hues[i % 4]
                new_r, new_g, new_b = colorsys.hls_to_rgb(use_h, l, s)
                colors.append((new_r, new_g, new_b))
        
        # Display colors
        for i, (cr, cg, cb) in enumerate(colors[:color_count], 1):
            print(f"🎨 Color {i}:")
            
            if "hex" in output_format:
                print(f"   HEX: {rgb_to_hex(cr, cg, cb)}")
            
            if "rgb" in output_format:
                print(f"   RGB: rgb({int(cr*255)}, {int(cg*255)}, {int(cb*255)})")
            
            if "hsl" in output_format:
                ch, cl, cs = rgb_to_hsl(cr, cg, cb)
                print(f"   HSL: hsl({ch}, {cs}%, {cl}%)")
            
            if "css" in output_format:
                print(f"   CSS: --color-{i}: {rgb_to_hex(cr, cg, cb)};")
            
            print()
        
        print("=" * 60)
        print("💡 Palette Usage Tips:")
        print(f"• {palette_type.title()} harmony creates {'subtle' if palette_type == 'monochromatic' else 'balanced'} color relationships")
        print("• Use darker colors for text, lighter for backgrounds")
        print("• Test accessibility with contrast ratio tools")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")

# Generate the palette
generate_palette(base_color, palette_type, color_count, output_format)
"""
    }

def qr_code_generator():
    """
    Generate QR codes for text, URLs, and other data.
    
    Returns:
        dict: Tool definition for QR code generation
    """
    return {
        "name": "QR Code Generator",
        "description": "Generate QR codes for text, URLs, WiFi, and contact information",
        "category": "Utilities",
        "parameters": [
            {
                "name": "data",
                "type": "textarea",
                "description": "Data to encode in QR code",
                "required": True,
                "placeholder": "Enter URL, text, or other data..."
            },
            {
                "name": "qr_type",
                "type": "select",
                "description": "QR code type",
                "options": ["text", "url", "wifi", "email", "phone", "sms"],
                "default": "text"
            },
            {
                "name": "error_correction",
                "type": "select",
                "description": "Error correction level",
                "options": ["L", "M", "Q", "H"],
                "default": "M"
            },
            {
                "name": "size",
                "type": "select",
                "description": "QR code size",
                "options": ["small", "medium", "large"],
                "default": "medium"
            }
        ],
        "implementation": """
def generate_qr_info(data, qr_type="text", error_correction="M", size="medium"):
    print(f"📱 QR Code Generator")
    print(f"📝 Data: {data}")
    print(f"🔧 Type: {qr_type}")
    print(f"🛡️ Error Correction: {error_correction}")
    print(f"📏 Size: {size}")
    print("\\n" + "=" * 50)
    
    # Format data based on type
    formatted_data = data
    
    if qr_type == "url":
        if not data.startswith(('http://', 'https://')):
            formatted_data = 'https://' + data
        print(f"🔗 Formatted URL: {formatted_data}")
    
    elif qr_type == "wifi":
        # Expected format: SSID,Password,Security
        parts = data.split(',')
        if len(parts) >= 2:
            ssid, password = parts[0], parts[1]
            security = parts[2] if len(parts) > 2 else "WPA"
            formatted_data = f"WIFI:T:{security};S:{ssid};P:{password};;"
            print(f"📶 WiFi Network: {ssid}")
            print(f"🔒 Security: {security}")
        else:
            print("❌ WiFi format should be: SSID,Password,Security")
    
    elif qr_type == "email":
        if '@' in data:
            formatted_data = f"mailto:{data}"
            print(f"📧 Email: {formatted_data}")
        else:
            print("❌ Invalid email format")
    
    elif qr_type == "phone":
        formatted_data = f"tel:{data}"
        print(f"📞 Phone: {formatted_data}")
    
    elif qr_type == "sms":
        # Expected format: number,message
        parts = data.split(',', 1)
        if len(parts) >= 2:
            number, message = parts[0], parts[1]
            formatted_data = f"sms:{number}:{message}"
            print(f"💬 SMS to: {number}")
            print(f"📝 Message: {message}")
        else:
            formatted_data = f"sms:{data}"
            print(f"💬 SMS to: {data}")
    
    # Error correction info
    error_levels = {
        'L': 'Low (~7% recovery)',
        'M': 'Medium (~15% recovery)',
        'Q': 'Quartile (~25% recovery)',
        'H': 'High (~30% recovery)'
    }
    
    # Size info
    size_info = {
        'small': '150x150 pixels',
        'medium': '300x300 pixels',
        'large': '600x600 pixels'
    }
    
    print(f"\\n📊 QR Code Specifications:")
    print(f"   Data Length: {len(formatted_data)} characters")
    print(f"   Error Correction: {error_levels.get(error_correction, error_correction)}")
    print(f"   Recommended Size: {size_info.get(size, size)}")
    
    print(f"\\n🔧 Final QR Data:")
    print(f"   {formatted_data}")
    
    print(f"\\n💡 Usage Tips:")
    print("• Higher error correction = more robust but larger QR code")
    print("• Test QR codes with multiple scanner apps")
    print("• Ensure sufficient contrast between foreground and background")
    print("• Leave quiet zone (white space) around QR code")
    
    # ASCII QR representation (simplified)
    print(f"\\n📱 ASCII QR Preview (simplified):")
    print("█████████████████████████")
    print("█ ▄▄▄▄▄ █▀▄█▄█ ▄▄▄▄▄ █")
    print("█ █   █ █▄▀▀▄█ █   █ █")
    print("█ █▄▄▄█ █▀▄▀▄█ █▄▄▄█ █")
    print("█▄▄▄▄▄▄▄█▄▀▄▀█▄▄▄▄▄▄▄█")
    print("█▄▄▄▄▄▄▄█▄▄▄▄█▄▄▄▄▄▄▄█")
    print("█████████████████████████")
    print("(Actual QR code would be generated by QR library)")

# Generate QR code info
generate_qr_info(data, qr_type, error_correction, size)
"""
    }

# Export additional tools
ADDITIONAL_TOOLS = [
    base64_encoder(),
    color_palette_generator(),
    qr_code_generator()
]