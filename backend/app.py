from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

# Hugging Face API configuration
HF_API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
HF_TOKEN = os.environ.get('HF_TOKEN', '')

# Game levels data - Educational Psychology chapters
GAME_LEVELS = {
    1: {
        "chapter": "Εισαγωγή στην Εκπαιδευτική Ψυχολογία",
        "scenario": "Η κυρία Νιούμπι αντιμετωπίζει άγχος πριν την πρώτη μέρα. Τι πρέπει να κάνει;",
        "doors": [
            {
                "text": "Να αγνοήσει το άγχος και να προχωρήσει",
                "correct": False,
                "feedback": "Το άγχος είναι φυσιολογικό. Σύμφωνα με το πρότυπο ΑΠΛΑ, χρειάζεται Αναστοχασμός πρώτα."
            },
            {
                "text": "Να εφαρμόσει το πρότυπο ΑΠΛΑ (Αναστοχασμός, Πληροφορίες, Λήψη αποφάσεων, Αξιολόγηση)",
                "correct": True,
                "feedback": "Σωστά! Το ΑΠΛΑ βοηθάει στη συστηματική αντιμετώπιση προβλημάτων."
            },
            {
                "text": "Να ζητήσει να μην διδάξει την πρώτη μέρα",
                "correct": False,
                "feedback": "Η αποφυγή δεν λύνει το πρόβλημα. Χρειάζεται προετοιμασία και στρατηγική."
            }
        ]
    },
    2: {
        "chapter": "Εκπαιδευτικοί και Διδασκαλία",
        "scenario": "Ένας μαθητής αρνείται να συμμετάσχει. Τι κάνετε;",
        "doors": [
            {
                "text": "Τον τιμωρώ αμέσως",
                "correct": False,
                "feedback": "Η τιμωρία χωρίς κατανόηση δεν βοηθάει. Χρειάζεται διερεύνηση των αιτιών."
            },
            {
                "text": "Παρατηρώ ολιστικά, κατανοώ τα κίνητρα, παρέχω στήριξη",
                "correct": True,
                "feedback": "Σωστά! Οι έμπειροι εκπαιδευτικοί βλέπουν την κατάσταση ολιστικά και αντιδρούν με στρατηγική."
            },
            {
                "text": "Τον αγνοώ και συνεχίζω το μάθημα",
                "correct": False,
                "feedback": "Η αγνόηση δεν αντιμετωπίζει το πρόβλημα. Χρειάζεται προσοχή και παρέμβαση."
            }
        ]
    },
    3: {
        "chapter": "Γνωστική Ανάπτυξη",
        "scenario": "Παιδιά 8 ετών δεν καταλαβαίνουν αφηρημένα μαθηματικά. Τι κάνετε;",
        "doors": [
            {
                "text": "Συνεχίζω με αφηρημένες εξηγήσεις",
                "correct": False,
                "feedback": "Σύμφωνα με τον Piaget, τα παιδιά 8 ετών είναι στο στάδιο συγκεκριμένων νοητικών λειτουργιών."
            },
            {
                "text": "Χρησιμοποιώ συγκεκριμένα αντικείμενα και οπτικά παραδείγματα",
                "correct": True,
                "feedback": "Σωστά! Τα παιδιά αυτής της ηλικίας μαθαίνουν καλύτερα με χειραπτικά και οπτικά μέσα."
            },
            {
                "text": "Τους ζητώ να προσπαθήσουν περισσότερο",
                "correct": False,
                "feedback": "Το πρόβλημα δεν είναι η προσπάθεια αλλά η αναπτυξιακή ετοιμότητα."
            }
        ]
    },
    4: {
        "chapter": "Κοινωνική Ανάπτυξη",
        "scenario": "Παρατηρείτε σχολική βία (bullying). Τι κάνετε;",
        "doors": [
            {
                "text": "Αγνοώ το θέμα, δεν είναι δική μου ευθύνη",
                "correct": False,
                "feedback": "Η σχολική βία είναι σοβαρό πρόβλημα που απαιτεί άμεση παρέμβαση από τον εκπαιδευτικό."
            },
            {
                "text": "Παρεμβαίνω αμέσως, ενημερώνω διεύθυνση και γονείς, δημιουργώ ασφαλές περιβάλλον",
                "correct": True,
                "feedback": "Σωστά! Ο εκπαιδευτικός έχει ευθύνη προστασίας και πρέπει να δράσει άμεσα."
            },
            {
                "text": "Περιμένω να το αναφέρει το θύμα",
                "correct": False,
                "feedback": "Τα θύματα συχνά φοβούνται να μιλήσουν. Χρειάζεται προληπτική παρέμβαση."
            }
        ]
    },
    5: {
        "chapter": "Συμπεριφοριστική Θεωρία Μάθησης",
        "scenario": "Μαθητής σπάνια φέρνει εργασίες. Ποια στρατηγική εφαρμόζετε;",
        "doors": [
            {
                "text": "Τον τιμωρώ κάθε φορά που δεν φέρνει",
                "correct": False,
                "feedback": "Η συνεχής αρνητική ενίσχυση μπορεί να μειώσει το κίνητρο. Χρειάζεται θετική προσέγγιση."
            },
            {
                "text": "Τον επαινώ δημοσίως όταν φέρνει (θετική ενίσχυση)",
                "correct": True,
                "feedback": "Σωστά! Σύμφωνα με τον Skinner, η θετική ενίσχυση είναι πιο αποτελεσματική μακροπρόθεσμα."
            },
            {
                "text": "Τον αγνοώ εντελώς",
                "correct": False,
                "feedback": "Η αγνόηση δεν διδάσκει την επιθυμητή συμπεριφορά."
            }
        ]
    },
    6: {
        "chapter": "Διαχείριση της Τάξης",
        "scenario": "Δύσκολη τάξη χωρίς σαφείς κανόνες. Τι κάνετε;",
        "doors": [
            {
                "text": "Συνεχίζω όπως πριν, ελπίζοντας να βελτιωθούν",
                "correct": False,
                "feedback": "Χωρίς δομή και κανόνες, η κατάσταση συνήθως χειροτερεύει."
            },
            {
                "text": "Θεσπίζω σαφείς κανόνες, δημιουργώ δομή, εφαρμόζω συνεπώς τις συνέπειες",
                "correct": True,
                "feedback": "Σωστά! Η διαχείριση τάξης απαιτεί σαφείς προσδοκίες και συνέπεια."
            },
            {
                "text": "Γίνομαι πιο αυστηρός και τιμωρητικός",
                "correct": False,
                "feedback": "Η αυστηρότητα χωρίς δομή δεν φέρνει μακροχρόνια αποτελέσματα."
            }
        ]
    },
    7: {
        "chapter": "Γνωστική Θεωρία Μάθησης",
        "scenario": "Οι μαθητές δεν θυμούνται τίποτα από τις 10 έννοιες που δίδαξες. Τι πήγε στραβά;",
        "doors": [
            {
                "text": "Οι μαθητές δεν προσπάθησαν αρκετά",
                "correct": False,
                "feedback": "Το πρόβλημα είναι το γνωστικό φορτίο, όχι η προσπάθεια."
            },
            {
                "text": "Παρουσίασα πάρα πολλές πληροφορίες - χρειάζεται chunking και απλοποίηση",
                "correct": True,
                "feedback": "Σωστά! Η εργαζόμενη μνήμη έχει περιορισμένη χωρητικότητα. Χρειάζεται βηματική παρουσίαση."
            },
            {
                "text": "Θα επαναλάβω τα ίδια με πιο γρήγορο ρυθμό",
                "correct": False,
                "feedback": "Ο ρυθμός δεν είναι το πρόβλημα αλλά ο όγκος πληροφοριών."
            }
        ]
    },
    8: {
        "chapter": "Εμπλοκή και Συμμετοχή",
        "scenario": "Μαθητής δείχνει απάθεια και βαρεμάρα στο μάθημα. Ποια στρατηγική εφαρμόζετε;",
        "doors": [
            {
                "text": "Τον επιπλήττω για την απάθειά του",
                "correct": False,
                "feedback": "Η επίπληξη δεν αντιμετωπίζει την έλλειψη κινήτρων και μπορεί να επιδεινώσει την κατάσταση."
            },
            {
                "text": "Χρησιμοποιώ ενεργητική μάθηση, συνδέω με ενδιαφέροντα, δίνω επιλογές",
                "correct": True,
                "feedback": "Σωστά! Η ενεργητική συμμετοχή και η σύνδεση με προσωπικά ενδιαφέροντα ενισχύουν την εμπλοκή."
            },
            {
                "text": "Συνεχίζω το μάθημα ελπίζοντας να ενδιαφερθεί",
                "correct": False,
                "feedback": "Η παθητική αναμονή δεν λύνει το πρόβλημα. Χρειάζεται ενεργή παρέμβαση."
            }
        ]
    },
    9: {
        "chapter": "Μάθηση μέσω Συνομηλίκων",
        "scenario": "Σε ομαδικό project, ένας κάνει όλη τη δουλειά. Τι πήγε στραβά;",
        "doors": [
            {
                "text": "Οι άλλοι ήταν τεμπέληδες",
                "correct": False,
                "feedback": "Το πρόβλημα είναι η δομή της συνεργασίας, όχι οι μαθητές."
            },
            {
                "text": "Δεν όρισα σαφείς ρόλους και ατομική ευθύνη για κάθε μέλος",
                "correct": True,
                "feedback": "Σωστά! Η αποτελεσματική ομαδοσυνεργατική μάθηση απαιτεί ατομική λογοδοσία."
            },
            {
                "text": "Η ομαδική εργασία δεν λειτουργεί",
                "correct": False,
                "feedback": "Η ομαδική εργασία λειτουργεί όταν σχεδιάζεται σωστά."
            }
        ]
    },
    10: {
        "chapter": "Κίνητρα και Εμπλοκή",
        "scenario": "Μαθήτρια που αγαπούσε τα μαθηματικά έχει σταματήσει να προσπαθεί. Τι κάνετε;",
        "doors": [
            {
                "text": "Της λέω να προσπαθήσει περισσότερο",
                "correct": False,
                "feedback": "Το πρόβλημα δεν είναι η προσπάθεια αλλά τα κίνητρα και η αυτοπεποίθηση."
            },
            {
                "text": "Ενισχύω την αυτονομία, ικανότητα και σχέσεις της (ενδογενή κίνητρα)",
                "correct": True,
                "feedback": "Σωστά! Η θεωρία αυτοδιάθεσης δείχνει ότι τα ενδογενή κίνητρα είναι κλειδί."
            },
            {
                "text": "Της προσφέρω εξωτερικές ανταμοιβές",
                "correct": False,
                "feedback": "Οι εξωγενείς ανταμοιβές μπορεί να μειώσουν τα ενδογενή κίνητρα μακροπρόθεσμα."
            }
        ]
    }
}

