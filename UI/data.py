diseases = [
    "Apple___Apple_scab", "Apple___Black_rot", "Apple___Cedar_apple_rust", "Apple___healthy",
    "Blueberry___healthy", "Cherry_(including_sour)___Powdery_mildew", "Cherry_(including_sour)___healthy",
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot", "Corn_(maize)___Common_rust_", "Corn_(maize)___Northern_Leaf_Blight",
    "Corn_(maize)___healthy", "Grape___Black_rot", "Grape___Esca_(Black_Measles)", "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
    "Grape___healthy", "Orange___Haunglongbing_(Citrus_greening)", "Peach___Bacterial_spot", "Peach___healthy",
    "Pepper,_bell___Bacterial_spot", "Pepper,_bell___healthy", "Potato___Early_blight", "Potato___Late_blight",
    "Potato___healthy", "Raspberry___healthy", "Soybean___healthy", "Squash___Powdery_mildew", "Strawberry___Leaf_scorch",
    "Strawberry___healthy", "Tomato___Bacterial_spot", "Tomato___Early_blight", "Tomato___Late_blight",
    "Tomato___Leaf_Mold", "Tomato___Septoria_leaf_spot", "Tomato___Spider_mites Two-spotted_spider_mite",
    "Tomato___Target_Spot", "Tomato___Tomato_Yellow_Leaf_Curl_Virus", "Tomato___Tomato_mosaic_virus",
    "Tomato___healthy"
]


