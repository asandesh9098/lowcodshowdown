import streamlit as st

def main():
    st.title("Guidelines")

    st.write("This website allows you to practice for your quizzes and endterm in a easier and smarter way. If you are unable to understand how to use this website, follow the below instructions\n")
    st.write("As you can see in the startpage, we asked you to select for a subject, a paper and mode of exam. \n")
    st.subheader("Subject")
    st.write(" Select the subject which you want to practice. once you change the subject in the dropdown, your previous data might get lost. so please choose wisely the subject you want to practice and once completely done with the subject, move for the next one.")
    st.subheader("Papers")
    st.write("After selecting the subject, Select the paper which you want to practice for your preparation. as you can see, the papers naming is sorted in (TERM) (QUIZ/ENDTERM): (PAPER NAME). here TERM is the term in which the paper is released and QUIZ/ENDTERM represents whether its Quiz1,Quiz2 or endterm. and paper name represents the name of paper which is given by iitm. if you are unaware of paper name, just keep practicing a random paper and move to next one once completed. ")
    st.subheader("Mode of Exam")
    st.write("After selecting both subject and paper, Select the mode of exam you want to attempt.\n If you want to attempt the paper in a practicing fashion without validating your answers, then we suggest you to go for practic emode which allows yout o see answer at any time by clicking the button show answer.\n")
    st.write("If you want to attempt the paper in a exam like fashion where you want ot validate your answers and test yourself how good you are in the particular subject, then w suggest you to go for exam mode. once you finish attempting the paper, click on submit button below so that  the score will be displayed and correct answers and your atempted answers also will be displayed below.")
    st.markdown('----')
    st.write("\n\n\nNOTE: We understand that there are few difficulties in using the website as streamlit has a limited number of fucntions to execute the website in a desired manner. if you feel any or have any suggestions for us to improvise the website then please mail us at 21f1005681@student.onlinedegree.iitm.ac.in. ")
if __name__ == "__main__":
    main()
