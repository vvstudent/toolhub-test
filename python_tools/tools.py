"""
ToolHub Sample Tools for GitHub Integration Testing
This file contains various sample tools to demonstrate ToolHub functionality.
"""

def text_analyzer():
    """
    Analyze text for various metrics like word count, character count, and readability.
    
    Returns:
        dict: Analysis results including word count, character count, sentences, and readability score
    """
    return {
        "name": "Text Analyzer",
        "description": "Analyze text for word count, character count, sentences, and readability metrics",
        "category": "Text Processing",
        "parameters": [
            {
                "name": "text",
                "type": "textarea",
                "description": "Text to analyze",
                "required": True,
                "placeholder": "Enter your text here..."
            },
            {
                "name": "include_readability",
                "type": "checkbox",
                "description": "Include readability analysis",
                "default": True
            }
        ],
        "implementation": """
import re
from collections import Counter

def analyze_text(text, include_readability=True):
    # Basic metrics
    word_count = len(text.split())
    char_count = len(text)
    char_count_no_spaces = len(text.replace(' ', ''))
    sentence_count = len(re.findall(r'[.!?]+', text))
    paragraph_count = len([p for p in text.split('\\n\\n') if p.strip()])
    
    # Word frequency
    words = re.findall(r'\\b\\w+\\b', text.lower())
    word_freq = Counter(words).most_common(10)
    
    result = {
        'word_count': word_count,
        'character_count': char_count,
        'character_count_no_spaces': char_count_no_spaces,
        'sentence_count': sentence_count,
        'paragraph_count': paragraph_count,
        'average_words_per_sentence': round(word_count / max(sentence_count, 1), 2),
        'most_common_words': word_freq
    }
    
    if include_readability and sentence_count > 0:
        # Simple readability score (Flesch Reading Ease approximation)
        avg_sentence_length = word_count / sentence_count
        avg_syllables = sum(len(re.findall(r'[aeiouAEIOU]', word)) for word in words) / max(word_count, 1)
        readability = 206.835 - (1.015 * avg_sentence_length) - (84.6 * avg_syllables)
        result['readability_score'] = round(max(0, min(100, readability)), 2)
        
        if readability >= 90:
            result['readability_level'] = 'Very Easy'
        elif readability >= 80:
            result['readability_level'] = 'Easy'
        elif readability >= 70:
            result['readability_level'] = 'Fairly Easy'
        elif readability >= 60:
            result['readability_level'] = 'Standard'
        elif readability >= 50:
            result['readability_level'] = 'Fairly Difficult'
        elif readability >= 30:
            result['readability_level'] = 'Difficult'
        else:
            result['readability_level'] = 'Very Difficult'
    
    return result

# Execute the analysis
result = analyze_text(text, include_readability)
print("📊 Text Analysis Results:")
print(f"📝 Words: {result['word_count']}")
print(f"🔤 Characters: {result['character_count']} (without spaces: {result['character_count_no_spaces']})")
print(f"📄 Sentences: {result['sentence_count']}")
print(f"📋 Paragraphs: {result['paragraph_count']}")
print(f"📏 Average words per sentence: {result['average_words_per_sentence']}")

if 'readability_score' in result:
    print(f"📖 Readability Score: {result['readability_score']} ({result['readability_level']})")

print("\\n🔤 Most Common Words:")
for word, count in result['most_common_words']:
    print(f"  {word}: {count}")
"""
    }

