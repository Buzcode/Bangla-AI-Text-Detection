def extract_all_features(text):
    # Check if text is valid
    if not isinstance(text, str) or len(text.strip()) == 0:
        return {"token_count": 0, "unique_token_count": 0, "lexical_diversity": 0, "stopword_count": 0}

    # Get Handcrafted Features
    features = get_handcrafted_features(text)

    # Get Stopword Count
    features['stopword_count'] = count_stopwords(text)

    # Note: We will add embedding logic here once the dataset is ready
    return features

# Quick test
print(extract_all_features("আমি এই কাজটি করেছি।"))
