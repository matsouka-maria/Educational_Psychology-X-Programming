// Phaser Game - Story-Based με Χαρακτήρες
const config = {
    type: Phaser.AUTO,
    width: 1000,
    height: 300,
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
        { name: 'Κυρία Νιούμπι', color: 0xf87171, text: 'Νιώθω άγχος...', x: 200 },
        { name: 'Σύμβουλος', color: 0x60a5fa, text: 'Μπορείς να το κάνεις!', x: 400 },
        { name: 'Εσύ', color: 0xa78bfa, text: 'Τι να κάνει;', x: 600 }
    ],
    2: [
        { name: 'Μαθητής', color: 0xfbbf24, text: 'Δεν θέλω να συμμετάσχω', x: 200 },
        { name: 'Εκπαιδευτικός', color: 0xf87171, text: 'Δεν ξέρω τι να κάνω!', x: 400 },
        { name: 'Εσύ', color: 0xa78bfa, text: 'Πώς θα αντιδράσεις;', x: 600 }
    ],
    3: [
        { name: 'Παιδί 8 ετών', color: 0xfbbf24, text: 'Δεν καταλαβαίνω...', x: 200 },
        { name: 'Δασκάλα', color: 0x60a5fa, text: 'Πώς να το εξηγήσω;', x: 400 },
        { name: 'Εσύ', color: 0xa78bfa, text: 'Τι μέθοδο;', x: 600 }
    ],
    4: [
        { name: 'Ηλίας', color: 0x60a5fa, text: 'Με πειράζουν...', x: 200 },
        { name: 'Δαριένης', color: 0xef4444, text: 'Δώσε μου τη τσάντα!', x: 400 },
        { name: 'Εσύ', color: 0xa78bfa, text: 'Προσαύλιο — Διάλειμμα', x: 600 }
    ],
    5: [
        { name: 'Νίκος', color: 0xfbbf24, text: 'Ξέχασα την εργασία', x: 200 },
        { name: 'Καθηγητής', color: 0x60a5fa, text: 'Τι να κάνω;', x: 400 },
        { name: 'Εσύ', color: 0xa78bfa, text: 'Ποια στρατηγική;', x: 600 }
    ],
    6: [
        { name: 'Μαθητές', color: 0xef4444, text: 'Χάος!', x: 200 },
        { name: 'Κα Παπαδοπούλου', color: 0x60a5fa, text: 'Τι έκανα λάθος;', x: 400 },
        { name: 'Εσύ', color: 0xa78bfa, text: 'Πώς να φτιάξει την τάξη;', x: 600 }
    ],
    7: [
        { name: 'Μαθητές', color: 0xfbbf24, text: 'Δεν θυμόμαστε τίποτα', x: 200 },
        { name: 'Καθηγητής', color: 0x60a5fa, text: '10 έννοιες σε 1 ώρα!', x: 400 },
        { name: 'Εσύ', color: 0xa78bfa, text: 'Τι πήγε στραβά;', x: 600 }
    ],
    8: [
        { name: 'Μαθητής', color: 0xef4444, text: 'Βαριέμαι...', x: 200 },
        { name: 'Καθηγήτρια', color: 0x60a5fa, text: 'Πώς να τον ενεργοποιήσω;', x: 400 },
        { name: 'Εσύ', color: 0xa78bfa, text: 'Ποια στρατηγική;', x: 600 }
    ],
    9: [
        { name: 'Σοφία', color: 0x60a5fa, text: 'Έκανα όλη τη δουλειά', x: 200 },
        { name: 'Ομάδα', color: 0xef4444, text: 'Εμείς τίποτα!', x: 400 },
        { name: 'Εσύ', color: 0xa78bfa, text: 'Τι πήγε στραβά;', x: 600 }
    ],
    10: [
        { name: 'Μαρία', color: 0xef4444, text: 'Δεν είμαι για μαθηματικά', x: 200 },
        { name: 'Δάσκαλος', color: 0x60a5fa, text: 'Πώς να την κινητοποιήσω;', x: 400 },
        { name: 'Εσύ', color: 0xa78bfa, text: 'Τι στρατηγική;', x: 600 }
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
        fontSize: '16px',
        color: '#fff',
        backgroundColor: '#4f46e5',
        padding: { x: 12, y: 6 }
    });
    const chars = levelCharacters[currentLevel] || levelCharacters[1];
    chars.forEach(char => {
        scene.add.rectangle(char.x, 250, 40, 60, char.color);
        scene.add.circle(char.x, 220, 20, 0xffc9a3);
        scene.add.text(char.x, 320, char.name, {
            fontSize: '13px',
            color: '#fff',
            backgroundColor: '#000',
            padding: { x: 6, y: 3 }
        }).setOrigin(0.5);
        const bubble = scene.add.graphics();
        bubble.fillStyle(0xffffff, 1);
        bubble.fillRoundedRect(char.x - 85, 100, 170, 55, 8);
        bubble.fillTriangle(char.x - 8, 155, char.x + 8, 155, char.x, 165);
        scene.add.text(char.x, 128, char.text, {
            fontSize: '12px',
            color: '#000',
            align: 'center',
            wordWrap: { width: 155 }
        }).setOrigin(0.5);
    });
    setTimeout(() => showScenarioPanel(), 0);
}

