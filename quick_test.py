from ai_engine import AIEngine
from config import Config

def test_skin():
    print("Testing Skin Recommendations...")
    ai = AIEngine()
    
    # Test different scenarios
    test_cases = [
        (25, "Oily", "Medium", "acne, oily skin, large pores"),
        (35, "Dry", "Fair", "dryness, aging, fine lines"),
        (28, "Combination", "Medium", "pigmentation, dullness"),
        (45, "Sensitive", "Fair", "redness, sensitivity")
    ]
    
    for age, skin_type, tone, concerns in test_cases:
        print(f"\n{'='*60}")
        print(f"Testing: Age {age}, {skin_type} skin, {concerns}")
        print('='*60)
        
        result = ai.generate_skin_recommendations(age, skin_type, tone, concerns)
        
        print(f"\n✅ Summary: {result['summary'][0][:150]}...")
        print(f"✅ Morning Routine: {len(result['morning'])} steps")
        print(f"✅ Night Routine: {len(result['night'])} steps")
        print(f"✅ Remedies: {len(result['remedies'])} remedies")
        print(f"✅ Tips: {len(result['tips'])} tips")
        print(f"✅ AI Powered: {result.get('ai_powered', False)}")
        
        # Show first remedy
        if result['remedies']:
            print(f"✅ Sample Remedy: {result['remedies'][0][:100]}...")
        
        print("\n" + "-"*60)

def test_hair():
    print("\n\nTesting Hair Recommendations...")
    ai = AIEngine()
    
    test_cases = [
        ("Curly", "frizz, dryness, split ends"),
        ("Straight", "hair fall, dandruff"),
        ("Wavy", "frizz, slow growth"),
        ("Straight", "premature greying, thinning")
    ]
    
    for hair_type, concerns in test_cases:
        print(f"\n{'='*60}")
        print(f"Testing: {hair_type} hair, {concerns}")
        print('='*60)
        
        result = ai.generate_hair_recommendations(hair_type, concerns)
        
        print(f"\n✅ Summary: {result['summary'][0][:150]}...")
        print(f"✅ Routine: {len(result['routine'])} steps")
        print(f"✅ Remedies: {len(result['remedies'])} remedies")
        print(f"✅ Tips: {len(result['tips'])} tips")
        print(f"✅ AI Powered: {result.get('ai_powered', False)}")
        
        # Show first remedy
        if result['remedies']:
            print(f"✅ Sample Remedy: {result['remedies'][0][:100]}...")
        
        print("\n" + "-"*60)

if __name__ == "__main__":
    test_skin()
    test_hair()