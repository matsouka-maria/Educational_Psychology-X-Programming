# 🎓 Εκπαιδευτική Ψυχολογία - Runner Game & AI Tool

Μια ολοκληρωμένη web εφαρμογή που συνδυάζει ένα διαδραστικό browser game με εργαλείο τεχνητής νοημοσύνης για εκπαιδευτικούς.

## 📋 Περιγραφή

### 🎮 Browser Game (Phaser.js)
- **9 Levels**: Ένα για κάθε κεφάλαιο εκπαιδευτικής ψυχολογίας
- **Runner Mechanics**: Ο χαρακτήρας τρέχει προς πόρτες με επιλογές
- **Εκπαιδευτικά Διλήμματα**: Κάθε πόρτα αντιπροσωπεύει μια απάντηση
- **Instant Feedback**: Αναφορές σε συγκεκριμένες θεωρίες (Piaget, Skinner, κ.ά.)
- **Progressive Difficulty**: Από βασικές έως προχωρημένες έννοιες

### 🤖 AI Tool για Εκπαιδευτικούς
- **Hugging Face API**: Mistral-7B-Instruct για έξυπνες απαντήσεις
- **Θεωρία-Based Advice**: Συμβουλές βασισμένες σε θεωρίες μάθησης
- **Πρακτικές Στρατηγικές**: Συγκεκριμένες, εφαρμόσιμες λύσεις

## 🛠️ Τεχνολογίες

### Frontend
- HTML5, CSS3, JavaScript
- **Phaser.js 3.70**: Game engine
- Responsive design

### Backend
- **Python 3.11** + **Flask**
- **Flask-CORS** για cross-origin requests
- **Hugging Face API** για AI functionality
- **Gunicorn** για production server

### Deployment
- **Vercel**: Frontend hosting
- **Render**: Backend hosting
- **GitHub**: Version control

## 📂 Δομή Project

```
edu_psych_game/
├── frontend/
│   ├── index.html          # Κύρια σελίδα game
│   ├── teacher.html        # AI tool σελίδα
│   ├── css/
│   │   ├── styles.css      # Κύριο styling
│   │   └── teacher.css     # AI tool styling
│   ├── js/
│   │   └── game.js         # Phaser.js game logic
│   └── assets/             # Images, sounds (προαιρετικό)
├── backend/
│   ├── app.py              # Flask application
│   ├── requirements.txt    # Python dependencies
│   ├── Procfile           # Render deployment
│   └── runtime.txt        # Python version
├── deployment/
│   └── vercel.json        # Vercel configuration
├── .gitignore
└── README.md
```

## 🚀 Local Development

### Backend Setup

1. **Πήγαινε στο backend directory**
   ```bash
   cd backend
   ```

2. **Εγκατάστησε dependencies**
   ```bash
   pip install -r requirements.txt --break-system-packages
   ```

3. **Όρισε το Hugging Face API token (προαιρετικό)**
   
   Για να χρησιμοποιήσεις το AI tool:
   
   ```bash
   export HF_TOKEN="your_huggingface_token_here"
   ```
   
   Ή δημιούργησε `.env`:
   ```
   HF_TOKEN=your_token_here
   ```

4. **Τρέξε το Flask app**
   ```bash
   python app.py
   ```
   
   Backend τρέχει στο: `http://localhost:5000`

### Frontend Setup

1. **Άνοιξε το `frontend/index.html` σε browser**
   
   Ή χρησιμοποίησε ένα local server:
   ```bash
   cd frontend
   python -m http.server 8000
   ```
   
   Frontend στο: `http://localhost:8000`

2. **Ενημέρωσε το API_URL**
   
   Στο `frontend/index.html` και `frontend/teacher.html`:
   ```javascript
   const API_URL = 'http://localhost:5000';
   ```

## 🌐 Deployment στο Production

### 1. Deploy Backend στο Render

1. **Δημιούργησε GitHub repository**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin YOUR_GITHUB_REPO_URL
   git push -u origin main
   ```

2. **Πήγαινε στο [Render](https://render.com)**
   - Sign up / Log in
   - Click "New +" → "Web Service"
   - Connect GitHub repository
   - **Root Directory**: `backend`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`

3. **Όρισε Environment Variables**
   - Πήγαινε στο "Environment"
   - Πρόσθεσε: `HF_TOKEN` = your_huggingface_token

4. **Deploy!**
   - Κάντε click "Create Web Service"
   - Περίμενε το deployment
   - Σημείωσε το URL (π.χ. `https://your-app.onrender.com`)

### 2. Deploy Frontend στο Vercel

1. **Ενημέρωσε API_URL στον κώδικα**
   
   Στο `frontend/index.html` και `frontend/teacher.html`:
   ```javascript
   const API_URL = 'https://your-backend.onrender.com';
   ```