def password_generator():
    """
    Generate secure passwords with customizable options.
    
    Returns:
        dict: Tool definition for password generation
    """
    return {
        "name": "Password Generator",
        "description": "Generate secure passwords with customizable length and character sets",
        "category": "Security",
        "parameters": [
            {
                "name": "length",
                "type": "number",
                "description": "Password length",
                "required": True,
                "default": 12,
                "min": 4,
                "max": 128
            },
            {
                "name": "include_uppercase",
                "type": "checkbox",
                "description": "Include uppercase letters (A-Z)",
                "default": True
            },
            {
                "name": "include_lowercase",
                "type": "checkbox",
                "description": "Include lowercase letters (a-z)",
                "default": True
            },
            {
                "name": "include_numbers",
                "type": "checkbox",
                "description": "Include numbers (0-9)",
                "default": True
            },
            {
                "name": "include_symbols",
                "type": "checkbox",
                "description": "Include symbols (!@#$%^&*)",
                "default": True
            },
            {
                "name": "exclude_ambiguous",
                "type": "checkbox",
                "description": "Exclude ambiguous characters (0, O, l, 1, I)",
                "default": False
            },
            {
                "name": "count",
                "type": "number",
                "description": "Number of passwords to generate",
                "default": 1,
                "min": 1,
                "max": 10
            }
        ],
        "implementation": """
import random
import string

def generate_password(length, include_uppercase=True, include_lowercase=True, 
                     include_numbers=True, include_symbols=True, 
                     exclude_ambiguous=False, count=1):
    
    # Build character set
    chars = ""
    if include_lowercase:
        chars += string.ascii_lowercase
    if include_uppercase:
        chars += string.ascii_uppercase
    if include_numbers:
        chars += string.digits
    if include_symbols:
        chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    if exclude_ambiguous:
        ambiguous = "0Ol1I"
        chars = ''.join(c for c in chars if c not in ambiguous)
    
    if not chars:
        print("❌ Error: No character types selected!")
        return
    
    passwords = []
    for i in range(count):
        password = ''.join(random.choice(chars) for _ in range(length))
        passwords.append(password)
    
    print(f"🔐 Generated {count} password(s):")
    for i, pwd in enumerate(passwords, 1):
        print(f"  {i}. {pwd}")
    
    # Password strength analysis
    strength_score = 0
    if length >= 8: strength_score += 1
    if length >= 12: strength_score += 1
    if include_uppercase and include_lowercase: strength_score += 1
    if include_numbers: strength_score += 1
    if include_symbols: strength_score += 1
    
    strength_levels = ["Very Weak", "Weak", "Fair", "Good", "Strong"]
    strength = strength_levels[min(strength_score, 4)]
    
    print(f"\\n💪 Password Strength: {strength}")
    print(f"📏 Length: {length} characters")
    print(f"🎯 Character Set Size: {len(chars)} possible characters")

# Generate passwords
generate_password(length, include_uppercase, include_lowercase, include_numbers, 
                 include_symbols, exclude_ambiguous, count)
"""
    }

def json_formatter():
    """
    Format and validate JSON data with various output options.
    
    Returns:
        dict: Tool definition for JSON formatting
    """
    return {
        "name": "JSON Formatter",
        "description": "Format, validate, and beautify JSON data with syntax highlighting",
        "category": "Data Processing",
        "parameters": [
            {
                "name": "json_input",
                "type": "textarea",
                "description": "JSON data to format",
                "required": True,
                "placeholder": '{"name": "example", "value": 123}'
            },
            {
                "name": "indent_size",
                "type": "select",
                "description": "Indentation size",
                "options": ["2", "4", "8"],
                "default": "2"
            },
            {
                "name": "sort_keys",
                "type": "checkbox",
                "description": "Sort object keys alphabetically",
                "default": False
            },
            {
                "name": "compact_output",
                "type": "checkbox",
                "description": "Compact output (minified)",
                "default": False
            }
        ],
        "implementation": """
import json

def format_json(json_input, indent_size="2", sort_keys=False, compact_output=False):
    try:
        # Parse JSON
        data = json.loads(json_input)
        
        # Format options
        indent = None if compact_output else int(indent_size)
        separators = (',', ':') if compact_output else (',', ': ')
        
        # Format JSON
        formatted = json.dumps(data, indent=indent, sort_keys=sort_keys, 
                             separators=separators, ensure_ascii=False)
        
        print("✅ JSON Validation: Valid")
        print(f"📊 Data Type: {type(data).__name__}")
        
        if isinstance(data, dict):
            print(f"🔑 Object Keys: {len(data)}")
        elif isinstance(data, list):
            print(f"📋 Array Length: {len(data)}")
        
        print(f"📏 Original Size: {len(json_input)} characters")
        print(f"📏 Formatted Size: {len(formatted)} characters")
        
        print("\\n📄 Formatted JSON:")
        print("=" * 50)
        print(formatted)
        print("=" * 50)
        
    except json.JSONDecodeError as e:
        print(f"❌ JSON Validation: Invalid")
        print(f"🚫 Error: {str(e)}")
        print(f"📍 Line {e.lineno}, Column {e.colno}")
        
        # Try to show context around error
        lines = json_input.split('\\n')
        if e.lineno <= len(lines):
            error_line = lines[e.lineno - 1]
            print(f"\\n🔍 Error Context:")
            print(f"  {error_line}")
            print(f"  {' ' * (e.colno - 1)}^")

# Format the JSON
format_json(json_input, indent_size, sort_keys, compact_output)
"""
    }

