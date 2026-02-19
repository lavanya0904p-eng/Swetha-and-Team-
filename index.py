import streamlit as st

# -----------------------------
# Simple Skill Database
# -----------------------------
career_skills = {
    "Data Scientist": ["python", "machine learning", "statistics", "data analysis"],
    "Web Developer": ["html", "css", "javascript", "react"],
    "Software Engineer": ["python", "java", "c++", "data structures"],
    "AI Engineer": ["python", "deep learning", "machine learning", "tensorflow"]
}

learning_resources = {
    "python": "Practice Python projects and learn advanced concepts.",
    "machine learning": "Study ML algorithms and build small ML models.",
    "data structures": "Practice problems on arrays, linked lists, trees.",
    "html": "Build small web pages using HTML.",
    "javascript": "Create interactive web applications.",
    "deep learning": "Learn neural networks and work on AI projects."
}

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("🎓 VidyaGuide AI Agent")
st.subheader("Career Planning & Resume Mentor")

resume_text = st.text_area("Paste your resume content here:")

if st.button("Analyze Resume"):

    if resume_text.strip() == "":
        st.warning("Please enter resume content.")
    else:
        resume_lower = resume_text.lower()

        detected_skills = []
        for career, skills in career_skills.items():
            for skill in skills:
                if skill in resume_lower:
                    detected_skills.append(skill)

        detected_skills = list(set(detected_skills))

        st.success("Resume Analysis Completed!")

        # Display Skills
        st.write("### ✅ Detected Skills:")
        if detected_skills:
            st.write(detected_skills)
        else:
            st.write("No major skills detected.")

        # Career Recommendation
        st.write("### 🎯 Career Recommendations:")
        recommended_careers = []

        for career, skills in career_skills.items():
            match_count = len(set(detected_skills) & set(skills))
            if match_count >= 2:
                recommended_careers.append(career)

        if recommended_careers:
            st.write(recommended_careers)
        else:
            st.write("Try improving technical skills for better recommendations.")

        # Learning Suggestions
        st.write("### 📚 Learning Guidance:")
        for skill in detected_skills:
            if skill in learning_resources:
                st.write(f"🔹 {skill}: {learning_resources[skill]}")
