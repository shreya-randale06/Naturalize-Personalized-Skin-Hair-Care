import google.generativeai as genai
import json
from datetime import datetime
from config import Config
from data_fetcher import DataFetcher

class AIEngine:
    def __init__(self):
        self.model = None
        self.data_fetcher = DataFetcher()
        
        try:
            # Initialize Gemini AI
            if Config.GEMINI_API_KEY:
                genai.configure(api_key=Config.GEMINI_API_KEY)
                self.model = genai.GenerativeModel('gemini-2.5-flash')
                print("✅ AI Engine initialized with Gemini API")
            else:
                print("⚠️ No Gemini API key found")
                
        except Exception as e:
            print(f"⚠️ Error initializing Gemini: {e}")
    
    def generate_skin_recommendations(self, age, skin_type, skin_tone, concerns):
        """Generate natural skincare recommendations"""
        
        print(f"\n{'='*60}")
        print(f"🎯 GENERATING SKIN RECOMMENDATIONS")
        print(f"Age: {age}, Skin Type: {skin_type}, Skin Tone: {skin_tone}")
        print(f"Concerns: {concerns}")
        print(f"{'='*60}\n")
        
        # Fetch real data
        real_data = self.data_fetcher.fetch_skincare_data(skin_type, concerns, age)
        
        print(f"📊 Fetched {len(real_data.get('ingredients', []))} natural ingredients")
        print(f"📊 Fetched {len(real_data.get('tips', []))} tips")
        
        # Format ingredients for the prompt
        ingredients_text = self._format_ingredients_for_prompt(real_data['ingredients'])
        
        # Try to use AI if available
        if self.model:
            try:
                # Create a specific prompt for skin
                prompt = f"""You are an Ayurvedic skincare expert. Create personalized natural skincare recommendations.

USER DETAILS:
- Age: {age} years
- Skin Type: {skin_type}
- Skin Tone: {skin_tone}
- Specific Concerns: {concerns}

NATURAL INGREDIENTS & REMEDIES (Use these specific ingredients in your recommendations):
{ingredients_text}

DAILY ROUTINE:
Morning: {real_data['routines']['morning']}
Night: {real_data['routines']['night']}

TIPS:
{real_data['tips'][:5]}

Based on the information above, create a response in this EXACT format (use the ingredients provided):

Summary:
[Write 2-3 sentences about natural approach for this specific skin type and concerns]

Morning Routine:
- [Step 1 using a natural ingredient from above]
- [Step 2 using a natural ingredient from above]
- [Step 3 using a natural ingredient from above]

Night Routine:
- [Step 1 using a natural ingredient from above]
- [Step 2 using a natural ingredient from above]
- [Step 3 using a natural ingredient from above]

Home Remedies:
- [Remedy name from above]: [How to use] - [Benefits] - [Use frequency]
- [Remedy name from above]: [How to use] - [Benefits] - [Use frequency]
- [Remedy name from above]: [How to use] - [Benefits] - [Use frequency]

Tips:
- [Tip 1 from above]
- [Tip 2 from above]
- [Tip 3 from above]
- [Tip 4 from above]"""
                
                print("🤖 Calling Gemini API for skin recommendations...")
                response = self.model.generate_content(prompt)
                print("✅ Gemini response received")
                
                # Parse the response
                parsed_response = self._parse_skin_response(response.text)
                
                # Add metadata
                parsed_response['generated_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                parsed_response['data_sources'] = ['Ayurveda', 'Traditional Indian Remedies']
                parsed_response['ai_powered'] = True
                
                print("✅ Successfully generated AI recommendations for skin")
                return parsed_response
                
            except Exception as e:
                print(f"⚠️ AI generation failed: {e}")
                import traceback
                traceback.print_exc()
                print("Falling back to natural remedies database...")
                return self._create_natural_skin_response(real_data)
        else:
            print("⚠️ No AI model available, using fallback")
            return self._create_natural_skin_response(real_data)
    
    def generate_hair_recommendations(self, hair_type, concerns):
        """Generate natural haircare recommendations"""
        
        print(f"\n{'='*60}")
        print(f"🎯 GENERATING HAIR RECOMMENDATIONS")
        print(f"Hair Type: {hair_type}, Concerns: {concerns}")
        print(f"{'='*60}\n")
        
        # Fetch real data
        real_data = self.data_fetcher.fetch_haircare_data(hair_type, concerns)
        
        print(f"📊 Fetched {len(real_data.get('ingredients', []))} natural ingredients")
        print(f"📊 Fetched {len(real_data.get('tips', []))} tips")
        
        # Format ingredients for the prompt
        ingredients_text = self._format_ingredients_for_prompt(real_data['ingredients'])
        
        # Format routine
        routine_text = self._format_routine_for_prompt(real_data['routines'])
        
        # Try to use AI if available
        if self.model:
            try:
                # Create a specific prompt for hair
                prompt = f"""You are an Ayurvedic haircare expert. Create personalized natural haircare recommendations.

USER DETAILS:
- Hair Type: {hair_type}
- Specific Concerns: {concerns}

NATURAL INGREDIENTS & REMEDIES (Use these specific ingredients in your recommendations):
{ingredients_text}

HAIR ROUTINE:
{routine_text}

TIPS:
{real_data['tips'][:5]}

Based on the information above, create a response in this EXACT format (use the ingredients provided):

Summary:
[Write 2-3 sentences about natural approach for this specific hair type and concerns]

Hair Care Routine:
- [Step 1 using a natural ingredient from above]
- [Step 2 using a natural ingredient from above]
- [Step 3 using a natural ingredient from above]

Home Remedies:
- [Remedy name from above]: [How to use] - [Benefits] - [Use frequency]
- [Remedy name from above]: [How to use] - [Benefits] - [Use frequency]
- [Remedy name from above]: [How to use] - [Benefits] - [Use frequency]

Tips:
- [Tip 1 from above]
- [Tip 2 from above]
- [Tip 3 from above]
- [Tip 4 from above]"""
                
                print("🤖 Calling Gemini API for hair recommendations...")
                response = self.model.generate_content(prompt)
                print("✅ Gemini response received")
                
                # Parse the response
                parsed_response = self._parse_hair_response(response.text)
                
                # Add metadata
                parsed_response['generated_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                parsed_response['data_sources'] = ['Ayurveda', 'Traditional Indian Remedies']
                parsed_response['ai_powered'] = True
                
                print("✅ Successfully generated AI recommendations for hair")
                return parsed_response
                
            except Exception as e:
                print(f"⚠️ AI generation failed: {e}")
                import traceback
                traceback.print_exc()
                print("Falling back to natural remedies database...")
                return self._create_natural_hair_response(real_data)
        else:
            print("⚠️ No AI model available, using fallback")
            return self._create_natural_hair_response(real_data)
    
    def _format_ingredients_for_prompt(self, ingredients):
        """Format ingredients for prompt"""
        if not ingredients:
            return "No specific ingredients found. Use general natural ingredients like aloe vera, coconut oil, turmeric, besan."
        
        formatted = []
        for ing in ingredients[:5]:  # Take top 5 ingredients
            formatted.append(f"- {ing['name']}:")
            formatted.append(f"  Benefits: {ing['benefits']}")
            formatted.append(f"  How to use: {ing['how_to_use']}")
            formatted.append(f"  Frequency: {ing['frequency']}")
        return "\n".join(formatted)
    
    def _format_routine_for_prompt(self, routine):
        """Format routine for prompt"""
        if not routine:
            return "No specific routine found"
        
        formatted = []
        for key, value in routine.items():
            formatted.append(f"{key.capitalize()}: {value}")
        return "\n".join(formatted)
    
    def _parse_skin_response(self, response_text):
        """Parse skin response into structured format"""
        structured_data = {
            'summary': [],
            'morning': [],
            'night': [],
            'remedies': [],
            'tips': []
        }
        
        sections = {
            'Summary:': 'summary',
            'Morning Routine:': 'morning',
            'Night Routine:': 'night',
            'Home Remedies:': 'remedies',
            'Tips:': 'tips'
        }
        
        current_section = None
        
        for line in response_text.split('\n'):
            line = line.strip()
            if not line:
                continue
            
            if line in sections:
                current_section = sections[line]
                continue
            
            if current_section and line.startswith('-'):
                structured_data[current_section].append(line[1:].strip())
            elif current_section and current_section == 'summary' and not line.startswith('-'):
                structured_data[current_section].append(line)
        
        # Clean up empty sections
        for key in structured_data:
            if not structured_data[key]:
                if key == 'remedies':
                    structured_data[key] = ["• Apply aloe vera gel daily for hydration", "• Use turmeric face pack twice a week"]
                elif key == 'tips':
                    structured_data[key] = ["Drink warm water with lemon daily", "Get 7-8 hours of sleep"]
                else:
                    structured_data[key] = ["No recommendations available"]
        
        return structured_data
    
    def _parse_hair_response(self, response_text):
        """Parse hair response into structured format"""
        structured_data = {
            'summary': [],
            'routine': [],
            'remedies': [],
            'tips': []
        }
        
        sections = {
            'Summary:': 'summary',
            'Hair Care Routine:': 'routine',
            'Home Remedies:': 'remedies',
            'Tips:': 'tips'
        }
        
        current_section = None
        
        for line in response_text.split('\n'):
            line = line.strip()
            if not line:
                continue
            
            if line in sections:
                current_section = sections[line]
                continue
            
            if current_section and line.startswith('-'):
                structured_data[current_section].append(line[1:].strip())
            elif current_section and current_section == 'summary' and not line.startswith('-'):
                structured_data[current_section].append(line)
        
        for key in structured_data:
            if not structured_data[key]:
                if key == 'remedies':
                    structured_data[key] = ["• Coconut oil massage twice a week", "• Apply amla powder mask weekly"]
                elif key == 'tips':
                    structured_data[key] = ["Eat protein-rich foods", "Drink plenty of water"]
                else:
                    structured_data[key] = ["No recommendations available"]
        
        return structured_data
    
    def _create_natural_skin_response(self, real_data):
        """Create natural skin response with actual data"""
        
        # Format remedies from ingredients
        remedies = []
        for ing in real_data.get('ingredients', [])[:4]:
            remedies.append(f"• {ing['name']}: {ing['how_to_use']} - Benefits: {ing['benefits']} - Use {ing['frequency']}")
        
        # Format products if available
        products = []
        for p in real_data.get('products', [])[:3]:
            products.append(f"• {p['name']} - {p['price']} - Available at: {p['available_at']}")
        
        return {
            'summary': [f"🌿 Based on Ayurvedic principles, here are natural remedies for your skin."],
            'morning': real_data['routines']['morning'],
            'night': real_data['routines']['night'],
            'remedies': remedies,
            'tips': real_data['tips'][:8]
        }
    
    def _create_natural_hair_response(self, real_data):
        """Create natural hair response with actual data"""
        
        # Format remedies from ingredients
        remedies = []
        for ing in real_data.get('ingredients', [])[:4]:
            remedies.append(f"• {ing['name']}: {ing['how_to_use']} - Benefits: {ing['benefits']} - Use {ing['frequency']}")
        
        # Format routine
        routine_list = []
        for key, value in real_data['routines'].items():
            routine_list.append(f"• {key.capitalize()}: {value}")
        
        return {
            'summary': [f"🌿 Ayurvedic remedies for your hair using natural ingredients."],
            'routine': routine_list,
            'remedies': remedies,
            'tips': real_data['tips'][:8]
        }