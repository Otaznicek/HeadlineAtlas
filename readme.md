# 📰 HeadlineAtlas

**HeadlineAtlas** je interaktivní webová aplikace, která zobrazuje novinové články na mapě podle jejich geografické lokace. Uživatelé mohou vidět hlavní události, přiblížit se na konkrétní články a procházet seznam zpráv v postranním panelu.

---

## 🌟 **Funkce**
✅ **Zobrazení článků na mapě** – Novinové články jsou automaticky umístěny na mapu podle místa, o kterém pojednávají.  
✅ **Interaktivní seznam článků** – Kliknutím na článek v seznamu se mapa přesune na odpovídající lokaci.  
✅ **Přiblížení na článek** – Vedle každého článku je tlačítko **"Přejít na lokaci"**, které vás přesune na odpovídající místo na mapě.  
✅ **Časová značka** – U každého článku je uvedeno, kdy byl přidán do databáze.  
✅ **Moderní UI** – Použití **Bootstrapu**, **Leaflet.js** a **Luxon.js** pro hezký a přehledný vzhled.  

---

## 🛠 **Použité technologie**
### **Backend**
- **Python (Flask)** – Zajišťuje backend aplikace a API.
- **MySQL** – Databáze pro ukládání článků a jejich lokací.
- **Flask-MySQLdb** – Knihovna pro připojení k databázi.
- **WebPilot API** – Používá se k extrakci nadpisů a geografických dat z novinových stránek.

### **Frontend**
- **HTML, CSS (Bootstrap)** – Moderní vzhled a responzivní design.
- **JavaScript (Leaflet.js)** – Dynamická mapa se značkami.
- **Luxon.js** – Formátování časových údajů.

---

## ⚙️ **Instalace a spuštění**

### **1️⃣ Naklonujte repozitář**
```bash
git clone https://github.com/vase-repozitar/headlineatlas.git
cd headlineatlas
