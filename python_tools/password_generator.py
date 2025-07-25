#!/usr/bin/env python3
"""
Password Generator Tool

A comprehensive tool for generating secure passwords with various customization options.
Supports different character sets, length requirements, and security analysis.
"""

import random
import string
import secrets
import argparse
import re
from typing import List, Dict, Any
import math


class PasswordGenerator:
    """A secure password generator with customizable options."""
    
    def __init__(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        self.ambiguous = "0O1lI"
    
    def generate_password(self, 
                         length: int = 12,
                         include_uppercase: bool = True,
                         include_lowercase: bool = True,
                         include_digits: bool = True,
                         include_symbols: bool = True,
                         exclude_ambiguous: bool = False,
                         custom_chars: str = "") -> str:
        """
        Generate a secure password with specified criteria.
        
        Args:
            length: Password length (minimum 4)
            include_uppercase: Include uppercase letters
            include_lowercase: Include lowercase letters
            include_digits: Include digits
            include_symbols: Include symbols
            exclude_ambiguous: Exclude ambiguous characters (0, O, 1, l, I)
            custom_chars: Additional custom characters to include
            
        Returns:
            Generated password string
        """
        if length < 4:
            raise ValueError("Password length must be at least 4 characters")
        
        # Build character set
        charset = ""
        required_chars = []
        
        if include_lowercase:
            chars = self.lowercase
            if exclude_ambiguous:
                chars = ''.join(c for c in chars if c not in self.ambiguous)
            charset += chars
            required_chars.append(secrets.choice(chars))
        
        if include_uppercase:
            chars = self.uppercase
            if exclude_ambiguous:
                chars = ''.join(c for c in chars if c not in self.ambiguous)
            charset += chars
            required_chars.append(secrets.choice(chars))
        
        if include_digits:
            chars = self.digits
            if exclude_ambiguous:
                chars = ''.join(c for c in chars if c not in self.ambiguous)
            charset += chars
            required_chars.append(secrets.choice(chars))
        
        if include_symbols:
            charset += self.symbols
            required_chars.append(secrets.choice(self.symbols))
        
        if custom_chars:
            charset += custom_chars
            required_chars.append(secrets.choice(custom_chars))
        
        if not charset:
            raise ValueError("At least one character type must be selected")
        
        # Generate password ensuring at least one character from each selected type
        password_chars = required_chars[:]
        remaining_length = length - len(required_chars)
        
        for _ in range(remaining_length):
            password_chars.append(secrets.choice(charset))
        
        # Shuffle the password characters
        secrets.SystemRandom().shuffle(password_chars)
        
        return ''.join(password_chars)
    
    def generate_multiple_passwords(self, count: int, **kwargs) -> List[str]:
        """Generate multiple passwords with the same criteria."""
        return [self.generate_password(**kwargs) for _ in range(count)]
    
    def generate_passphrase(self, 
                           word_count: int = 4,
                           separator: str = "-",
                           capitalize: bool = True,
                           add_numbers: bool = False) -> str:
        """
        Generate a passphrase using random words.
        
        Args:
            word_count: Number of words in the passphrase
            separator: Character to separate words
            capitalize: Capitalize first letter of each word
            add_numbers: Add random numbers to the passphrase
            
        Returns:
            Generated passphrase
        """
        # Simple word list for demonstration
        words = [
            "apple", "banana", "cherry", "dragon", "elephant", "forest", "guitar",
            "house", "island", "jungle", "kitchen", "laptop", "mountain", "ocean",
            "piano", "queen", "river", "sunset", "tiger", "umbrella", "village",
            "window", "yellow", "zebra", "bridge", "castle", "diamond", "engine",
            "flower", "garden", "hammer", "iceberg", "jacket", "knight", "ladder"
        ]
        
        selected_words = [secrets.choice(words) for _ in range(word_count)]
        
        if capitalize:
            selected_words = [word.capitalize() for word in selected_words]
        
        passphrase = separator.join(selected_words)
        
        if add_numbers:
            passphrase += separator + str(secrets.randbelow(9999))
        
        return passphrase
    
    def analyze_password_strength(self, password: str) -> Dict[str, Any]:
        """
        Analyze the strength of a password.
        
        Args:
            password: Password to analyze
            
        Returns:
            Dictionary containing strength analysis
        """
        analysis = {
            "length": len(password),
            "has_lowercase": bool(re.search(r'[a-z]', password)),
            "has_uppercase": bool(re.search(r'[A-Z]', password)),
            "has_digits": bool(re.search(r'\d', password)),
            "has_symbols": bool(re.search(r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?]', password)),
            "unique_chars": len(set(password)),
            "entropy": 0,
            "strength": "Very Weak"
        }
        
        # Calculate entropy
        charset_size = 0
        if analysis["has_lowercase"]:
            charset_size += 26
        if analysis["has_uppercase"]:
            charset_size += 26
        if analysis["has_digits"]:
            charset_size += 10
        if analysis["has_symbols"]:
            charset_size += 32
        
        if charset_size > 0:
            analysis["entropy"] = len(password) * math.log2(charset_size)
        
        # Determine strength
        score = 0
        if analysis["length"] >= 8:
            score += 1
        if analysis["length"] >= 12:
            score += 1
        if analysis["has_lowercase"]:
            score += 1
        if analysis["has_uppercase"]:
            score += 1
        if analysis["has_digits"]:
            score += 1
        if analysis["has_symbols"]:
            score += 1
        if analysis["unique_chars"] >= len(password) * 0.8:
            score += 1
        if analysis["entropy"] >= 50:
            score += 1
        
        if score <= 2:
            analysis["strength"] = "Very Weak"
        elif score <= 4:
            analysis["strength"] = "Weak"
        elif score <= 6:
            analysis["strength"] = "Medium"
        elif score <= 7:
            analysis["strength"] = "Strong"
        else:
            analysis["strength"] = "Very Strong"
        
        return analysis
    
    def check_common_passwords(self, password: str) -> bool:
        """
        Check if password is in common passwords list.
        
        Args:
            password: Password to check
            
        Returns:
            True if password is common, False otherwise
        """
        common_passwords = [
            "password", "123456", "password123", "admin", "qwerty",
            "letmein", "welcome", "monkey", "1234567890", "abc123",
            "password1", "123456789", "welcome123", "admin123"
        ]
        
        return password.lower() in [p.lower() for p in common_passwords]


def main():
    """Main function for command-line usage."""
    parser = argparse.ArgumentParser(description="Generate secure passwords")
    parser.add_argument("--length", "-l", type=int, default=12,
                       help="Password length (default: 12)")
    parser.add_argument("--count", "-c", type=int, default=1,
                       help="Number of passwords to generate (default: 1)")
    parser.add_argument("--no-uppercase", action="store_true",
                       help="Exclude uppercase letters")
    parser.add_argument("--no-lowercase", action="store_true",
                       help="Exclude lowercase letters")
    parser.add_argument("--no-digits", action="store_true",
                       help="Exclude digits")
    parser.add_argument("--no-symbols", action="store_true",
                       help="Exclude symbols")
    parser.add_argument("--exclude-ambiguous", action="store_true",
                       help="Exclude ambiguous characters (0, O, 1, l, I)")
    parser.add_argument("--custom-chars", type=str, default="",
                       help="Additional custom characters to include")
    parser.add_argument("--passphrase", action="store_true",
                       help="Generate passphrase instead of password")
    parser.add_argument("--words", type=int, default=4,
                       help="Number of words in passphrase (default: 4)")
    parser.add_argument("--separator", type=str, default="-",
                       help="Passphrase word separator (default: -)")
    parser.add_argument("--analyze", type=str,
                       help="Analyze strength of provided password")
    
    args = parser.parse_args()
    
    generator = PasswordGenerator()
    
    if args.analyze:
        # Analyze password strength
        analysis = generator.analyze_password_strength(args.analyze)
        is_common = generator.check_common_passwords(args.analyze)
        
        print(f"Password Analysis for: {args.analyze}")
        print(f"Length: {analysis['length']}")
        print(f"Strength: {analysis['strength']}")
        print(f"Entropy: {analysis['entropy']:.2f} bits")
        print(f"Has lowercase: {analysis['has_lowercase']}")
        print(f"Has uppercase: {analysis['has_uppercase']}")
        print(f"Has digits: {analysis['has_digits']}")
        print(f"Has symbols: {analysis['has_symbols']}")
        print(f"Unique characters: {analysis['unique_chars']}")
        print(f"Common password: {is_common}")
        
    elif args.passphrase:
        # Generate passphrase
        for i in range(args.count):
            passphrase = generator.generate_passphrase(
                word_count=args.words,
                separator=args.separator
            )
            print(f"Passphrase {i+1}: {passphrase}")
    
    else:
        # Generate regular passwords
        passwords = generator.generate_multiple_passwords(
            count=args.count,
            length=args.length,
            include_uppercase=not args.no_uppercase,
            include_lowercase=not args.no_lowercase,
            include_digits=not args.no_digits,
            include_symbols=not args.no_symbols,
            exclude_ambiguous=args.exclude_ambiguous,
            custom_chars=args.custom_chars
        )
        
        for i, password in enumerate(passwords):
            print(f"Password {i+1}: {password}")
            
            # Show strength analysis for single password
            if args.count == 1:
                analysis = generator.analyze_password_strength(password)
                print(f"Strength: {analysis['strength']} (Entropy: {analysis['entropy']:.2f} bits)")


if __name__ == "__main__":
    main()