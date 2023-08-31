
import streamlit as st
#from streamlit_extras.app_logo import add_logo
import sqlite3
from io import BytesIO


st.set_page_config(page_title="Smartprep",page_icon="https://i.imgur.com/S9k9LNT.png")

# Function to fetch subjects from the database
def fetch_subjects():
    conn = sqlite3.connect("database.db")  # Update with your database name
    cursor = conn.cursor()

    cursor.execute("SELECT subjectname FROM Subjects")
    subjects = cursor.fetchall()
    frame = []
    for i in subjects:
        if i not in frame:
            frame.append(i)

    conn.close()
    return [subject[0] for subject in frame]


# Function to fetch papers by subject from the database
def fetch_papers_by_subject(subject):
    conn = sqlite3.connect("database.db")  # Update with your database name
    cursor = conn.cursor()
    paperid_list = []
    cursor.execute("SELECT subjects,paperid,papername,exam,paperterm FROM Paper")
    info = cursor.fetchall()

    for i in info:
        if subject in i[0]:
            paperid_list.append((i[1],i[2],i[3],i[4]))

    conn.close()
    return [paper for paper in paperid_list]


# Function to fetch questions by paper from the database
def fetch_questions_by_paper(paper, subject):
    conn = sqlite3.connect("database.db")  # Update with your database name
    cursor = conn.cursor()
    full_data = []
    cursor.execute("SELECT questionid, questiontext, questiontype, answer, imageids, marks, compid FROM Question WHERE paperid=? and subject=?", (paper,subject,))
    questions = cursor.fetchall()

    for i in questions:
        options = []
        comprehension = []
        cursor.execute("SELECT optnumber, opttext, answer, imageids FROM Options where questionid=?", (i[0],))
        options = cursor.fetchall()

        if i[6] != 'NONE':
            cursor.execute("SELECT comptext, imageids FROM Comprehension WHERE compid=?", (i[6],))
            comprehension = cursor.fetchall()

        full_data.append((i,options,comprehension))

    conn.close()
    return full_data

def fetch_image_by_id(imageid):
    conn = sqlite3.connect("database.db")  # Update with your database name
    cursor = conn.cursor()
    cursor.execute("SELECT image FROM Image WHERE imageid=?", (imageid,))
    blobdata = cursor.fetchall()

    return blobdata[0][0]

def btn_b_callback():
    st.session_state.display_result = False
    st.session_state.reset = False

def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://i.imgur.com/n1v7QfM.png);
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 20px 20px;

            }
            [data-testid="stSidebarNav"]::before {
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

def main():

    st.title("Saavan Event: Low-Code Showdown")
    # add_logo("https://i.imgur.com/W0NrmI1.png")
    add_logo()

    st.write("We are oraginsing an event this Saavan with the name of Low-Code Showdown, a competitive event for people who are enthusiaistic about coding mainly involving logicla and algorithmic approach and less of coding")
    st.write("\n\nRegister Here: https://saavan.iitmparadox.org/events/technical/35")
    st.subheader("About the Event")

    st.markdown("""
Low-Code Showdow is a event where you will be giving multiple
rounds related to coding and the one holding the maximum total points in
the end will be declared as the winner. 

There will be less about of coding involved and more of your logical and algorithmic approach will be assessed

Our objective is to address that coding is only not about solving the
problem statement, it is also about how you approach the problem, with
minimal time complexity, identifying the errors and through a proper
algorithm.""")

    st.subheader("Non-Coders! Assemble")
    st.markdown("""Are you ready to dive into a world of imagination, creativity, and out-of-the-box thinking? Introducing our one-of-a-kind coding competition that's not about lines of code, but about the boundless power of your ideas!

🌟 **Event Highlights:**

- 🧠 **Innovative Challenges, No Coding Required**: Step away from the intimidating world of programming languages! Our competition is designed for individuals who believe in the magic of ideas. **You won't need to write a single line of code – all you need is your incredible imagination.**
- 🧩 **Engaging Problem-Solving**: Bid farewell to conventional coding competitions! The System Design Challenge is tailored for those who thrive on intellectual exploration. No coding, no design – just your brilliant ideas at play.
- 🏆 **Judging Beyond Code**: We will evaluate your solutions based on creativity, feasibility, time taken and the impact of your ideas. It's not about how well you code; it's about how brilliantly you envision solutions. """)

    st.subheader("Rules and Guidelines")
    st.markdown("""To participate in this event. you must have a laptop with a working camera as we will be monitoring you throughout the quiz which is 2.5hrs.

There are 4 rounds in this event. They are:

- Round 1: **ALGORITHMIC THINKING** -- 1.5hr (Quiz mode) -- 25% Weightage
- Round 2: **LOGICAL THINKING** -- 1hr  (Quiz Mode) -- 20% Weightage
- Round 3: **CODE REVIEWING** -- 30min (Quiz Mode) -- 15% Weightage
- Round 4: **SYSTEM DESIGN SCENARIO** -- 12hr (work at any hour as this is submission round) -- 40% Weightage

After these 4 rounds, according to your final scores, the winner and runner up will be declared.
""")


if __name__ == "__main__":
    main()