// Phaser Game - Story-Based με Χαρακτήρες
const config = {
    type: Phaser.AUTO,
    width: 1000,
    height: 500,
    parent: 'game-container',
    scene: {
        preload: preload,
        create: create
    },
    backgroundColor: '#1e293b'
};

const game = new Phaser.Game(config);
let currentScene = null;

// Χαρακτήρες ανά level
const levelCharacters = {
    1: [
        { name: 'Κυρία Νιούμπι', color: 0xf87171, text: 'Νιώθω άγχος...', x: 250 },
        { name: 'Σύμβουλος', color: 0x60a5fa, text: 'Μπορείς να το κάνεις!', x: 500 },
        { name: 'Εσύ', color: 0xa78bfa, text: 'Τι να κάνει;', x: 750 }
    ],
    2: [
        { name: 'Μαθητής', color: 0xfbbf24, text: 'Δεν θέλω να συμμετάσχω', x: 250 },
        { name: 'Εκπαιδευτικός', color: 0xf87171, text: 'Δεν ξέρω τι να κάνω!', x: 500 },
        { name: 'Εσύ', color: 0xa78bfa, text: 'Πώς θα αντιδράσεις;', x: 750 }
    ],
    3: [
        { name: 'Παιδί 8 ετών', color: 0xfbbf24, text: 'Δεν καταλαβαίνω...', x: 250 },
        { name: 'Δασκάλα', color: 0x60a5fa, text: 'Πώς να το εξηγήσω;', x: 500 },
        { name: 'Εσύ', color: 0xa78bfa, text: 'Τι μέθοδο;', x: 750 }
    ],
    4: [
        { name: 'Ηλίας', color: 0x60a5fa, text: 'Με πειράζουν...', x: 250 },
        { name: 'Δαριένης', color: 0xef4444, text: 'Δώσε μου τη τσάντα!', x: 500 },
        { name: 'Εσύ', color: 0xa78bfa, text: 'Προσαύλιο — Διάλειμμα', x: 750 }
    ],
    5: [
        { name: 'Νίκος', color: 0xfbbf24, text: 'Ξέχασα την εργασία', x: 250 },
        { name: 'Καθηγητής', color: 0x60a5fa, text: 'Τι να κάνω;', x: 500 },
        { name: 'Εσύ', color: 0xa78bfa, text: 'Ποια στρατηγική;', x: 750 }
    ],
    6: [
        { name: 'Μαθητές', color: 0xef4444, text: 'Χάος!', x: 250 },
        { name: 'Κα Παπαδοπούλου', color: 0x60a5fa, text: 'Τι έκανα λάθος;', x: 500 },
        { name: 'Εσύ', color: 0xa78bfa, text: 'Πώς να φτιάξει την τάξη;', x: 750 }
    ],
    7: [
        { name: 'Μαθητές', color: 0xfbbf24, text: 'Δεν θυμόμαστε τίποτα', x: 250 },
        { name: 'Καθηγητής', color: 0x60a5fa, text: '10 έννοιες σε 1 ώρα!', x: 500 },
        { name: 'Εσύ', color: 0xa78bfa, text: 'Τι πήγε στραβά;', x: 750 }
    ],
    9: [
        { name: 'Σοφία', color: 0x60a5fa, text: 'Έκανα όλη τη δουλειά', x: 250 },
        { name: 'Ομάδα', color: 0xef4444, text: 'Εμείς τίποτα!', x: 500 },
        { name: 'Εσύ', color: 0xa78bfa, text: 'Τι πήγε στραβά;', x: 750 }
    ],
    10: [
        { name: 'Μαρία', color: 0xef4444, text: 'Δεν είμαι για μαθηματικά', x: 250 },
        { name: 'Δάσκαλος', color: 0x60a5fa, text: 'Πώς να την κινητοποιήσω;', x: 500 },
        { name: 'Εσύ', color: 0xa78bfa, text: 'Τι στρατηγική;', x: 750 }
    ]
};

function preload() {}

function create() {
    currentScene = this;
    loadAndSetupLevel(this);
}

async function loadAndSetupLevel(scene) {
    document.getElementById('currentLevel').textContent = `Level ${currentLevel}`;
    
    gameData = await loadLevelData(currentLevel);
    
    if (gameData) {
        document.getElementById('chapterName').textContent = gameData.chapter;
        createStoryScene(scene);
    }
}

