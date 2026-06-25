import pytest
import re
import unicodedata

class TestTokenization:
    def test_basic_word_tokenization(self):
        text = "Hello world this is a test"
        tokens = text.split()
        assert len(tokens) == 6

    def test_punctuation_handling(self):
        text = "Hello, world! How are you?"
        tokens = re.findall(r"\b\w+\b", text)
        assert "Hello" in tokens
        assert "world" in tokens
        assert "," not in tokens

    def test_lowercasing(self):
        tokens = ["Hello","WORLD","Python"]
        lower = [t.lower() for t in tokens]
        assert lower == ["hello","world","python"]

    def test_stopword_removal(self):
        stopwords = {"the","a","an","is","in","on","at","of"}
        tokens = ["the","cat","is","on","a","mat"]
        filtered = [t for t in tokens if t not in stopwords]
        assert filtered == ["cat","mat"]

    def test_ngram_generation(self):
        tokens = ["I","love","NLP"]
        bigrams = [(tokens[i],tokens[i+1]) for i in range(len(tokens)-1)]
        assert bigrams == [("I","love"),("love","NLP")]

class TestNormalization:
    def test_unicode_normalization(self):
        text = "café"
        normalized = unicodedata.normalize("NFC", text)
        assert len(normalized) > 0

    def test_number_normalization(self):
        text = "I have 3 cats and 10 dogs"
        normalized = re.sub(r"\d+", "<NUM>", text)
        assert "<NUM>" in normalized
        assert "3" not in normalized

    def test_special_char_removal(self):
        text = "Hello @world #NLP !!!"
        clean = re.sub(r"[^a-zA-Z\s]", "", text).strip()
        assert "@" not in clean and "#" not in clean

class TestDescriptiveStats:
    def test_word_frequency(self):
        from collections import Counter
        tokens = ["cat","dog","cat","bird","dog","cat"]
        freq = Counter(tokens)
        assert freq["cat"] == 3
        assert freq["dog"] == 2

    def test_vocabulary_size(self):
        tokens = ["cat","dog","cat","bird","dog","cat"]
        vocab = set(tokens)
        assert len(vocab) == 3

    def test_average_word_length(self):
        tokens = ["cat","elephant","hi"]
        avg = sum(len(t) for t in tokens) / len(tokens)
        assert round(avg, 2) == round((3+8+2)/3, 2)