function showScenarioPanel() {
    const panel = document.getElementById('scenario-panel');
    document.getElementById('scenarioText').textContent = gameData.scenario;
    const doorsContainer = document.getElementById('doorsContainer');
    doorsContainer.innerHTML = '';
    gameData.doors.forEach((door, i) => {
        const btn = document.createElement('button');
        btn.className = 'door-btn';
        btn.innerHTML = `<div class="door-number">${i + 1}</div><div class="door-text">${door.text}</div>`;
        btn.onclick = () => selectDoor(i);
        doorsContainer.appendChild(btn);
    });
    panel.classList.remove('hidden');
}

function hideScenarioPanel() {
    document.getElementById('scenario-panel').classList.add('hidden');
}

async function selectDoor(doorIndex) {
    hideScenarioPanel();
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
        // ✅ Πρόσθεσε πόντους για σωστή απάντηση
        totalScore += 10;
        updateScoreDisplay();
        
        icon.textContent = '✅';
        icon.className = 'feedback-icon success';
        title.textContent = 'Σωστά! +10 πόντοι';
        text.textContent = result.feedback;
        btn.textContent = result.next_level ? 'Επόμενο Level →' : '🎉 Ολοκλήρωση!';
        btn.onclick = () => result.next_level ? nextLevel() : showCompletionScreen();
    } else {
        // ❌ Αφαίρεση πόντων για λάθος απάντηση
        totalScore -= 5;
        if (totalScore < 0) totalScore = 0;
        updateScoreDisplay();
        
        // Έλεγχος για Game Over
        if (totalScore === 0) {
            showGameOver();
            return;
        }
        
        icon.textContent = '❌';
        icon.className = 'feedback-icon error';
        title.textContent = 'Όχι ακριβώς... -5 πόντοι';
        text.textContent = result.feedback;
        btn.textContent = 'Προσπάθησε Ξανά';
        btn.onclick = () => { hideFeedback(); resetLevel(); };
    }
    modal.classList.remove('hidden');
}

function hideFeedback() {
    document.getElementById('feedback-modal').classList.add('hidden');
}


function updateScoreDisplay() {
    document.getElementById('scoreDisplay').textContent = totalScore;
}

function nextLevel() {
    hideFeedback();
    currentLevel++;
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
            <div class="completion-actions">
                <button class="btn" onclick="restartGame()">Παίξε Ξανά</button>
                <a href="teacher.html" class="btn btn-secondary">AI Εργαλείο →</a>
            </div>
        </div>
    `;
    modal.classList.remove('hidden');

    // Game Over screen όταν φτάσεις στο 0
function showGameOver() {
    hideFeedback();
    const modal = document.getElementById('feedback-modal');
    modal.querySelector('.modal-content').innerHTML = `
        <div class="completion-screen">
            <div class="feedback-icon error" style="font-size: 80px;">💀</div>
            <h2>Game Over!</h2>
            <p>Οι πόντοι σου έφτασαν στο 0!</p>
            <div style="background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%); 
                        color: white; padding: 1.5rem; border-radius: 12px; margin: 1rem 0;">
                <h3 style="margin: 0;">📊 Έφτασες μέχρι</h3>
                <div style="font-size: 2rem; font-weight: bold; margin-top: 0.5rem;">Level ${currentLevel}</div>
            </div>
            <div class="completion-actions">
                <button class="btn" onclick="restartFromBeginning()">🔄 Try Again</button>
                <a href="teacher.html" class="btn btn-secondary">AI Εργαλείο →</a>
            </div>
        </div>
    `;
    modal.classList.remove('hidden');
}
}

function restartGame() {
    currentLevel = 1;
    hideFeedback();
    resetLevel();
}