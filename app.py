import streamlit as st
import google.generativeai as genai

# 1. Configuration
st.set_page_config(page_title="Le LinkedInator", page_icon="🚀", layout="centered")

# Récupération de la clé API depuis le fichier secret
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

st.title("🚀 Le Traducteur LinkedIn (BullshItIn)")
st.markdown("**Générez de l'engagement gratuitement depuis votre salon.**")

intensite = st.slider("Niveau de *Personal Branding*", 1, 3, 2, help="1=Stagiaire | 2=Manager | 3=CEO")
texte_original = st.text_area("Votre texte normal :", placeholder="Ex: J'ai bu un café.")

if st.button("🌟 Disrupter le texte"):
    if texte_original:
        with st.spinner("Alignement des chakras professionnels en cours... 🧠"):
            
            # Instructions pour l'IA
            system_prompt = f"""
            Tu es le meilleur créateur de contenu LinkedIn. Transforme le texte de l'utilisateur en un post LinkedIn extrêmement stéréotypé (broetry).
            Règles :
            - Phrase d'accroche très courte et dramatique.
            - Abus des sauts de ligne (une phrase = un paragraphe).
            - Jargon franglais obligatoire (mindset, focus, KPI, pivot).
            - Au moins 4 emojis.
            - Fausse humilité et fin par une leçon de vie ou question ouverte.
            Niveau d'intensité demandé : {intensite}/3. Si 3, sois totalement caricatural.
            """
            
            try:
                # Création du modèle avec les instructions système
                model = genai.GenerativeModel(
                    model_name="gemini-1.5-flash",
                    system_instruction=system_prompt
                )
                
                # Génération de la réponse
                reponse = model.generate_content(texte_original)
                
                st.success("✅ Prêt pour faire le buzz !")
                st.code(reponse.text, language="markdown")
                st.balloons()
            except Exception as e:
                st.error(f"Une erreur est survenue : {e}")
    else:
        st.warning("⚠️ Veuillez entrer un texte.")
    
