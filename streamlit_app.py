import streamlit as st
from pathlib import Path

def get_file_content_as_bytes(file_path):
    with open(file_path, "rb") as file:
        return file.read()

# Pfad zur PDF-Datei
file_path = 'Lebenslauf.pdf'

# Lese den Inhalt der PDF-Datei als Bytes
file_bytes = get_file_content_as_bytes(file_path)

left, right =st.columns([3,3], gap="medium")
with left:
        st.image("profile-pic.png", caption=None, width=250,)

with right:
    st.title("Ceylin Hekim", anchor=False)
    st.write("*Die Mathematik ist eine Art Spielzeug, welches die Natur uns zuwarf zum Troste und zur Unterhaltung in der Finsternis.*")
    st.write("keskinceylinnaz@gmail.com")


with right:
    st.download_button(
        label="📄 Download CV",
         data=file_bytes,
        file_name=file_path,
        mime='application/pdf'
    )
  

st.header("IT-Kompetentzen" , anchor=False)
st.markdown("<hr>" , unsafe_allow_html=True)


st.markdown("""
            - Webentwicklung: Fundierte Grundkenntnisse in HTML, CSS und Streamlit (Fullstack-Framework)
            - Programmierung: Praktische Erfahrung in Python, Entwicklung kleiner Anwendungen und Skripte
            - Office-Suite: Versierter Umgang mit Microsoft Word, Excel und PowerPoint
            - Eigene Projekte: Konzeption und Umsetzung verschiedener Projekte inklusive Hosting
            - Schulprojekte: Erstellung datenbasierter Präsentationen und interaktiver Tabellenkalkulationen
            
            """, unsafe_allow_html=True)

st.header("Schulbildung" , anchor=False)
st.markdown("<hr>" , unsafe_allow_html=True)
st.subheader("Fachmittelschule Schaumburgergasse Wien", anchor=False)


st.markdown("""
            - Schwerpunkt: Intensive IT-Spezialisierung, Fokus auf modernen Webtechnologien und Wirtschaft
            - Zeitraum: September 2024 - Juli 2025
            - Derzeitiger Notenschnitt: 1,5
            """, unsafe_allow_html=True)

st.subheader("HTL Rennweg Wien", anchor=False)

st.markdown("""
            - Zeitraum: September 2023 – Juli 2024
            - Abschluss-Notendurchschnitt: 5

            """, unsafe_allow_html=True)

st.subheader("Mittelschule Glassergasse 9 Wien", anchor=False)

st.markdown("""
            - Zeitraum: September 2018 – Juli 2022
            - Abschluss-Notendurchschnitt: 1

            """, unsafe_allow_html=True)

st.subheader("Arbeitserfahrung", anchor=False)
st.markdown("<hr>" , unsafe_allow_html=True)

st.markdown("""
            -  Berufspraktische Tage 1: Bei Apotheke zur Austria von 18. bis 22. Nov. 2024
            -  Berufspraktische Tage 2: Bei UNI-ECK von 24. bis 28. Feb. 2025

            """, unsafe_allow_html=True)

st.subheader("Zusätzliche Qualifikationen", anchor=False)
st.markdown("<hr>" , unsafe_allow_html=True)

st.markdown("""
            -  Schnelle Auffassungsgabe für neue Softwareanwendungen und Technologien
            -  Großes Interesse an der kontinuierlichen Weiterentwicklung im IT-Bereich
            -  Teamfähigkeit und Kommunikationsstärke bei gemeinsamen Coding-Projekten
            """, unsafe_allow_html=True)

st.subheader("Interessen und Hobbys", anchor=False)
st.markdown("<hr>" , unsafe_allow_html=True)

st.markdown("""
            -  Snowboard
            -  Mathe
            -  Zeichnen
            """, unsafe_allow_html=True)


