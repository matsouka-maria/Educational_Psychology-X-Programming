from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Groq API configuration
GROQ_API_KEY = os.getenv('GROQ_API_KEY', '')
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

# Educational Psychology levels data
LEVELS_DATA = [
    {
        "id": 1,
        "title": "Κεφάλαιο 1: Εισαγωγή στην Εκπαιδευτική Ψυχολογία",
        "scenario": "Ένας νέος δάσκαλος προετοιμάζει το πρώτο του μάθημα. Πώς πρέπει να σχεδιάσει την προσέγγισή του;",
        "doors": [
            {"text": "Απομνημόνευση γεγονότων", "correct": False},
            {"text": "Εφαρμογή του προτύπου ΑΠΛΑ (Αναγνώριση, Παρατήρηση, Λύση, Αξιολόγηση)", "correct": True},
            {"text": "Αυστηρή πειθαρχία από την αρχή", "correct": False}
        ],
        "feedback": {
            "correct": "Σωστά! Το πρότυπο ΑΠΛΑ είναι βασικό εργαλείο για την οργάνωση της διδασκαλίας.",
            "wrong": "Λάθος. Η εκπαιδευτική ψυχολογία προτείνει δομημένη προσέγγιση με το πρότυπο ΑΠΛΑ."
        }
    },
    {
        "id": 2,
        "title": "Κεφάλαιο 2: Ο Ρόλος του Εκπαιδευτικού",
        "scenario": "Πώς μπορεί ένας δάσκαλος να αυξήσει τη διδακτική του αποτελεσματικότητα;",
        "doors": [
            {"text": "Με συνεχή αυτοαξιολόγηση και ανατροφοδότηση", "correct": True},
            {"text": "Με αυστηρότερους κανόνες", "correct": False},
            {"text": "Με περισσότερες εργασίες", "correct": False}
        ],
        "feedback": {
            "correct": "Άριστα! Η συνεχής αυτοβελτίωση είναι κλειδί για την αποτελεσματικότητα.",
            "wrong": "Λάθος. Η έρευνα δείχνει ότι η αυτοαξιολόγηση είναι πιο αποτελεσματική."
        }
    },
    {
        "id": 3,
        "title": "Κεφάλαιο 3: Γνωστική Ανάπτυξη (Piaget)",
        "scenario": "Ένας μαθητής 8 ετών δυσκολεύεται με αφηρημένες έννοιες. Τι προτείνει ο Piaget;",
        "doors": [
            {"text": "Χρήση συγκεκριμένων παραδειγμάτων και χειραπτικών υλικών", "correct": True},
            {"text": "Εντατική μελέτη θεωρίας", "correct": False},
            {"text": "Αναμονή μέχρι να μεγαλώσει", "correct": False}
        ],
        "feedback": {
            "correct": "Σωστά! Σύμφωνα με τον Piaget, τα παιδιά αυτής της ηλικίας βρίσκονται στο στάδιο των συγκεκριμένων πράξεων.",
            "wrong": "Λάθος. Ο Piaget προτείνει προσαρμογή στο γνωστικό στάδιο του παιδιού."
        }
    },
    {
        "id": 4,
        "title": "Κεφάλαιο 4: Κοινωνική Ανάπτυξη",
        "scenario": "Ένας μαθητής υφίσταται bullying. Ποια είναι η καλύτερη παρέμβαση;",
        "doors": [
            {"text": "Αγνόηση του προβλήματος", "correct": False},
            {"text": "Άμεση παρέμβαση και δημιουργία ασφαλούς περιβάλλοντος", "correct": True},
            {"text": "Συμβουλή στο θύμα να αντιμετωπίσει μόνο του την κατάσταση", "correct": False}
        ],
        "feedback": {
            "correct": "Εξαιρετικά! Η άμεση παρέμβαση και η δημιουργία ασφαλούς κλίματος είναι κρίσιμες.",
            "wrong": "Λάθος. Το bullying απαιτεί άμεση και δομημένη παρέμβαση από τον εκπαιδευτικό."
        }
    },
    {
        "id": 5,
        "title": "Κεφάλαιο 5: Συμπεριφοριστική Θεωρία (Skinner)",
        "scenario": "Πώς μπορείτε να ενισχύσετε μια επιθυμητή συμπεριφορά στην τάξη;",
        "doors": [
            {"text": "Με τιμωρία των λαθών", "correct": False},
            {"text": "Με θετική ενίσχυση (επαίνους, ανταμοιβές)", "correct": True},
            {"text": "Με αγνόηση όλων των συμπεριφορών", "correct": False}
        ],
        "feedback": {
            "correct": "Τέλεια! Ο Skinner έδειξε ότι η θετική ενίσχυση είναι πιο αποτελεσματική από την τιμωρία.",
            "wrong": "Λάθος. Η συμπεριφοριστική θεωρία υποστηρίζει τη θετική ενίσχυση."
        }
    },
    {
        "id": 6,
        "title": "Κεφάλαιο 6: Διαχείριση Τάξης",
        "scenario": "Πώς δημιουργείτε ένα αποτελεσματικό περιβάλλον μάθησης;",
        "doors": [
            {"text": "Με ασαφείς κανόνες που αλλάζουν συνέχεια", "correct": False},
            {"text": "Με σαφείς κανόνες, ρουτίνες και δομή", "correct": True},
            {"text": "Χωρίς κανόνες για ελευθερία", "correct": False}
        ],
        "feedback": {
            "correct": "Σωστά! Η σαφής δομή και οι κανόνες δημιουργούν ασφάλεια και προβλεψιμότητα.",
            "wrong": "Λάθος. Η αποτελεσματική διαχείριση τάξης απαιτεί σαφείς κανόνες και δομή."
        }
    },
    {
        "id": 7,
        "title": "Κεφάλαιο 7: Γνωστική Θεωρία Μάθησης",
        "scenario": "Πώς μειώνετε το γνωστικό φορτίο των μαθητών;",
        "doors": [
            {"text": "Δίνοντας όλη την ύλη μαζί", "correct": False},
            {"text": "Χωρίζοντας την πληροφορία σε μικρά κομμάτια (chunking)", "correct": True},
            {"text": "Απαιτώντας απομνημόνευση χωρίς κατανόηση", "correct": False}
        ],
        "feedback": {
            "correct": "Άριστα! Η θεωρία γνωστικού φορτίου προτείνει τη σταδιακή παρουσίαση πληροφοριών.",
            "wrong": "Λάθος. Το υπερβολικό γνωστικό φορτίο εμποδίζει τη μάθηση."
        }
    },
    {
        "id": 8,
        "title": "Κεφάλαιο 8: Μάθηση μέσω Συνομηλίκων",
        "scenario": "Πώς οργανώνετε αποτελεσματική ομαδική εργασία;",
        "doors": [
            {"text": "Αφήνοντας τους μαθητές χωρίς καθοδήγηση", "correct": False},
            {"text": "Με σαφείς ρόλους, στόχους και δομή συνεργασίας", "correct": True},
            {"text": "Δίνοντας βαθμό μόνο στον καλύτερο", "correct": False}
        ],
        "feedback": {
            "correct": "Τέλεια! Η δομημένη συνεργασία με σαφείς ρόλους είναι η πιο αποτελεσματική.",
            "wrong": "Λάθος. Η έρευνα δείχνει ότι η δομημένη συνεργασία φέρνει καλύτερα αποτελέσματα."
        }
    },
    {
        "id": 9,
        "title": "Κεφάλαιο 9: Κίνητρα και Παρακίνηση",
        "scenario": "Πώς αυξάνετε το ενδογενές κίνητρο των μαθητών;",
        "doors": [
            {"text": "Με συνεχείς τιμωρίες", "correct": False},
            {"text": "Με επιλογές, αυτονομία και νόημα στις δραστηριότητες", "correct": True},
            {"text": "Με μόνο εξωτερικές ανταμοιβές (βαθμούς)", "correct": False}
        ],
        "feedback": {
            "correct": "Εξαιρετικά! Η θεωρία αυτοδιάθεσης δείχνει ότι η αυτονομία ενισχύει το ενδογενές κίνητρο.",
            "wrong": "Λάθος. Οι εξωτερικές ανταμοιβές μπορεί να μειώσουν το ενδογενές κίνητρο."
        }
    }
]

