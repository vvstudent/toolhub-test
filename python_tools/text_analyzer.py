#!/usr/bin/env python3
"""
Text Analyzer Tool

A comprehensive tool for analyzing text content including word count, readability metrics,
sentiment analysis, and various text statistics.
"""

import re
import argparse
import math
from collections import Counter
from typing import Dict, List, Tuple, Any
import string


class TextAnalyzer:
    """A comprehensive text analysis tool."""
    
    def __init__(self):
        self.stop_words = {
            'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from',
            'has', 'he', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the',
            'to', 'was', 'will', 'with', 'the', 'this', 'but', 'they', 'have',
            'had', 'what', 'said', 'each', 'which', 'she', 'do', 'how', 'their',
            'if', 'up', 'out', 'many', 'then', 'them', 'these', 'so', 'some',
            'her', 'would', 'make', 'like', 'into', 'him', 'time', 'two', 'more',
            'go', 'no', 'way', 'could', 'my', 'than', 'first', 'been', 'call',
            'who', 'oil', 'sit', 'now', 'find', 'down', 'day', 'did', 'get',
            'come', 'made', 'may', 'part'
        }
    
    def basic_statistics(self, text: str) -> Dict[str, Any]:
        """
        Calculate basic text statistics.
        
        Args:
            text: Input text to analyze
            
        Returns:
            Dictionary containing basic statistics
        """
        # Clean text for word analysis
        words = self._extract_words(text)
        sentences = self._extract_sentences(text)
        paragraphs = self._extract_paragraphs(text)
        
        stats = {
            'character_count': len(text),
            'character_count_no_spaces': len(text.replace(' ', '')),
            'word_count': len(words),
            'sentence_count': len(sentences),
            'paragraph_count': len(paragraphs),
            'average_words_per_sentence': len(words) / len(sentences) if sentences else 0,
            'average_sentences_per_paragraph': len(sentences) / len(paragraphs) if paragraphs else 0,
            'average_word_length': sum(len(word) for word in words) / len(words) if words else 0
        }
        
        return stats
    
    def readability_analysis(self, text: str) -> Dict[str, Any]:
        """
        Calculate various readability metrics.
        
        Args:
            text: Input text to analyze
            
        Returns:
            Dictionary containing readability metrics
        """
        words = self._extract_words(text)
        sentences = self._extract_sentences(text)
        syllables = sum(self._count_syllables(word) for word in words)
        
        if not words or not sentences:
            return {
                'flesch_reading_ease': 0,
                'flesch_kincaid_grade': 0,
                'automated_readability_index': 0,
                'readability_level': 'Cannot determine'
            }
        
        avg_sentence_length = len(words) / len(sentences)
        avg_syllables_per_word = syllables / len(words)
        
        # Flesch Reading Ease
        flesch_ease = 206.835 - (1.015 * avg_sentence_length) - (84.6 * avg_syllables_per_word)
        flesch_ease = max(0, min(100, flesch_ease))  # Clamp between 0-100
        
        # Flesch-Kincaid Grade Level
        flesch_grade = (0.39 * avg_sentence_length) + (11.8 * avg_syllables_per_word) - 15.59
        flesch_grade = max(0, flesch_grade)
        
        # Automated Readability Index
        characters = sum(len(word) for word in words)
        ari = (4.71 * (characters / len(words))) + (0.5 * avg_sentence_length) - 21.43
        ari = max(0, ari)
        
        # Determine readability level
        if flesch_ease >= 90:
            level = "Very Easy"
        elif flesch_ease >= 80:
            level = "Easy"
        elif flesch_ease >= 70:
            level = "Fairly Easy"
        elif flesch_ease >= 60:
            level = "Standard"
        elif flesch_ease >= 50:
            level = "Fairly Difficult"
        elif flesch_ease >= 30:
            level = "Difficult"
        else:
            level = "Very Difficult"
        
        return {
            'flesch_reading_ease': round(flesch_ease, 2),
            'flesch_kincaid_grade': round(flesch_grade, 2),
            'automated_readability_index': round(ari, 2),
            'average_sentence_length': round(avg_sentence_length, 2),
            'average_syllables_per_word': round(avg_syllables_per_word, 2),
            'readability_level': level
        }
    
    def word_frequency_analysis(self, text: str, top_n: int = 10) -> Dict[str, Any]:
        """
        Analyze word frequency in the text.
        
        Args:
            text: Input text to analyze
            top_n: Number of top words to return
            
        Returns:
            Dictionary containing word frequency analysis
        """
        words = self._extract_words(text)
        
        # All words frequency
        all_word_freq = Counter(word.lower() for word in words)
        
        # Content words (excluding stop words)
        content_words = [word.lower() for word in words if word.lower() not in self.stop_words]
        content_word_freq = Counter(content_words)
        
        return {
            'total_unique_words': len(all_word_freq),
            'content_words_count': len(content_words),
            'unique_content_words': len(content_word_freq),
            'lexical_diversity': len(all_word_freq) / len(words) if words else 0,
            'top_words': all_word_freq.most_common(top_n),
            'top_content_words': content_word_freq.most_common(top_n)
        }
    
    def sentiment_analysis(self, text: str) -> Dict[str, Any]:
        """
        Perform basic sentiment analysis using word lists.
        
        Args:
            text: Input text to analyze
            
        Returns:
            Dictionary containing sentiment analysis
        """
        # Simple positive and negative word lists
        positive_words = {
            'good', 'great', 'excellent', 'amazing', 'wonderful', 'fantastic',
            'awesome', 'brilliant', 'outstanding', 'superb', 'magnificent',
            'perfect', 'beautiful', 'love', 'like', 'enjoy', 'happy', 'pleased',
            'satisfied', 'delighted', 'thrilled', 'excited', 'positive', 'best',
            'better', 'success', 'successful', 'win', 'winner', 'victory'
        }
        
        negative_words = {
            'bad', 'terrible', 'awful', 'horrible', 'disgusting', 'hate',
            'dislike', 'angry', 'sad', 'disappointed', 'frustrated', 'annoyed',
            'upset', 'worried', 'concerned', 'problem', 'issue', 'fail', 'failure',
            'lose', 'loss', 'wrong', 'error', 'mistake', 'difficult', 'hard',
            'impossible', 'never', 'worst', 'worse', 'negative', 'poor'
        }
        
        words = [word.lower().strip(string.punctuation) for word in text.split()]
        
        positive_count = sum(1 for word in words if word in positive_words)
        negative_count = sum(1 for word in words if word in negative_words)
        neutral_count = len(words) - positive_count - negative_count
        
        total_sentiment_words = positive_count + negative_count
        
        if total_sentiment_words == 0:
            sentiment = "Neutral"
            confidence = 0
        else:
            sentiment_score = (positive_count - negative_count) / total_sentiment_words
            confidence = total_sentiment_words / len(words) if words else 0
            
            if sentiment_score > 0.1:
                sentiment = "Positive"
            elif sentiment_score < -0.1:
                sentiment = "Negative"
            else:
                sentiment = "Neutral"
        
        return {
            'sentiment': sentiment,
            'confidence': round(confidence, 3),
            'positive_words_count': positive_count,
            'negative_words_count': negative_count,
            'neutral_words_count': neutral_count,
            'sentiment_ratio': round((positive_count - negative_count) / len(words) if words else 0, 3)
        }
    
    def text_complexity_analysis(self, text: str) -> Dict[str, Any]:
        """
        Analyze text complexity using various metrics.
        
        Args:
            text: Input text to analyze
            
        Returns:
            Dictionary containing complexity analysis
        """
        words = self._extract_words(text)
        sentences = self._extract_sentences(text)
        
        if not words:
            return {'error': 'No words found in text'}
        
        # Calculate various complexity metrics
        long_words = [word for word in words if len(word) > 6]
        very_long_words = [word for word in words if len(word) > 10]
        
        # Sentence length variation
        sentence_lengths = [len(self._extract_words(sentence)) for sentence in sentences]
        avg_sentence_length = sum(sentence_lengths) / len(sentence_lengths) if sentence_lengths else 0
        sentence_length_variance = sum((length - avg_sentence_length) ** 2 for length in sentence_lengths) / len(sentence_lengths) if sentence_lengths else 0
        
        return {
            'long_words_percentage': (len(long_words) / len(words)) * 100,
            'very_long_words_count': len(very_long_words),
            'average_word_length': sum(len(word) for word in words) / len(words),
            'sentence_length_variance': round(sentence_length_variance, 2),
            'complexity_score': self._calculate_complexity_score(text),
            'estimated_reading_time_minutes': len(words) / 200  # Assuming 200 WPM reading speed
        }
    
    def _extract_words(self, text: str) -> List[str]:
        """Extract words from text, removing punctuation."""
        return re.findall(r'\b[a-zA-Z]+\b', text)
    
    def _extract_sentences(self, text: str) -> List[str]:
        """Extract sentences from text."""
        sentences = re.split(r'[.!?]+', text)
        return [s.strip() for s in sentences if s.strip()]
    
    def _extract_paragraphs(self, text: str) -> List[str]:
        """Extract paragraphs from text."""
        paragraphs = re.split(r'\n\s*\n', text)
        return [p.strip() for p in paragraphs if p.strip()]
    
    def _count_syllables(self, word: str) -> int:
        """Count syllables in a word (approximation)."""
        word = word.lower()
        vowels = 'aeiouy'
        syllable_count = 0
        previous_was_vowel = False
        
        for char in word:
            is_vowel = char in vowels
            if is_vowel and not previous_was_vowel:
                syllable_count += 1
            previous_was_vowel = is_vowel
        
        # Handle silent 'e'
        if word.endswith('e') and syllable_count > 1:
            syllable_count -= 1
        
        return max(1, syllable_count)
    
    def _calculate_complexity_score(self, text: str) -> float:
        """Calculate a custom complexity score."""
        words = self._extract_words(text)
        sentences = self._extract_sentences(text)
        
        if not words or not sentences:
            return 0
        
        avg_word_length = sum(len(word) for word in words) / len(words)
        avg_sentence_length = len(words) / len(sentences)
        unique_words_ratio = len(set(word.lower() for word in words)) / len(words)
        
        # Weighted complexity score
        complexity = (avg_word_length * 0.3) + (avg_sentence_length * 0.4) + (unique_words_ratio * 0.3)
        return round(complexity, 2)
    
    def analyze_text(self, text: str, include_all: bool = True) -> Dict[str, Any]:
        """
        Perform comprehensive text analysis.
        
        Args:
            text: Input text to analyze
            include_all: Whether to include all analysis types
            
        Returns:
            Dictionary containing all analysis results
        """
        if not text.strip():
            return {'error': 'Empty text provided'}
        
        analysis = {
            'basic_statistics': self.basic_statistics(text),
            'readability': self.readability_analysis(text),
            'word_frequency': self.word_frequency_analysis(text),
            'sentiment': self.sentiment_analysis(text),
            'complexity': self.text_complexity_analysis(text)
        }
        
        return analysis


