import streamlit as st
import google.generativeai as genai
import time  # 👈 On ajoute l'outil pour gérer le temps

# 1. Configuration
st.set_page_config(page_title="Le LinkedInator", page_icon="🚀", layout="centered")
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

st.title("🚀 Le Traducteur LinkedIn")
st.markdown("**Transformez une phrase banale en un post viral.**")

# 2. Interface
persona_choisi = st.selectbox(
    "Qui voulez-vous incarner ?",
    ("🎓 Lucas (L'étudiant en quête de sens)", "🤝 Sophie (La manager bienveillante)", "💎 Jean-Disrupteur (Le CEO visionnaire)")
)
texte_original = st.text_area("Votre texte normal :", placeholder="Ex: J'ai mangé une pomme ce midi.")

# 3. Logique
if st.button("Traduire"):
    if texte_original:
        with st.spinner("Génération du post en cours... 🧠"):
            
            # Préparation du style
            if "Lucas" in persona_choisi:
                style = "Tu es Lucas, un étudiant qui surjoue la maturité. Utilise : challenge, opportunité, humilité."
            elif "Sophie" in persona_choisi:
                style = "Tu es Sophie, manager bienveillante. Utilise : synergie, alignement, sortir de sa zone de confort."
            else:
                style = "Tu es Jean-Disrupteur, CEO insupportable. Utilise : mindset, ROI, pivoter, out of the box."

            prompt_complet = f"""
            {style}
            Règles STRICTES:
            1. Phrase d'accroche courte.
            2. Un saut de ligne entre chaque phrase (obligatoire).
            3. 4 emojis minimum.
            4. Finit par une question ouverte.
            
            Texte à transformer : "{texte_original}"
            """
            
            # 🚀 SYSTÈME ANTI-QUOTA : On tente 3 fois maximum
            max_tentatives = 3
            for tentative in range(max_tentatives):
                try:
                    # Utilisation du modèle standard le plus rapide
                    model = genai.GenerativeModel("gemini-1.5-flash")
                    reponse = model.generate_content(prompt_complet)
                    
                    st.success("✅ Succès ! Votre post est prêt.")
                    st.code(reponse.text, language="markdown")
                    st.balloons()
                    break # Si ça marche, on sort de la boucle !
                    
                except Exception as e:
                    erreur = str(e)
                    # Si c'est une erreur de quota (429)
                    if "429" in erreur or "Quota" in erreur:
                        if tentative < max_tentatives - 1:
                            st.warning(f"⏳ Google est un peu surchargé. Nouvelle tentative automatique dans 15 secondes... (Essai {tentative + 1}/{max_tentatives})")
                            time.sleep(15) # On met le code en pause pendant 15 secondes
                        else:
                            st.error("🚨 Le quota est toujours bloqué après plusieurs tentatives. Revenez dans quelques minutes.")
                    else:
                        st.error(f"Une autre erreur est survenue : {e}")
                        break
    else:
        st.warning("⚠️ Veuillez entrer un texte.")