def query_groq(user_message, temperature=0.7, max_tokens=800):
    """
    "model": "llama-3.3-70b-versatile",
    """
    if not GROQ_API_KEY:
        logger.warning("GROQ_API_KEY not found - using fallback responses")
        return None
    
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "mixtral-8x7b-32768",
        "messages": [
            {
                "role": "system",
                "content": "Είσαι ειδικός σύμβουλος εκπαιδευτικής ψυχολογίας που παρέχει συγκεκριμένες, πρακτικές συμβουλές βασισμένες σε επιστημονικές θεωρίες. Απαντάς στα ελληνικά με σαφήνεια και δομή."
            },
            {
                "role": "user",
                "content": user_message
            }
        ],
        "temperature": temperature,
        "max_tokens": max_tokens,
        "top_p": 0.9
    }
    
    try:
        logger.info(f"Calling Groq API with message length: {len(user_message)}")
        response = requests.post(GROQ_API_URL, headers=headers, json=payload, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            generated_text = result['choices'][0]['message']['content'].strip()
            logger.info(f"Successfully generated response of length: {len(generated_text)}")
            return generated_text
        else:
            logger.error(f"API Error {response.status_code}: {response.text}")
            return None
            
    except requests.exceptions.Timeout:
        logger.error("Request to Groq API timed out")
        return None
    except Exception as e:
        logger.error(f"Error calling Groq API: {str(e)}")
        return None

def get_fallback_advice(problem):
    """
    Provide basic fallback advice when AI is not available
    """
    fallback_responses = {
        "default": """
        📚 Βασικές Συμβουλές Εκπαιδευτικής Ψυχολογίας:

        1. **Κατανοήστε το Πλαίσιο**: Ποιο είναι το αναπτυξιακό στάδιο του μαθητή; (Piaget)
        
        2. **Δημιουργήστε Ασφαλές Περιβάλλον**: Οι μαθητές μαθαίνουν καλύτερα όταν αισθάνονται ασφαλείς.
        
        3. **Θετική Ενίσχυση**: Επαινέστε την προσπάθεια, όχι μόνο το αποτέλεσμα (Skinner).
        
        4. **Σαφείς Προσδοκίες**: Ορίστε σαφείς κανόνες και ρουτίνες.
        
        5. **Ενδογενή Κίνητρα**: Δώστε επιλογές και αυτονομία στους μαθητές.
        
        ⚠️ Σημείωση: Αυτή είναι μια γενική συμβουλή. Για πιο εξατομικευμένες και λεπτομερείς συμβουλές, 
        παρακαλώ ζητήστε από τον διαχειριστή να ορίσει το Groq API token.
        """
    }
    
    return fallback_responses["default"]

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "ai_enabled": bool(GROQ_API_KEY),
        "message": "AI is enabled (Groq/Mixtral)" if GROQ_API_KEY else "AI is disabled - using fallback responses"
    })

