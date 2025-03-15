import requests
import time

API_URL = "https://your-app-name.onrender.com/predict"

def test_pair(text1, text2, retries=5):
    """Test with cold start handling"""
    for attempt in range(retries):
        try:
            response = requests.post(
                API_URL,
                json={"text1": text1, "text2": text2},
                timeout=30
            )
            
            if response.status_code == 200:
                return response.json()['similarity score']
            
            print(f"Attempt {attempt+1} failed (HTTP {response.status_code})")
            print("Response:", response.text)
            
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt+1} failed: {str(e)}")
        
        time.sleep(15 * (attempt+1))  # Exponential backoff
    
    return None

if __name__ == "__main__":
    # Sample from your dataset
    test_cases = [
        (
            "broadband challenges tv viewing...",  # Full text 1
            "rap boss arrested over drug find...",  # Full text 2
            0.1  # Expected low similarity
        ),
        (
            "player burn-out worries robinson...",
            "hanks greeted at wintry premiere...",
            0.15
        )
    ]
    
    for text1, text2, expected in test_cases:
        print(f"\nTesting:\nT1: {text1[:50]}...\nT2: {text2[:50]}...")
        score = test_pair(text1, text2)
        
        if score is not None:
            print(f"Score: {score} | Expected: {expected}")
            print(f"Verdict: {'✅' if abs(score - expected) < 0.2 else '❌'}")
        else:
            print("All attempts failed")