treatments = {
        "Apple___Apple_scab": [
            "Remove and destroy infected leaves.",
            "Use resistant apple cultivars.",
            "Apply fungicides at intervals during the growing season.",
            "Promote good air circulation in the tree canopy.",
            "Prune and properly dispose of fallen leaves."
        ],
        "Apple___Black_rot": [
            "Remove mummified fruits and dead limbs.",
            "Apply fungicides starting at petal fall.",
            "Sanitize pruning tools to prevent spread.",
            "Avoid overhead irrigation to reduce humidity.",
            "Harvest fruits promptly to minimize infection."
        ],
        "Apple___Cedar_apple_rust": [
            "Remove galls on cedar trees near orchards.",
            "Apply protective fungicides during spring.",
            "Plant resistant apple varieties.",
            "Maintain good orchard sanitation.",
            "Avoid planting apples near cedar trees."
        ],
        "Apple___healthy": [
            "Maintain regular watering and fertilization schedule.",
            "Monitor periodically for pests and diseases.",
            "Practice good pruning and sanitation.",
            "Ensure proper sunlight exposure.",
            "Keep soil pH balanced."
        ],
        "Blueberry___healthy": [
            "Follow sound cultural practices including mulching.",
            "Maintain soil moisture evenly.",
            "Fertilize carefully to avoid deficiencies.",
            "Protect from common pests via integrated pest management.",
            "Prune properly to enhance airflow."
        ],
        "Cherry_(including_sour)___Powdery_mildew": [
            "Apply sulfur-based fungicides as preventive sprays.",
            "Prune infected twigs and branches.",
            "Increase orchard ventilation.",
            "Avoid excessive nitrogen fertilization.",
            "Remove ground debris to reduce inoculum."
        ],
        "Cherry_(including_sour)___healthy": [
            "Maintain balanced irrigation and fertilization.",
            "Monitor for pests and diseases regularly.",
            "Ensure good airflow by pruning dense branches.",
            "Use mulch to retain soil moisture.",
            "Avoid overhead watering."
        ],
        "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": [
            "Rotate crops to non-host species.",
            "Use resistant corn hybrids.",
            "Apply recommended fungicides early in the season.",
            "Avoid excessive plant density.",
            "Remove crop residues after harvest."
        ],
        "Corn_(maize)___Common_rust_": [
            "Plant resistant varieties when available.",
            "Use fungicides as needed based on monitoring.",
            "Promote good field drainage.",
            "Control grassy weeds which can host rust.",
            "Adjust planting dates to avoid peak inoculum."
        ],
        "Corn_(maize)___Northern_Leaf_Blight": [
            "Use certified disease-free seeds.",
            "Rotate to non-corn crops.",
            "Apply fungicides at early disease stages.",
            "Remove or plow under infected debris.",
            "Manage irrigation to reduce leaf wetness."
        ],
        "Corn_(maize)___healthy": [
            "Maintain proper soil fertility and irrigation.",
            "Conduct regular pest and disease scouting.",
            "Implement recommended planting density.",
            "Use cover crops to improve soil health.",
            "Avoid corn monoculture where possible."
        ],
        "Grape___Black_rot": [
            "Remove and destroy infected leaves and fruit.",
            "Apply fungicides in early growing season.",
            "Prune to increase sunlight penetration.",
            "Sanitize tools between pruning cuts.",
            "Control weeds to reduce humidity."
        ],
        "Grape___Esca_(Black_Measles)": [
            "Remove infected vines promptly.",
            "Avoid excessive nitrogen fertilization.",
            "Improve soil drainage if necessary.",
            "Use protective fungicide treatments.",
            "Maintain vineyard sanitation."
        ],
        "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": [
            "Apply fungicides during wet periods.",
            "Remove fallen leaves to reduce inoculum.",
            "Space vines properly to improve airflow.",
            "Monitor regularly for early symptoms.",
            "Use resistant grape varieties when available."
        ],
        "Grape___healthy": [
            "Implement crop rotation and soil health practices.",
            "Irrigate adequately to avoid stress.",
            "Perform regular disease and pest scouting.",
            "Maintain good vineyard hygiene.",
            "Train vines correctly to promote air circulation."
        ],
        "Orange___Haunglongbing_(Citrus_greening)": [
            "Remove infected trees immediately.",
            "Control psyllid vectors with insecticides.",
            "Use disease-free nursery stock.",
            "Monitor and trap psyllid populations.",
            "Implement good orchard sanitation practices."
        ],
        "Peach___Bacterial_spot": [
            "Apply copper-based bactericides before infection periods.",
            "Remove infected twigs and leaves.",
            "Avoid overhead irrigation during wet periods.",
            "Select resistant peach cultivars.",
            "Practice good orchard sanitation."
        ],
        "Peach___healthy": [
            "Provide adequate water and balanced fertilization.",
            "Conduct regular scouting for pests and diseases.",
            "Prune dead or diseased wood.",
            "Ensure good air circulation through canopy management.",
            "Maintain clean orchard floor."
        ],
        "Pepper,_bell___Bacterial_spot": [
            "Use disease-free seeds or transplants.",
            "Apply copper-based sprays to protect leaves.",
            "Remove and destroy infected plants.",
            "Avoid working in wet fields to reduce spread.",
            "Rotate crops away from peppers."
        ],
        "Pepper,_bell___healthy": [
            "Ensure consistent irrigation and nutrition.",
            "Monitor for pests and diseases on a schedule.",
            "Practice crop rotation.",
            "Use mulch to reduce soil splash.",
            "Maintain good greenhouse or field sanitation."
        ],
        "Potato___Early_blight": [
            "Apply protective fungicides starting early in the season.",
            "Use resistant potato varieties if available.",
            "Remove and destroy infected plant debris.",
            "Avoid overhead irrigation to reduce leaf wetness.",
            "Rotate crops to non-host species."
        ],
        "Potato___Late_blight": [
            "Apply fungicides preventatively during wet weather.",
            "Use certified seed potatoes.",
            "Destroy volunteer potatoes and cull piles.",
            "Remove infected foliage promptly.",
            "Avoid planting potatoes in the same location consecutively."
        ],
        "Potato___healthy": [
            "Practice crop rotation and soil health management.",
            "Monitor regularly for pests and diseases.",
            "Use balanced fertilization and irrigation.",
            "Control weeds and volunteer potatoes.",
            "Maintain good field sanitation."
        ],
        "Raspberry___healthy": [
            "Maintain proper pruning schedules.",
            "Ensure good soil drainage.",
            "Monitor for common pests and diseases.",
            "Fertilize according to soil test recommendations.",
            "Rotate with non-host crops when possible."
        ],
        "Soybean___healthy": [
            "Use high-quality seed and certified disease-free seed.",
            "Rotate crops to reduce pest and disease pressure.",
            "Apply balanced fertilization.",
            "Monitor fields regularly for disease symptoms.",
            "Maintain proper weed control."
        ],
        "Squash___Powdery_mildew": [
            "Apply sulfur-based fungicides at first sign of disease.",
            "Plant resistant squash cultivars.",
            "Ensure adequate plant spacing for airflow.",
            "Water early in the day to allow leaves to dry.",
            "Remove and destroy infected plant parts."
        ],
        "Strawberry___Leaf_scorch": [
            "Remove infected leaves promptly.",
            "Improve air circulation by thinning plants.",
            "Apply fungicides during wet weather.",
            "Avoid overhead irrigation.",
            "Practice crop rotation."
        ],
        "Strawberry___healthy": [
            "Provide balanced fertilization.",
            "Use certified disease-free plants.",
            "Maintain proper irrigation schedules.",
            "Monitor for pests and diseases regularly.",
            "Practice good sanitation in fields."
        ],
        "Tomato___Bacterial_spot": [
            "Use certified, disease-free seeds and transplants.",
            "Apply copper-based bactericides in hot, wet weather.",
            "Remove and destroy infected plants.",
            "Avoid working in wet fields.",
            "Rotate crops and avoid tomato planting consecutively."
        ],
        "Tomato___Early_blight": [
            "Apply fungicides preventatively beginning at flowering.",
            "Use disease-resistant tomato varieties.",
            "Practice effective crop rotation.",
            "Remove plant debris promptly.",
            "Ensure plants have adequate air circulation."
        ],
        "Tomato___Late_blight": [
            "Use certified disease-free seeds or transplants.",
            "Apply fungicides at early disease detection or preventative spray.",
            "Destroy infected plant material after harvest.",
            "Manage irrigation to avoid prolonged leaf wetness.",
            "Rotate crops away from solanaceous plants."
        ],
        "Tomato___Leaf_Mold": [
            "Apply fungicides regularly in high humidity.",
            "Use resistant cultivars if available.",
            "Improve greenhouse ventilation.",
            "Avoid overhead irrigation.",
            "Sanitize greenhouse tools and equipment."
        ],
        "Tomato___Septoria_leaf_spot": [
            "Use fungicides starting at first symptoms.",
            "Practice crop rotation.",
            "Remove infected crop debris.",
            "Space plants for good air circulation.",
            "Use disease-free seeds or transplants."
        ],
        "Tomato___Spider_mites Two-spotted_spider_mite": [
            "Use miticides approved for spider mites.",
            "Encourage natural predators like lady beetles.",
            "Avoid over-fertilizing with nitrogen.",
            "Spray plants with water to physically remove mites.",
            "Monitor regularly and isolate heavily infested plants."
        ],
        "Tomato___Target_Spot": [
            "Apply appropriate fungicides as early preventive measure.",
            "Remove and destroy infected plant material.",
            "Maintain good air circulation around plants.",
            "Avoid overhead watering in the evenings.",
            "Rotate crops yearly."
        ],
        "Tomato___Tomato_Yellow_Leaf_Curl_Virus": [
            "Control whitefly vectors with insecticides or traps.",
            "Remove infected plants promptly.",
            "Use resistant tomato varieties where available.",
            "Practice proper sanitation to remove weeds.",
            "Use reflective mulches to repel whiteflies."
        ],
        "Tomato___Tomato_mosaic_virus": [
            "Use disease-free seeds and transplants.",
            "Sanitize tools and hands after working with infected plants.",
            "Remove infected plants from the field.",
            "Avoid tobacco use near tomato fields.",
            "Implement strict hygiene protocols in greenhouses."
        ],
        "Tomato___healthy": [
            "Maintain balanced fertilization and watering.",
            "Perform regular pest and disease scouting.",
            "Ensure adequate sunlight and airflow.",
            "Practice crop rotation with non-host plants.",
            "Use certified disease-free seeds or transplants."
        ]
    }