@app.route('/api/levels', methods=['GET'])
def get_levels():
    """Get all levels"""
    return jsonify({
        "success": True,
        "levels": LEVELS_DATA
    })

@app.route('/api/level/<int:level_id>', methods=['GET'])
def get_level(level_id):
    """Get specific level by ID"""
    level = next((l for l in LEVELS_DATA if l['id'] == level_id), None)
    
    if level:
        return jsonify({
            "success": True,
            "level": level
        })
    else:
        return jsonify({
            "success": False,
            "error": "Level not found"
        }), 404

@app.route('/api/validate-answer', methods=['POST'])
def validate_answer():
    """Validate student's answer"""
    data = request.json
    level_id = data.get('level_id')
    door_index = data.get('door_index')
    
    level = next((l for l in LEVELS_DATA if l['id'] == level_id), None)
    
    if not level:
        return jsonify({
            "success": False,
            "error": "Level not found"
        }), 404
    
    if door_index < 0 or door_index >= len(level['doors']):
        return jsonify({
            "success": False,
            "error": "Invalid door index"
        }), 400
    
    is_correct = level['doors'][door_index]['correct']
    feedback = level['feedback']['correct'] if is_correct else level['feedback']['wrong']
    
    return jsonify({
        "success": True,
        "correct": is_correct,
        "feedback": feedback,
        "selected_door": level['doors'][door_index]['text']
    })

@app.route('/api/teacher-advice', methods=['POST'])
def teacher_advice():
    """
    Generate AI-powered advice for teachers based on educational psychology theories
    """
    try:
        data = request.json
        problem = data.get('problem', '').strip()
        
        if not problem:
            return jsonify({
                "success": False,
                "error": "Παρακαλώ περιγράψτε το πρόβλημα"
            }), 400
        
        # Enhanced prompt for better educational psychology advice
        user_message = f"""Ένας εκπαιδευτικός μου παρουσιάζει το εξής πρόβλημα:

"{problem}"

Παρέχε συγκεκριμένες και πρακτικές συμβουλές βασισμένες σε θεωρίες εκπαιδευτικής ψυχολογίας. Στην απάντησή σου:

1. Αναγνώρισε το πρόβλημα και το πλαίσιο
2. Αναφέρσου σε συγκεκριμένες θεωρίες (π.χ. Piaget, Vygotsky, Skinner, Bandura, θεωρία αυτοδιάθεσης)
3. Πρότεινε 3-4 συγκεκριμένες στρατηγικές που μπορεί να εφαρμοστούν άμεσα
4. Εξήγησε γιατί αυτές οι στρατηγικές είναι αποτελεσματικές

Κράτησε την απάντηση σε 300-400 λέξεις και χρησιμοποίησε σαφή δομή."""
        
        # Try to get AI response
        ai_response = query_groq(user_message, temperature=0.8, max_tokens=800)
        
        if ai_response:
            return jsonify({
                "success": True,
                "advice": ai_response,
                "source": "ai",
                "model": "Groq/Mixtral-8x7B"
            })
        else:
            # Use fallback
            fallback = get_fallback_advice(problem)
            return jsonify({
                "success": True,
                "advice": fallback,
                "source": "fallback",
                "message": "Χρησιμοποιήθηκαν βασικές συμβουλές. Για AI-powered συμβουλές, ορίστε το GROQ_API_KEY."
            })
            
    except Exception as e:
        logger.error(f"Error in teacher_advice: {str(e)}")
        return jsonify({
            "success": False,
            "error": "Σφάλμα στην επεξεργασία του αιτήματος"
        }), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
