import streamlit as st
import google.generativeai as genai

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
            try:
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
                
                # LA CORRECTION EST ICI : On force le modèle demandé par Google
                model = genai.GenerativeModel("gemini-3.6-flash")
                reponse = model.generate_content(prompt_complet)
                
                st.success("✅ Succès ! Votre post est prêt.")
                st.code(reponse.text, language="markdown")
                st.balloons()
                
            except Exception as e:
                st.error(f"Une erreur persistante est survenue : {e}")
    else:
        st.warning("⚠️ Veuillez entrer un texte.")
