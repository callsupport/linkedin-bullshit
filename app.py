import streamlit as st
import google.generativeai as genai

# 1. Configuration de la page
st.set_page_config(page_title="Le LinkedInator", page_icon="🚀", layout="centered")

# 2. Récupération de la clé API depuis les secrets de Streamlit
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# 3. En-tête de l'application
st.title("🚀 Le Traducteur LinkedIn (BullshItIn)")
st.markdown("**Transformez une phrase banale en un post viral, selon le profil de votre choix.**")

# 4. Choix du Persona
persona_choisi = st.selectbox(
    "Qui voulez-vous incarner ?",
    (
        "🎓 Lucas (L'étudiant en quête de sens)", 
        "🤝 Sophie (La manager bienveillante)", 
        "💎 Jean-Disrupteur (Le CEO visionnaire)"
    )
)

# 5. Zone de texte utilisateur
texte_original = st.text_area("Votre texte normal :", placeholder="Ex: J'ai mangé une pomme ce midi.")

# 6. Bouton d'action (Renommé "Traduire")
if st.button("Traduire"):
    if texte_original:
        with st.spinner("Génération du post en cours... 🧠"):
            
            # Définition du comportement de l'IA selon le persona
            if "Lucas" in persona_choisi:
                style_persona = """
                Tu es Lucas, un jeune étudiant/diplômé. Tu veux prouver ta maturité. 
                Vocabulaire à utiliser : challenge, opportunité, humilité, hâte d'apprendre, reconnaissant. 
                Ton style : Tu transformes le moindre petit événement en une leçon de vie sur ta résilience.
                """
            elif "Sophie" in persona_choisi:
                style_persona = """
                Tu es Sophie, une manager agile, RH ou Scrum Master. Tu adores le télétravail et la santé mentale au travail. 
                Vocabulaire à utiliser : synergie, alignement, feedback, bienveillance, sortir de sa zone de confort. 
                Ton style : Très empathique, tu transformes tout en un moment de co-construction stratégique.
                """
            else:
                style_persona = """
                Tu es Jean-Disrupteur, un CEO insupportable de la Start-up Nation. Tu te lèves à 4h du matin. 
                Vocabulaire à utiliser : mindset, game changer, scale, hustle, ROI, pivoter, out of the box. 
                Ton style : Arrogant mais se voulant inspirant, tu sur-dramatises tout avec du franglais ridicule.
                """

            # Instructions globales pour le formatage LinkedIn
            system_prompt = f"""
            Tu es un générateur de posts LinkedIn (broetry). 
            {style_persona}
            
            Règles de formatage STRICTES :
            1. Commence par une phrase d'accroche très courte et dramatique.
            2. Fais un saut de ligne entre CHAQUE phrase (une phrase = un paragraphe). C'est obligatoire.
            3. Ajoute au moins 4 emojis pertinents.
            4. Termine toujours par une question ouverte pour générer des commentaires.
            """
            
            try:
                # Création du modèle avec les instructions
                model = genai.GenerativeModel(
                    model_name="gemini-1.5-flash",
                    system_instruction=system_prompt
                )
                
                # Génération du post
                reponse = model.generate_content(texte_original)
                
                # Affichage du résultat
                st.success("✅ Votre post est prêt !")
                st.code(reponse.text, language="markdown")
                st.balloons()
                
            except Exception as e:
                st.error(f"Une erreur est survenue : {e}")
    else:
        st.warning("⚠️ Veuillez entrer un texte avant de cliquer sur Traduire.")
