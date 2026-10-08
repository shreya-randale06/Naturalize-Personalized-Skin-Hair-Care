import json
from datetime import datetime

class DataFetcher:
    def __init__(self):
        self.cache = {}
        
        # Indian Natural Products Database - Ayurvedic & Home Remedies
        self.indian_natural_db = self._initialize_indian_natural_db()
        
    def _initialize_indian_natural_db(self):
        """Initialize with Indian natural ingredients and home remedies"""
        return {
            'skincare': {
                'Oily': {
                    'ingredients': [
                        {
                            'name': 'Multani Mitti (Fuller\'s Earth)',
                            'benefits': 'Absorbs excess oil, deep cleanses pores, removes impurities',
                            'how_to_use': 'Mix with rose water or curd to make a paste. Apply for 15 mins, wash off.',
                            'frequency': '2-3 times per week',
                            'precautions': 'Not for very dry skin. Moisturize after use.'
                        },
                        {
                            'name': 'Neem (Azadirachta indica)',
                            'benefits': 'Antibacterial, anti-acne, controls oil, reduces inflammation',
                            'how_to_use': 'Make paste of neem leaves with turmeric. Apply on acne-prone areas.',
                            'frequency': 'Daily as spot treatment',
                            'precautions': 'Do a patch test first'
                        },
                        {
                            'name': 'Besan (Gram Flour)',
                            'benefits': 'Natural cleanser, absorbs oil, gentle exfoliation',
                            'how_to_use': 'Mix with curd and turmeric. Use as face pack.',
                            'frequency': '2 times per week',
                            'precautions': 'Avoid if allergic to chickpeas'
                        },
                        {
                            'name': 'Tea Tree Oil',
                            'benefits': 'Antiseptic, fights acne bacteria, controls sebum',
                            'how_to_use': 'Add 2-3 drops to carrier oil or face pack',
                            'frequency': 'As needed',
                            'precautions': 'Always dilute, never apply directly'
                        }
                    ],
                    'routine': {
                        'morning': [
                            "Wash face with besan and turmeric paste mixed with rose water",
                            "Apply fresh aloe vera gel as moisturizer",
                            "Use neem-based natural sunscreen if going out"
                        ],
                        'night': [
                            "Oil cleanse with sesame oil or jojoba oil",
                            "Apply multani mitti face pack (2-3 times/week)",
                            "Spot treatment with neem-turmeric paste on acne",
                            "Light moisturizer with aloe vera"
                        ]
                    },
                    'products': [
                        {
                            'name': 'Khadi Natural Neem & Tulsi Face Wash',
                            'price': '₹150-200',
                            'available_at': 'Khadi stores, Amazon, Flipkart',
                            'natural_ingredients': ['Neem', 'Tulsi', 'Aloe Vera'],
                            'certification': 'Ayurvedic'
                        },
                        {
                            'name': 'Forest Essentials Facial Ubtan (Multani Mitti)',
                            'price': '₹695',
                            'available_at': 'Forest Essentials stores, Nykaa',
                            'natural_ingredients': ['Multani Mitti', 'Sandalwood', 'Turmeric'],
                            'certification': 'Ayurvedic'
                        },
                        {
                            'name': 'Jovees Neem & Tulsi Anti-Acne Face Pack',
                            'price': '₹175',
                            'available_at': 'Local stores, Amazon',
                            'natural_ingredients': ['Neem', 'Tulsi', 'Tea Tree'],
                            'certification': 'Herbal'
                        }
                    ]
                },
                'Dry': {
                    'ingredients': [
                        {
                            'name': 'Aloe Vera',
                            'benefits': 'Deep hydration, soothes dry skin, healing properties',
                            'how_to_use': 'Extract fresh gel, apply directly, leave for 20 mins',
                            'frequency': 'Daily',
                            'precautions': 'Use fresh plant for best results'
                        },
                        {
                            'name': 'Coconut Oil (Nariyal Tel)',
                            'benefits': 'Intense moisturization, nourishes dry skin, Vitamin E rich',
                            'how_to_use': 'Warm slightly and massage before bath',
                            'frequency': '3-4 times per week',
                            'precautions': 'Use virgin coconut oil'
                        },
                        {
                            'name': 'Honey (Shahad)',
                            'benefits': 'Natural humectant, antibacterial, softens skin',
                            'how_to_use': 'Mix with milk or curd, apply as mask',
                            'frequency': '2-3 times per week',
                            'precautions': 'Use pure, unprocessed honey'
                        },
                        {
                            'name': 'Sandalwood (Chandan)',
                            'benefits': 'Cooling, soothing, moisturizing, anti-inflammatory',
                            'how_to_use': 'Make paste with rose water or milk',
                            'frequency': '2 times per week',
                            'precautions': 'Buy pure sandalwood powder'
                        }
                    ],
                    'routine': {
                        'morning': [
                            "Splash face with plain water (no soap if possible)",
                            "Apply fresh aloe vera gel",
                            "Use glycerin and rose water as toner",
                            "Light moisturizer with almond oil"
                        ],
                        'night': [
                            "Cleanse with raw milk or cream",
                            "Apply honey and malai (cream) mask",
                            "Massage with coconut oil or almond oil",
                            "Apply sandalwood paste for glow"
                        ]
                    },
                    'products': [
                        {
                            'name': 'Biotique Bio Coconut Whitening & Nourishing Cream',
                            'price': '₹150',
                            'available_at': 'Local stores, Amazon, Nykaa',
                            'natural_ingredients': ['Coconut', 'Honey', 'Saffron'],
                            'certification': 'Ayurvedic'
                        },
                        {
                            'name': 'Himalaya Herbals Nourishing Skin Cream',
                            'price': '₹85',
                            'available_at': 'All medical stores, supermarkets',
                            'natural_ingredients': ['Aloe Vera', 'Wheat Germ Oil'],
                            'certification': 'Herbal'
                        }
                    ]
                },
                'Combination': {
                    'ingredients': [
                        {
                            'name': 'Rose Water (Gulab Jal)',
                            'benefits': 'Balances pH, tones skin, refreshing',
                            'how_to_use': 'Use as toner after cleansing',
                            'frequency': 'Daily',
                            'precautions': 'Buy pure, chemical-free rose water'
                        },
                        {
                            'name': 'Curd (Dahi)',
                            'benefits': 'Lactic acid exfoliation, moisturizes dry areas, controls oil',
                            'how_to_use': 'Apply as face pack with besan or honey',
                            'frequency': '2-3 times per week',
                            'precautions': 'Use fresh, plain curd'
                        },
                        {
                            'name': 'Turmeric (Haldi)',
                            'benefits': 'Anti-inflammatory, brightening, antibacterial',
                            'how_to_use': 'Mix with curd or milk, apply as pack',
                            'frequency': '2 times per week',
                            'precautions': 'May stain, use small amount'
                        }
                    ],
                    'routine': {
                        'morning': [
                            "Cleanse with besan and curd",
                            "Rose water toner",
                            "Light aloe vera gel moisturizer"
                        ],
                        'night': [
                            "Oil cleanse with jojoba or grapeseed oil",
                            "Multani mitti pack (T-zone only, 2 times/week)",
                            "Honey and curd mask for overall face"
                        ]
                    }
                },
                'Sensitive': {
                    'ingredients': [
                        {
                            'name': 'Aloe Vera',
                            'benefits': 'Soothes irritation, calming, cooling',
                            'how_to_use': 'Fresh gel applied daily',
                            'frequency': 'Daily',
                            'precautions': 'Test on small area first'
                        },
                        {
                            'name': 'Cucumber (Kheera)',
                            'benefits': 'Cooling, reduces redness, soothes inflammation',
                            'how_to_use': 'Grate and apply juice or slices',
                            'frequency': 'Daily as needed',
                            'precautions': 'Use fresh cucumber'
                        },
                        {
                            'name': 'Saffron (Kesar)',
                            'benefits': 'Gentle brightening, soothing, antioxidant',
                            'how_to_use': 'Soak strands in milk, apply mixture',
                            'frequency': '1-2 times per week',
                            'precautions': 'Use genuine saffron'
                        }
                    ],
                    'routine': {
                        'morning': [
                            "Wash with plain water only",
                            "Apply fresh cucumber juice",
                            "Aloe vera gel as moisturizer"
                        ],
                        'night': [
                            "Cleanse with raw milk",
                            "Apply aloe vera and sandalwood pack",
                            "Light almond oil massage"
                        ]
                    }
                }
            },
            'haircare': {
                'Curly': {
                    'ingredients': [
                        {
                            'name': 'Coconut Oil (Nariyal Tel)',
                            'benefits': 'Deep conditioning, reduces frizz, promotes growth',
                            'how_to_use': 'Warm oil, massage scalp, leave overnight',
                            'frequency': '2-3 times per week',
                            'precautions': 'Use virgin coconut oil'
                        },
                        {
                            'name': 'Amla (Indian Gooseberry)',
                            'benefits': 'Strengthens roots, prevents greying, adds shine',
                            'how_to_use': 'Make amla powder paste with water, apply to hair',
                            'frequency': 'Weekly',
                            'precautions': 'Can be drying, follow with conditioner'
                        },
                        {
                            'name': 'Fenugreek (Methi) Seeds',
                            'benefits': 'Conditions, defines curls, reduces hair fall',
                            'how_to_use': 'Soak overnight, grind to paste, apply',
                            'frequency': 'Weekly',
                            'precautions': 'Wash thoroughly to remove smell'
                        },
                        {
                            'name': 'Shikakai',
                            'benefits': 'Natural shampoo, gentle cleansing, adds volume',
                            'how_to_use': 'Make powder paste, use as shampoo',
                            'frequency': '1-2 times per week',
                            'precautions': 'May be drying, use conditioner after'
                        }
                    ],
                    'routine': {
                        'wash': "Wash with shikakai and reetha powder mixed with water (1-2 times/week)",
                        'condition': "Apply methi seed paste or curd as conditioner",
                        'deep_condition': "Hot coconut oil treatment with amla, weekly",
                        'style': "Apply aloe vera gel as leave-in conditioner",
                        'protect': "Use silk scarf or satin pillowcase"
                    }
                },
                'Straight': {
                    'ingredients': [
                        {
                            'name': 'Amla (Indian Gooseberry)',
                            'benefits': 'Strengthens, adds shine, prevents hair fall',
                            'how_to_use': 'Amla powder + water paste, leave 30 mins',
                            'frequency': 'Weekly',
                            'precautions': 'Can be drying'
                        },
                        {
                            'name': 'Brahmi',
                            'benefits': 'Promotes growth, reduces stress, nourishes scalp',
                            'how_to_use': 'Brahmi powder with coconut oil',
                            'frequency': 'Weekly',
                            'precautions': 'Use consistently for results'
                        },
                        {
                            'name': 'Henna (Mehendi)',
                            'benefits': 'Conditions, adds volume, natural color',
                            'how_to_use': 'Mix with amla powder, apply as mask',
                            'frequency': 'Once a month',
                            'precautions': 'Can dry hair, use conditioner after'
                        }
                    ],
                    'routine': {
                        'wash': "Use reetha and shikakai shampoo (2 times/week)",
                        'condition': "Apply curd and honey mix",
                        'treatment': "Weekly amla and brahmi oil massage",
                        'style': "Apply coconut oil to ends to prevent split ends"
                    }
                },
                'Wavy': {
                    'ingredients': [
                        {
                            'name': 'Aloe Vera',
                            'benefits': 'Enhances waves, moisturizes, reduces frizz',
                            'how_to_use': 'Fresh gel as leave-in conditioner',
                            'frequency': 'After each wash',
                            'precautions': 'Use fresh plant'
                        },
                        {
                            'name': 'Flax Seeds (Alsi)',
                            'benefits': 'Natural gel, defines waves, adds shine',
                            'how_to_use': 'Boil seeds, strain gel, apply',
                            'frequency': 'After washing',
                            'precautions': 'Refrigerate gel for up to 1 week'
                        },
                        {
                            'name': 'Rice Water',
                            'benefits': 'Strengthens, adds shine, promotes growth',
                            'how_to_use': 'Ferment overnight, use as final rinse',
                            'frequency': 'Once a week',
                            'precautions': 'Don\'t leave on for too long'
                        }
                    ],
                    'routine': {
                        'wash': "Natural shampoo with reetha and shikakai",
                        'condition': "Apply aloe vera gel as leave-in",
                        'style': "Use flax seed gel for wave definition",
                        'protect': "Air dry, scrunch with microfiber towel"
                    }
                }
            }
        }
    
    def fetch_skincare_data(self, skin_type, concerns, age):
        """Fetch Indian natural skincare data"""
        
        print(f"🌿 Fetching Ayurvedic skincare data for {skin_type} skin...")
        
        # Get data for skin type
        skin_data = self.indian_natural_db['skincare'].get(skin_type, self.indian_natural_db['skincare']['Combination'])
        
        # Add concern-specific remedies
        concern_remedies = self._get_concern_remedies('skincare', concerns)
        
        # Combine all ingredients
        all_ingredients = skin_data['ingredients'] + concern_remedies
        
        return {
            'ingredients': all_ingredients[:8],
            'routines': skin_data['routine'],
            'products': skin_data.get('products', []),
            'tips': self._get_natural_tips('skincare', skin_type, concerns),
            'sources': ['Ayurveda', 'Grandma\'s Remedies', 'Natural Skincare Experts'],
            'generated_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    
    def fetch_haircare_data(self, hair_type, concerns):
        """Fetch Indian natural haircare data"""
        
        print(f"🌿 Fetching Ayurvedic haircare data for {hair_type} hair...")
        
        # Get data for hair type
        hair_data = self.indian_natural_db['haircare'].get(hair_type, self.indian_natural_db['haircare']['Straight'])
        
        # Add concern-specific remedies
        concern_remedies = self._get_concern_remedies('haircare', concerns)
        
        return {
            'ingredients': hair_data.get('ingredients', []) + concern_remedies,
            'routines': hair_data['routine'],
            'tips': self._get_natural_tips('haircare', hair_type, concerns),
            'sources': ['Ayurveda', 'Traditional Indian Remedies', 'Natural Hair Experts'],
            'generated_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    
    def _get_concern_remedies(self, category, concerns):
        """Get remedies for specific concerns"""
        
        remedies = []
        concerns_lower = concerns.lower()
        
        if category == 'skincare':
            if 'acne' in concerns_lower or 'pimple' in concerns_lower:
                remedies.append({
                    'name': 'Neem & Turmeric Paste',
                    'benefits': 'Powerful antibacterial combination, reduces acne, prevents scarring',
                    'how_to_use': 'Grind fresh neem leaves, mix with turmeric, apply to affected areas',
                    'frequency': 'Daily spot treatment',
                    'precautions': 'May cause slight yellow tint, wash off after 20 mins'
                })
                remedies.append({
                    'name': 'Sandalwood & Rose Water Paste',
                    'benefits': 'Cooling, reduces inflammation, prevents breakouts',
                    'how_to_use': 'Mix sandalwood powder with rose water, apply as mask',
                    'frequency': '3 times per week',
                    'precautions': 'Use pure sandalwood powder'
                })
                
            if 'pigmentation' in concerns_lower or 'dark spot' in concerns_lower:
                remedies.append({
                    'name': 'Licorice (Mulethi) & Saffron Mask',
                    'benefits': 'Lightens dark spots, even skin tone, natural brightening',
                    'how_to_use': 'Mix mulethi powder with milk, add few saffron strands, apply',
                    'frequency': '2-3 times per week',
                    'precautions': 'Consistent use shows results in 4-6 weeks'
                })
                
            if 'dullness' in concerns_lower:
                remedies.append({
                    'name': 'Besan, Haldi & Malai Pack',
                    'benefits': 'Instant glow, exfoliation, brightening',
                    'how_to_use': 'Mix besan with turmeric and fresh cream, apply as pack',
                    'frequency': '2 times per week',
                    'precautions': 'Avoid if allergic to dairy'
                })
                
        elif category == 'haircare':
            if 'hair fall' in concerns_lower or 'thinning' in concerns_lower:
                remedies.append({
                    'name': 'Amla, Brahmi & Bhringraj Oil',
                    'benefits': 'Strengthens roots, prevents hair fall, promotes growth',
                    'how_to_use': 'Mix amla, brahmi, bhringraj powders in coconut oil, heat, massage',
                    'frequency': '2-3 times per week',
                    'precautions': 'Warm slightly before applying'
                })
                remedies.append({
                    'name': 'Onion Juice',
                    'benefits': 'Sulfur-rich, stimulates follicles, promotes regrowth',
                    'how_to_use': 'Extract juice, apply to scalp, leave 30 mins, wash',
                    'frequency': '2 times per week',
                    'precautions': 'May have strong smell, add few drops essential oil'
                })
                
            if 'dandruff' in concerns_lower:
                remedies.append({
                    'name': 'Lemon & Yogurt Mask',
                    'benefits': 'Antifungal, removes flakes, soothes scalp',
                    'how_to_use': 'Mix fresh yogurt with lemon juice, apply to scalp',
                    'frequency': '2 times per week',
                    'precautions': 'Don\'t leave for more than 30 mins if sensitive'
                })
                remedies.append({
                    'name': 'Tea Tree & Coconut Oil',
                    'benefits': 'Antifungal, antibacterial, moisturizes scalp',
                    'how_to_use': 'Add tea tree oil to warm coconut oil, massage scalp',
                    'frequency': '2 times per week',
                    'precautions': 'Always dilute tea tree oil'
                })
                
            if 'frizz' in concerns_lower:
                remedies.append({
                    'name': 'Aloe Vera & Coconut Oil Mix',
                    'benefits': 'Smooths hair cuticles, controls frizz, adds shine',
                    'how_to_use': 'Mix aloe gel with coconut oil, apply as leave-in',
                    'frequency': 'After each wash',
                    'precautions': 'Use fresh aloe for best results'
                })
                
            if 'slow growth' in concerns_lower:
                remedies.append({
                    'name': 'Fenugreek (Methi) Seeds Mask',
                    'benefits': 'Rich in proteins, stimulates growth, strengthens roots',
                    'how_to_use': 'Soak overnight, grind to paste, apply to scalp and hair',
                    'frequency': 'Weekly',
                    'precautions': 'Wash thoroughly to remove all seeds'
                })
            # Add to the haircare section in _get_concern_remedies

            if 'premature greying' in concerns_lower or 'white hair' in concerns_lower:
                remedies.append({
        'name': 'Amla & Bhringraj Oil',
        'benefits': 'Prevents premature greying, darkens hair naturally, nourishes scalp',
        'how_to_use': 'Mix amla powder and bhringraj powder in coconut oil. Heat slightly, massage into scalp. Leave overnight.',
        'frequency': '3 times per week',
        'precautions': 'Consistent use for 3-6 months shows results'
    })
                remedies.append({
        'name': 'Curry Leaves & Coconut Oil',
        'benefits': 'Restores natural color, strengthens roots, prevents greying',
        'how_to_use': 'Boil fresh curry leaves in coconut oil until leaves crisp. Strain, cool, massage regularly.',
        'frequency': '2-3 times per week',
        'precautions': 'Use fresh curry leaves for best results'
    })
            remedies.append({
        'name': 'Henna (Mehendi) & Amla Pack',
        'benefits': 'Natural conditioner, covers grey hair, adds shine',
        'how_to_use': 'Mix henna powder with amla powder and water. Apply to hair, leave 2-3 hours, wash.',
        'frequency': 'Once a month',
        'precautions': 'Do patch test first, may cause dryness'
    })

        if 'oily scalp' in concerns_lower or 'excess oil' in concerns_lower:
            remedies.append({
        'name': 'Multani Mitti Hair Pack',
        'benefits': 'Absorbs excess oil, cleanses scalp, removes impurities',
        'how_to_use': 'Mix multani mitti with rose water to make paste. Apply to scalp, leave 20 mins, wash.',
        'frequency': 'Once a week',
        'precautions': 'Don\'t leave on too long as it can dry hair'
    })
            remedies.append({
        'name': 'Lemon & Aloe Vera Rinse',
        'benefits': 'Controls oil production, refreshing, balances pH',
        'how_to_use': 'Mix fresh aloe gel with lemon juice in water. Use as final rinse after shampoo.',
        'frequency': '2 times per week',
        'precautions': 'Don\'t use if scalp has cuts or irritation'
    })

        if 'split ends' in concerns_lower:
            remedies.append({
        'name': 'Coconut Oil & Almond Oil Mix',
        'benefits': 'Seals split ends, nourishes, prevents further damage',
        'how_to_use': 'Mix equal parts coconut and almond oil. Apply only to ends of hair daily.',
        'frequency': 'Daily on ends',
        'precautions': 'Apply only to ends, not scalp'
    })
            remedies.append({
        'name': 'Egg & Olive Oil Mask',
        'benefits': 'Rich in protein, repairs damage, strengthens hair shaft',
        'how_to_use': 'Mix egg with olive oil, apply to hair, focus on ends. Leave 30 mins, wash with cool water.',
        'frequency': 'Once a week',
        'precautions': 'Use cool water to prevent egg from cooking in hair'
    })
        
        return remedies
    
    def _get_natural_tips(self, category, type_key, concerns):
        """Get natural beauty tips"""
        
        tips = []
        
        if category == 'skincare':
            tips = [
                "🌿 Always do a patch test before trying new natural ingredients",
                "💧 Drink warm water with lemon and honey every morning for glowing skin",
                "🌙 Apply raw milk with a cotton ball as a natural cleanser before bed",
                "🍯 Use honey as a spot treatment for acne - its antibacterial properties work wonders",
                "🥒 Keep cucumber slices in the fridge for soothing tired eyes",
                "🌹 Store rose water in spray bottle for refreshing throughout the day",
                "🧴 Apply aloe vera gel daily - it's nature's best moisturizer",
                "🌿 Use neem water (boiled neem leaves) as final rinse for acne-prone skin"
            ]
        else:
            tips = [
                "🥥 Warm coconut oil massage before washing strengthens hair naturally",
                "🌿 Apply amla powder paste once a week for natural shine",
                "💧 Rinse hair with cold water after washing to seal cuticles",
                "🌙 Sleep with braided hair to prevent tangles and breakage",
                "🍳 Eat protein-rich foods like eggs, dal, and nuts for healthy hair",
                "💆‍♀️ Massage scalp with bhringraj oil weekly for hair growth",
                "🚿 Use shikakai and reetha instead of chemical shampoos",
                "🌿 Apply methi seed paste as natural conditioner"
            ]
        
        return tips