2. **Ενημέρωσε `deployment/vercel.json`**
   ```json
   {
     "rewrites": [
       {
         "source": "/api/(.*)",
         "destination": "https://your-backend.onrender.com/api/$1"
       }
     ]
   }
   ```

3. **Deploy στο Vercel**
   ```bash
   cd frontend
   vercel
   ```
   
   Ή μέσω Vercel Dashboard:
   - Πήγαινε στο [vercel.com](https://vercel.com)
   - "Add New..." → "Project"
   - Import GitHub repository
   - **Root Directory**: `frontend`
   - Deploy!

## 🎮 Πώς Παίζεται

1. **Άνοιξε το game** (`index.html`)
2. **Ο χαρακτήρας τρέχει** αυτόματα προς τις πόρτες
3. **Διάβασε το σενάριο** που εμφανίζεται
4. **Διάλεξε την πόρτα** με τη σωστή απάντηση
5. **Λάβε feedback** βασισμένο σε θεωρίες
6. **Προχώρα στο επόμενο level** ή μάθε από το λάθος!

## 📚 Κεφάλαια / Levels

1. **Εισαγωγή** - Πρότυπο ΑΠΛΑ
2. **Εκπαιδευτικοί** - Διδακτική αποτελεσματικότητα
3. **Γνωστική Ανάπτυξη** - Piaget
4. **Κοινωνική Ανάπτυξη** - Bullying
5. **Συμπεριφοριστική Θεωρία** - Skinner
6. **Διαχείριση Τάξης** - Κανόνες & δομή
7. **Γνωστική Θεωρία** - Γνωστικό φορτίο
9. **Μάθηση μέσω Συνομηλίκων** - Ομαδική εργασία
10. **Κίνητρα** - Ενδογενή vs εξωγενή

## 🤖 AI Tool - Χρήση

1. Πήγαινε στο "AI Εργαλείο"
2. Περίγραψε ένα πρόβλημα με μαθητή
3. Πάτα "Λήψη Συμβουλών AI"
4. Λάβε εξατομικευμένες συμβουλές με αναφορές σε θεωρίες

**Χωρίς HF_TOKEN**: Παίρνεις βασικές fallback συμβουλές  
**Με HF_TOKEN**: Παίρνεις πλήρεις AI-powered συμβουλές

## 🔑 API Endpoints

### GET `/api/levels`
Επιστρέφει όλα τα levels

### GET `/api/level/<id>`
Επιστρέφει συγκεκριμένο level

### POST `/api/validate-answer`
```json
{
  "level_id": 1,
  "door_index": 1
}
```

### POST `/api/teacher-advice`
```json
{
  "problem": "Περιγραφή προβλήματος..."
}
```

## 🎨 Customization

### Προσθήκη Assets

Πρόσθεσε images στο `frontend/assets/sprites/`:
- `player.png` - Χαρακτήρας
- `door1.png`, `door2.png`, `door3.png` - Πόρτες
- `background.png` - Φόντο

Ενημέρωσε το `game.js`:
```javascript
function preload() {
    this.load.image('player', 'assets/sprites/player.png');
    this.load.image('door1', 'assets/sprites/door1.png');
    // ...
}
```

### Αλλαγή Χρωμάτων

Στο `frontend/css/styles.css`:
```css
:root {
    --primary: #yourcolor;
    --secondary: #yourcolor;
}
```

## 🐛 Troubleshooting

### Backend δεν ξεκινάει
- Έλεγξε αν είναι εγκατεστημένες οι dependencies: `pip install -r requirements.txt`
- Έλεγξε το port: Μπορεί να χρησιμοποιείται ήδη

### CORS Errors
- Βεβαιώσου ότι το Flask app έχει `flask-cors` enabled
- Έλεγξε ότι το `API_URL` είναι σωστό

### AI Tool δεν λειτουργεί
- Έλεγξε το `HF_TOKEN`
- Δοκίμασε το API endpoint: `curl http://localhost:5000/health`

### Game δεν φορτώνει
- Άνοιξε Developer Console (F12)
- Έλεγξε για JavaScript errors
- Βεβαιώσου ότι το Phaser.js CDN φορτώνει

## 📊 Testing

### Test Backend
```bash
curl http://localhost:5000/api/levels
curl http://localhost:5000/health
```

### Test AI
```bash
curl -X POST http://localhost:5000/api/teacher-advice \
  -H "Content-Type: application/json" \
  -d '{"problem": "Test problem"}'
```

## 🤝 Contributing

Το project είναι educational. Παρακαλώ:
1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

## 📜 License

MIT License - Free for educational use

## 👥 Credits

- **Maria** - Junior Software engineer
- **Phaser.js** - Game engine
- **Hugging Face** - AI API


---

**🎓DEV BY : MATSOUKA MARIA