function createStoryScene(scene) {
    scene.children.removeAll();
    
    scene.add.text(20, 20, `Level ${currentLevel} — ${gameData.chapter}`, {
        fontSize: '18px',
        color: '#fff',
        backgroundColor: '#4f46e5',
        padding: { x: 12, y: 6 }
    });
    
    const chars = levelCharacters[currentLevel] || levelCharacters[1];
    
    chars.forEach(char => {
        scene.add.rectangle(char.x, 320, 50, 80, char.color);
        scene.add.circle(char.x, 280, 25, 0xffc9a3);
        
        scene.add.text(char.x, 420, char.name, {
            fontSize: '14px',
            color: '#fff',
            backgroundColor: '#000',
            padding: { x: 6, y: 3 }
        }).setOrigin(0.5);
        
        const bubble = scene.add.graphics();
        bubble.fillStyle(0xffffff, 1);
        bubble.fillRoundedRect(char.x - 100, 140, 200, 70, 10);
        bubble.fillTriangle(char.x - 10, 210, char.x + 10, 210, char.x, 225);
        
        scene.add.text(char.x, 175, char.text, {
            fontSize: '13px',
            color: '#000',
            align: 'center',
            wordWrap: { width: 180 }
        }).setOrigin(0.5);
    });
    
    showScenarioPanel();
}

async function loadLevelData(levelId) {
    try {
        const response = await fetch(`${API_URL}/api/level/${levelId}`);
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error loading level:', error);
        return null;
    }
}

async function validateAnswer(levelId, doorIndex) {
    try {
        const response = await fetch(`${API_URL}/api/validate-answer`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ level_id: levelId, door_index: doorIndex })
        });
        return await response.json();
    } catch (error) {
        console.error('Error validating answer:', error);
        return null;
    }
}

function showScenarioPanel() {
    const panel = document.getElementById('scenario-panel');
    document.getElementById('scenarioText').textContent = gameData.scenario;
    
    const doorsContainer = document.getElementById('doorsContainer');
    doorsContainer.innerHTML = '';
    
    gameData.doors.forEach((door, i) => {
        const btn = document.createElement('button');
        btn.className = 'door-btn';
        btn.innerHTML = `
            <div class="door-number">${i + 1}</div>
            <div class="door-text">${door.text}</div>
        `;
        btn.onclick = () => selectDoor(i);
        doorsContainer.appendChild(btn);
    });
    
    panel.classList.remove('hidden');
}

async function selectDoor(doorIndex) {
    const result = await validateAnswer(currentLevel, doorIndex);
    if (result) showFeedback(result);
}

function showFeedback(result) {
    const modal = document.getElementById('feedback-modal');
    const icon = document.getElementById('feedbackIcon');
    const title = document.getElementById('feedbackTitle');
    const text = document.getElementById('feedbackText');
    const btn = document.getElementById('continueBtn');
    
    if (result.correct) {
        totalScore += 10;
        document.getElementById('scoreDisplay').textContent = totalScore;
        
        icon.textContent = '✅';
        icon.className = 'feedback-icon success';
        title.textContent = 'Σωστά!';
        text.textContent = result.feedback;
        btn.textContent = result.next_level ? 'Επόμενο Level →' : '🎉 Ολοκλήρωση!';
        btn.onclick = () => result.next_level ? nextLevel() : showCompletionScreen();
    } else {
        icon.textContent = '❌';
        icon.className = 'feedback-icon error';
        title.textContent = 'Όχι ακριβώς...';
        text.textContent = result.feedback;
        btn.textContent = 'Προσπάθησε Ξανά';
        btn.onclick = () => { hideFeedback(); };
    }
    
    modal.classList.remove('hidden');
}

function hideFeedback() {
    document.getElementById('feedback-modal').classList.add('hidden');
}

function nextLevel() {
    hideFeedback();
    currentLevel++;
    resetLevel();
}

function resetLevel() {
    if (currentScene) {
        currentScene.children.removeAll();
        loadAndSetupLevel(currentScene);
    }
}

function restartFromBeginning() {
    currentLevel = 1;
    resetLevel();
}

function showCompletionScreen() {
    hideFeedback();
    const modal = document.getElementById('feedback-modal');
    modal.querySelector('.modal-content').innerHTML = `
        <div class="completion-screen">
            <div class="feedback-icon success" style="font-size: 80px;">🎓</div>
            <h2>Συγχαρητήρια!</h2>
            <p>Ολοκλήρωσες τα 9 levels!</p>
            <p>Συνολικό Score: ${totalScore} πόντοι</p>
            <div class="completion-actions">
                <button class="btn" onclick="restartGame()">Παίξε Ξανά</button>
                <a href="teacher.html" class="btn btn-secondary">AI Εργαλείο →</a>
            </div>
        </div>
    `;
    modal.classList.remove('hidden');
}

function restartGame() {
    currentLevel = 1;
    totalScore = 0;
    document.getElementById('scoreDisplay').textContent = '0';
    hideFeedback();
    resetLevel();
}