@app.route('/api/levels', methods=['GET'])
def get_levels():
    """Return all game levels"""
    return jsonify(GAME_LEVELS)

@app.route('/api/level/<int:level_id>', methods=['GET'])
def get_level(level_id):
    """Return specific level data"""
    if level_id in GAME_LEVELS:
        return jsonify(GAME_LEVELS[level_id])
    return jsonify({"error": "Level not found"}), 404

@app.route('/api/validate-answer', methods=['POST'])
def validate_answer():
    """Validate player's door choice"""
    data = request.json
    level_id = data.get('level_id')
    door_index = data.get('door_index')
    
    if level_id not in GAME_LEVELS:
        return jsonify({"error": "Invalid level"}), 400
    
    level = GAME_LEVELS[level_id]
    if door_index >= len(level['doors']):
        return jsonify({"error": "Invalid door"}), 400
    
    door = level['doors'][door_index]
    
    return jsonify({
        "correct": door["correct"],
        "feedback": door["feedback"],
        "next_level": level_id + 1 if door["correct"] and level_id < 10 else None
    })

@app.route('/api/teacher-advice', methods=['POST'])
def get_teacher_advice():
    """AI-powered advice for teachers"""
    data = request.json
    problem = data.get('problem', '')
    
    if not problem:
        return jsonify({"error": "No problem provided"}), 400
    
    system_prompt = """Είσαι ειδικός σύμβουλος εκπαιδευτικής ψυχολογίας. 
    Βάσισε τις απαντήσεις σου σε θεωρίες όπως:
    - Θεωρία Γνωστικής Ανάπτυξης (Piaget, Vygotsky)
    - Συμπεριφοριστικές Θεωρίες (Skinner - ενίσχυση)
    - Γνωστικές Θεωρίες (γνωστικό φορτίο, μνήμη)
    - Θεωρίες Κινήτρων (ενδογενή, εξωγενή, αυτοδιάθεση)
    - Διαχείριση Τάξης και Κοινωνική Ανάπτυξη
    
    Δώσε 3-4 συγκεκριμένες, πρακτικές συμβουλές στα ελληνικά.
    Αναφέρε τη θεωρία που στηρίζει κάθε σύσταση."""
    
    try:
        if HF_TOKEN:
            headers = {"Authorization": f"Bearer {HF_TOKEN}"}
            payload = {
                "inputs": f"{system_prompt}\n\nΠρόβλημα: {problem}\n\nΣυμβουλές:",
                "parameters": {
                    "max_new_tokens": 600,
                    "temperature": 0.7,
                    "return_full_text": False
                }
            }
            
            response = requests.post(HF_API_URL, headers=headers, json=payload, timeout=30)
            
            if response.status_code == 200:
                result = response.json()
                if isinstance(result, list) and len(result) > 0:
                    advice = result[0].get('generated_text', '')
                    return jsonify({'success': True, 'advice': advice})
        
        # Fallback advice
        return jsonify({
            'success': True,
            'advice': """Βασικές στρατηγικές:

1. **Κατανόηση Αναπτυξιακού Σταδίου** (Piaget, Vygotsky)
   - Προσάρμοσε τη διδασκαλία στο γνωστικό επίπεδο του μαθητή
   - Χρησιμοποίησε scaffolding για υποστήριξη

2. **Θετική Ενίσχυση** (Skinner)
   - Επαίνεσε συγκεκριμένες προσπάθειες και συμπεριφορές
   - Δημιούργησε σύστημα ανταμοιβών για πρόοδο

3. **Ενίσχυση Ενδογενών Κινήτρων**
   - Προσφέρε επιλογές για αυτονομία
   - Δημιούργησε προκλήσεις στο κατάλληλο επίπεδο δυσκολίας
   - Χτίσε θετικές σχέσεις

4. **Δομημένο Περιβάλλον**
   - Θέσπισε σαφείς κανόνες και προσδοκίες
   - Εφάρμοσε συνεπώς τις συνέπειες
   - Δημιούργησε ασφαλές χώρο μάθησης"""
        })
        
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({
            'success': True,
            'advice': 'Παρουσιάστηκε σφάλμα. Παρακαλώ δοκιμάστε ξανά.'
        }), 200

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)