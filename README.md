# Hi there! I'm Mariana 👋  

**Welcome to my dual-format CV portfolio** – a project that shows both my technical skills *and* my understanding of what hiring teams need.  

---

## 🌟 What You'll Find Here  
I’ve built **two versions of my CV** from the same data source because I know your time is valuable:  
1. **✨ Responsive Web Version** – The "hire me" page I’d want to see as a tech lead – works perfectly on phones, tablets, and desktops.  
2. **📄 PDF Version** – The "print this for the interview panel" version – clean, ATS-friendly, and distraction-free.  

*Why two versions?*  
- **You might** be reviewing candidates on your phone during a commute  
- **Your ATS** might prefer plain text without styles  
- **I want to demonstrate** I can build maintainable systems (one data source, multiple outputs)  

---

## 🖥️ Let’s Get This Running – 2 Minutes Tops!  

### **First, the Responsive CV**  
*(You’ll need Python 3.11+ – most machines have this!)*  

```bash
# 1. Generate the website (I automated this for us!)
python generate_portfolio.py --data portfolio-mariana.json

# 2. Open it right in your browser:  
# On Mac/Linux:
open index.html
# On Windows:  
start index.html
