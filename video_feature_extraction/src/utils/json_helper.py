import json

def save_features_to_json(features, output_path):
    """
    Saves the extracted features to a JSON file.
    
    :param features: List of features extracted from the frames.
    :param output_path: Path to the output JSON file.
    """
    with open(output_path, 'w') as f:
        json.dump(features, f, indent=4)
