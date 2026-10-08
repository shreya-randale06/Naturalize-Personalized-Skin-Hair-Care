import google.generativeai as genai
from config import Config

def test_gemini():
    try:
        print("Testing Gemini API connection...")
        genai.configure(api_key=Config.GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        response = model.generate_content("What are 3 natural Indian ingredients for glowing skin?")
        print("✅ API Working!")
        print(f"Response: {response.text[:200]}...")
        return True
    except Exception as e:
        print(f"❌ API Error: {e}")
        return False

if __name__ == "__main__":
    test_gemini()