def main():
    """Main function for command-line usage."""
    parser = argparse.ArgumentParser(description="Analyze text content")
    parser.add_argument("--file", "-f", type=str,
                       help="Path to text file to analyze")
    parser.add_argument("--text", "-t", type=str,
                       help="Text string to analyze")
    parser.add_argument("--basic", action="store_true",
                       help="Show only basic statistics")
    parser.add_argument("--readability", action="store_true",
                       help="Show only readability analysis")
    parser.add_argument("--frequency", action="store_true",
                       help="Show only word frequency analysis")
    parser.add_argument("--sentiment", action="store_true",
                       help="Show only sentiment analysis")
    parser.add_argument("--complexity", action="store_true",
                       help="Show only complexity analysis")
    parser.add_argument("--top-words", type=int, default=10,
                       help="Number of top words to show (default: 10)")
    
    args = parser.parse_args()
    
    # Get text input
    if args.file:
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                text = f.read()
        except FileNotFoundError:
            print(f"Error: File '{args.file}' not found.")
            return
        except Exception as e:
            print(f"Error reading file: {e}")
            return
    elif args.text:
        text = args.text
    else:
        print("Please provide text input using --file or --text")
        return
    
    analyzer = TextAnalyzer()
    
    # Determine which analyses to run
    show_all = not any([args.basic, args.readability, args.frequency, 
                       args.sentiment, args.complexity])
    
    print(f"Text Analysis Results")
    print("=" * 50)
    
    if args.basic or show_all:
        print("\n📊 BASIC STATISTICS")
        print("-" * 20)
        stats = analyzer.basic_statistics(text)
        for key, value in stats.items():
            formatted_key = key.replace('_', ' ').title()
            if isinstance(value, float):
                print(f"{formatted_key}: {value:.2f}")
            else:
                print(f"{formatted_key}: {value}")
    
    if args.readability or show_all:
        print("\n📖 READABILITY ANALYSIS")
        print("-" * 25)
        readability = analyzer.readability_analysis(text)
        for key, value in readability.items():
            formatted_key = key.replace('_', ' ').title()
            print(f"{formatted_key}: {value}")
    
    if args.frequency or show_all:
        print(f"\n🔤 WORD FREQUENCY (Top {args.top_words})")
        print("-" * 30)
        frequency = analyzer.word_frequency_analysis(text, args.top_words)
        print(f"Total unique words: {frequency['total_unique_words']}")
        print(f"Lexical diversity: {frequency['lexical_diversity']:.3f}")
        print("\nTop words:")
        for word, count in frequency['top_words']:
            print(f"  {word}: {count}")
        print("\nTop content words (excluding stop words):")
        for word, count in frequency['top_content_words']:
            print(f"  {word}: {count}")
    
    if args.sentiment or show_all:
        print("\n😊 SENTIMENT ANALYSIS")
        print("-" * 20)
        sentiment = analyzer.sentiment_analysis(text)
        for key, value in sentiment.items():
            formatted_key = key.replace('_', ' ').title()
            print(f"{formatted_key}: {value}")
    
    if args.complexity or show_all:
        print("\n🧠 COMPLEXITY ANALYSIS")
        print("-" * 22)
        complexity = analyzer.text_complexity_analysis(text)
        for key, value in complexity.items():
            formatted_key = key.replace('_', ' ').title()
            if isinstance(value, float):
                print(f"{formatted_key}: {value:.2f}")
            else:
                print(f"{formatted_key}: {value}")


if __name__ == "__main__":
    main()