"""
File Hash Calculator Tool
A comprehensive tool for calculating various hash values of files and text.
"""

import hashlib
import argparse
import os
import sys
import time

def calculate_hash(data, hash_type="md5", is_file=False):
    """
    Calculate hash for data or file.
    
    Args:
        data (str): File path or text data
        hash_type (str): Type of hash to calculate
        is_file (bool): Whether data is a file path or text
    
    Returns:
        str: Calculated hash value
    """
    
    # Available hash algorithms
    available_hashes = {
        'md5': hashlib.md5,
        'sha1': hashlib.sha1,
        'sha224': hashlib.sha224,
        'sha256': hashlib.sha256,
        'sha384': hashlib.sha384,
        'sha512': hashlib.sha512,
        'blake2b': hashlib.blake2b,
        'blake2s': hashlib.blake2s
    }
    
    if hash_type not in available_hashes:
        raise ValueError(f"Unsupported hash type: {hash_type}")
    
    hasher = available_hashes[hash_type]()
    
    if is_file:
        if not os.path.exists(data):
            raise FileNotFoundError(f"File not found: {data}")
        
        file_size = os.path.getsize(data)
        print(f"📁 File: {data}")
        print(f"📏 Size: {format_file_size(file_size)}")
        print(f"🔐 Hash Type: {hash_type.upper()}")
        print("⏳ Calculating hash...")
        
        start_time = time.time()
        
        # Read file in chunks for memory efficiency
        with open(data, 'rb') as f:
            chunk_size = 8192
            processed = 0
            
            while chunk := f.read(chunk_size):
                hasher.update(chunk)
                processed += len(chunk)
                
                # Show progress for large files
                if file_size > 1024 * 1024:  # > 1MB
                    progress = (processed / file_size) * 100
                    print(f"\r⏳ Progress: {progress:.1f}%", end="", flush=True)
        
        if file_size > 1024 * 1024:
            print()  # New line after progress
        
        end_time = time.time()
        calculation_time = end_time - start_time
        
        hash_value = hasher.hexdigest()
        
        print(f"✅ Hash calculated in {calculation_time:.2f} seconds")
        print(f"🔑 {hash_type.upper()}: {hash_value}")
        
        return hash_value
    
    else:
        # Hash text data
        print(f"📝 Text: {data[:100]}{'...' if len(data) > 100 else ''}")
        print(f"📏 Length: {len(data)} characters")
        print(f"🔐 Hash Type: {hash_type.upper()}")
        
        hasher.update(data.encode('utf-8'))
        hash_value = hasher.hexdigest()
        
        print(f"🔑 {hash_type.upper()}: {hash_value}")
        
        return hash_value

def format_file_size(size_bytes):
    """Format file size in human readable format."""
    if size_bytes == 0:
        return "0 B"
    
    size_names = ["B", "KB", "MB", "GB", "TB"]
    i = 0
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024.0
        i += 1
    
    return f"{size_bytes:.2f} {size_names[i]}"

def calculate_multiple_hashes(data, is_file=False):
    """Calculate multiple hash types for comparison."""
    hash_types = ['md5', 'sha1', 'sha256', 'sha512']
    results = {}
    
    print("🔐 Calculating multiple hashes...")
    print("=" * 60)
    
    for hash_type in hash_types:
        try:
            hash_value = calculate_hash(data, hash_type, is_file)
            results[hash_type] = hash_value
            print("-" * 60)
        except Exception as e:
            print(f"❌ Error calculating {hash_type}: {e}")
            results[hash_type] = None
    
    return results

def verify_hash(data, expected_hash, hash_type="md5", is_file=False):
    """Verify if calculated hash matches expected hash."""
    print(f"🔍 Verifying {hash_type.upper()} hash...")
    print(f"📋 Expected: {expected_hash}")
    
    try:
        calculated_hash = calculate_hash(data, hash_type, is_file)
        
        if calculated_hash.lower() == expected_hash.lower():
            print("✅ Hash verification PASSED")
            print("🔒 File/data integrity confirmed")
            return True
        else:
            print("❌ Hash verification FAILED")
            print("⚠️ File/data may be corrupted or modified")
            print(f"📋 Expected:   {expected_hash}")
            print(f"🔑 Calculated: {calculated_hash}")
            return False
    
    except Exception as e:
        print(f"❌ Verification error: {e}")
        return False

def analyze_hash_security(hash_type):
    """Provide security analysis of hash algorithm."""
    security_info = {
        'md5': {
            'security': 'WEAK',
            'bits': 128,
            'status': 'Cryptographically broken',
            'recommendation': 'Avoid for security purposes, OK for checksums'
        },
        'sha1': {
            'security': 'WEAK',
            'bits': 160,
            'status': 'Cryptographically broken',
            'recommendation': 'Avoid for security purposes'
        },
        'sha224': {
            'security': 'GOOD',
            'bits': 224,
            'status': 'Secure',
            'recommendation': 'Good for most applications'
        },
        'sha256': {
            'security': 'EXCELLENT',
            'bits': 256,
            'status': 'Highly secure',
            'recommendation': 'Recommended for security applications'
        },
        'sha384': {
            'security': 'EXCELLENT',
            'bits': 384,
            'status': 'Highly secure',
            'recommendation': 'Excellent for high-security applications'
        },
        'sha512': {
            'security': 'EXCELLENT',
            'bits': 512,
            'status': 'Highly secure',
            'recommendation': 'Excellent for high-security applications'
        },
        'blake2b': {
            'security': 'EXCELLENT',
            'bits': 512,
            'status': 'Modern and secure',
            'recommendation': 'Fast and secure alternative to SHA-2'
        },
        'blake2s': {
            'security': 'EXCELLENT',
            'bits': 256,
            'status': 'Modern and secure',
            'recommendation': 'Fast and secure for smaller outputs'
        }
    }
    
    if hash_type in security_info:
        info = security_info[hash_type]
        print(f"\n🛡️ Security Analysis for {hash_type.upper()}:")
        print(f"   Security Level: {info['security']}")
        print(f"   Output Size: {info['bits']} bits")
        print(f"   Status: {info['status']}")
        print(f"   Recommendation: {info['recommendation']}")

def main():
    """Main function to handle command line arguments."""
    parser = argparse.ArgumentParser(description="Calculate file and text hashes")
    
    parser.add_argument("input", help="File path or text to hash")
    parser.add_argument("--type", choices=['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512', 'blake2b', 'blake2s'],
                       default="sha256", help="Hash algorithm (default: sha256)")
    parser.add_argument("--file", action="store_true", help="Treat input as file path")
    parser.add_argument("--multiple", action="store_true", help="Calculate multiple hash types")
    parser.add_argument("--verify", help="Expected hash value for verification")
    parser.add_argument("--analyze", action="store_true", help="Show security analysis")
    
    args = parser.parse_args()
    
    try:
        if args.multiple:
            results = calculate_multiple_hashes(args.input, args.file)
            
            print("\n📊 Hash Summary:")
            print("=" * 60)
            for hash_type, hash_value in results.items():
                if hash_value:
                    print(f"{hash_type.upper():>8}: {hash_value}")
        
        elif args.verify:
            verify_hash(args.input, args.verify, args.type, args.file)
        
        else:
            calculate_hash(args.input, args.type, args.file)
        
        if args.analyze:
            analyze_hash_security(args.type)
    
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()