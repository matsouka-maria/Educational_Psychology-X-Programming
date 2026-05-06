# 📤 Πώς να Ανεβάσεις το Project στο GitHub

## ✅ ΒΗΜΑ 1: Δημιούργησε GitHub Account

1. Πήγαινε στο https://github.com
2. Sign Up (αν δεν έχεις ήδη account)
3. Επιβεβαίωσε το email σου

---

## ✅ ΒΗΜΑ 2: Δημιούργησε Repository

1. Μετά το login, κλικ το **"+"** πάνω δεξιά
2. Διάλεξε **"New repository"**
3. Συμπλήρωσε:
   - **Repository name**: `educational-psychology-game`
   - **Description**: "Διαδραστικό game εκπαιδευτικής ψυχολογίας με AI"
   - **Public** ή **Private** (διάλεξε Public αν θες να το δει η καθηγήτρια)
   - **ΜΗΝ** κάνεις check το "Initialize with README"
4. Κλικ **"Create repository"**

---

## ✅ ΒΗΜΑ 3: Ανέβασε τον Κώδικα

### 3.1 Άνοιξε Terminal

```bash
cd ~/Downloads/edu_psych_game_final
```

### 3.2 Initialize Git

```bash
git init
git add .
git commit -m "Initial commit - Educational Psychology Game by Matsouka Maria"
```

### 3.3 Σύνδεσε με GitHub

**ΑΛΛΑΞΕ** το `YOUR_USERNAME` με το δικό σου GitHub username!

```bash
git remote add origin https://github.com/YOUR_USERNAME/educational-psychology-game.git
git branch -M main
git push -u origin main
```

Θα σου ζητήσει:
- **Username**: Το GitHub username σου
- **Password**: ΌΧΙ το password σου! Χρειάζεσαι **Personal Access Token**

### 3.4 Δημιούργησε Personal Access Token

1. Πήγαινε στο GitHub → **Settings** (πάνω δεξιά)
2. Κάτω αριστερά: **Developer settings**
3. **Personal access tokens** → **Tokens (classic)**
4. **Generate new token** → **Generate new token (classic)**
5. **Note**: "Educational Psychology Game"
6. **Expiration**: 90 days (ή custom)
7. **Scopes**: Κάνε check μόνο το **"repo"**
8. **Generate token**
9. **ΑΝΤΙΓΡΑΨΕ** το token (φαίνεται μόνο μια φορά!)

### 3.5 Ξανά-push

```bash
git push -u origin main
```

Όταν ζητήσει password, βάλε το **token** που αντέγραψες!

---

## ✅ ΒΗΜΑ 4: Δες το Project Online

Πήγαινε στο:
```
https://github.com/YOUR_USERNAME/educational-psychology-game
```

**ΤΕΛΟΣ!** Το project σου είναι τώρα στο GitHub! 🎉

---

## 📧 Πώς να το Στείλεις στην Καθηγήτρια

### Τρόπος 1: Link
Στείλε της το link:
```
https://github.com/YOUR_USERNAME/educational-psychology-game
```

### Τρόπος 2: Download ZIP
1. Πήγαινε στο repository σου
2. Κλικ το πράσινο **"Code"** button
3. Κλικ **"Download ZIP"**
4. Στείλε της το ZIP

---

## 🔄 Αν Κάνεις Αλλαγές Αργότερα

```bash
cd ~/Downloads/edu_psych_game_final
git add .
git commit -m "Περιγραφή των αλλαγών"
git push
```

---

## ❓ Troubleshooting

### "Permission denied"
→ Το token έληξε, φτιάξε νέο

### "Repository not found"
→ Έλεγξε το URL, σίγουρα έχει το σωστό username

### "Failed to push"
→ Κάνε πρώτα `git pull origin main` και μετά `git push`

---

**Καλή επιτυχία! 🚀**