def hash_generator():
    """
    Generate various hash values for text input.
    
    Returns:
        dict: Tool definition for hash generation
    """
    return {
        "name": "Hash Generator",
        "description": "Generate MD5, SHA1, SHA256, and other hash values for text",
        "category": "Security",
        "parameters": [
            {
                "name": "input_text",
                "type": "textarea",
                "description": "Text to hash",
                "required": True,
                "placeholder": "Enter text to generate hash..."
            },
            {
                "name": "hash_types",
                "type": "multiselect",
                "description": "Hash algorithms to use",
                "options": ["MD5", "SHA1", "SHA256", "SHA512"],
                "default": ["MD5", "SHA256"]
            },
            {
                "name": "output_format",
                "type": "select",
                "description": "Output format",
                "options": ["lowercase", "uppercase"],
                "default": "lowercase"
            }
        ],
        "implementation": """
import hashlib

def generate_hashes(input_text, hash_types=["MD5", "SHA256"], output_format="lowercase"):
    text_bytes = input_text.encode('utf-8')
    
    print(f"🔤 Input Text: {input_text}")
    print(f"📏 Input Length: {len(input_text)} characters ({len(text_bytes)} bytes)")
    print("\\n🔐 Generated Hashes:")
    print("=" * 60)
    
    hash_functions = {
        'MD5': hashlib.md5,
        'SHA1': hashlib.sha1,
        'SHA256': hashlib.sha256,
        'SHA512': hashlib.sha512
    }
    
    for hash_type in hash_types:
        if hash_type in hash_functions:
            hash_obj = hash_functions[hash_type](text_bytes)
            hash_value = hash_obj.hexdigest()
            
            if output_format == "uppercase":
                hash_value = hash_value.upper()
            
            print(f"{hash_type:>6}: {hash_value}")
    
    print("=" * 60)
    print("\\n💡 Hash Usage Tips:")
    print("• MD5: Fast but not cryptographically secure")
    print("• SHA1: Deprecated for security applications")
    print("• SHA256: Recommended for most security applications")
    print("• SHA512: Higher security, larger output")

# Generate hashes
generate_hashes(input_text, hash_types, output_format)
"""
    }

def url_encoder():
    """
    Encode and decode URLs with various encoding options.
    
    Returns:
        dict: Tool definition for URL encoding/decoding
    """
    return {
        "name": "URL Encoder/Decoder",
        "description": "Encode and decode URLs with support for different encoding types",
        "category": "Web Development",
        "parameters": [
            {
                "name": "input_url",
                "type": "textarea",
                "description": "URL or text to encode/decode",
                "required": True,
                "placeholder": "https://example.com/path with spaces"
            },
            {
                "name": "operation",
                "type": "select",
                "description": "Operation to perform",
                "options": ["encode", "decode", "both"],
                "default": "both"
            },
            {
                "name": "encoding_type",
                "type": "select",
                "description": "Encoding type",
                "options": ["standard", "plus", "safe"],
                "default": "standard"
            }
        ],
        "implementation": """
import urllib.parse

def process_url(input_url, operation="both", encoding_type="standard"):
    print(f"🔗 Input: {input_url}")
    print(f"⚙️ Operation: {operation}")
    print(f"🔧 Encoding Type: {encoding_type}")
    print("\\n" + "=" * 50)
    
    # Configure encoding
    safe_chars = ''
    if encoding_type == 'plus':
        # Use quote_plus (spaces become +)
        encode_func = urllib.parse.quote_plus
        decode_func = urllib.parse.unquote_plus
    elif encoding_type == 'safe':
        # Keep common URL characters safe
        safe_chars = ':/?#[]@!$&\\'()*+,;='
        encode_func = lambda x: urllib.parse.quote(x, safe=safe_chars)
        decode_func = urllib.parse.unquote
    else:
        # Standard encoding
        encode_func = urllib.parse.quote
        decode_func = urllib.parse.unquote
    
    if operation in ['encode', 'both']:
        try:
            encoded = encode_func(input_url)
            print(f"📤 Encoded URL:")
            print(f"   {encoded}")
            
            # Show what changed
            if encoded != input_url:
                print(f"\\n🔍 Changes made:")
                for i, (orig, enc) in enumerate(zip(input_url, encoded)):
                    if orig != enc:
                        print(f"   '{orig}' → '{enc}' at position {i}")
                        break
        except Exception as e:
            print(f"❌ Encoding Error: {str(e)}")
    
    if operation in ['decode', 'both']:
        try:
            decoded = decode_func(input_url)
            print(f"\\n📥 Decoded URL:")
            print(f"   {decoded}")
            
            # Show what changed
            if decoded != input_url:
                print(f"\\n🔍 Changes made:")
                for i, (orig, dec) in enumerate(zip(input_url, decoded)):
                    if orig != dec:
                        print(f"   '{orig}' → '{dec}' at position {i}")
                        break
        except Exception as e:
            print(f"❌ Decoding Error: {str(e)}")
    
    print("\\n" + "=" * 50)
    print("💡 URL Encoding Guide:")
    print("• Space: %20 (standard) or + (plus encoding)")
    print("• Special chars: %XX where XX is hex ASCII code")
    print("• Safe chars: A-Z a-z 0-9 - . _ ~")

# Process the URL
process_url(input_url, operation, encoding_type)
"""
    }

# Export all tools
TOOLS = [
    text_analyzer(),
    password_generator(),
    json_formatter(),
    hash_generator(),
    url_encoder()
]