import streamlit as st
import random
import datetime

# Custom CSS for background image and text color
st.markdown(
    """
    <style>
    .main {
        background-image: url('https://blog.allgeo.com/wp-content/uploads/2023/08/unnamed-9-scaled-1-1280x750.jpeg');
        background-size: cover;
        padding: 20px;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
    }
    .stTextInput input {
        border-radius: 5px;
    }
    .stSelectbox select {
        background-color: #f0f2f6;
        border-radius: 5px;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #00008B;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    }
    p, label {
        color: purple;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        font-weight: italics;
        font-size: 20px;

    }
    </style>
    """, unsafe_allow_html=True
)


# List of students
if 'people' not in st.session_state:
    st.session_state.people = {
        'AI & ML IV': [
            "UMASHIS PATRA", "AGNIK GHOSH", "PRITHA GUHA MAJUMDAR", "PAULAM DAS", "MRIGANKA PAUL",
            "SUBHRANIL SARKAR", "ARNAB DAS", "ADITYA NARAYAN DALAPATI", "DEBAJYOTI PARUI", "RUDRANIL BASU",
            "SOUMADITYA MUKHERJEE", "SUBHAJIT MALLICK", "ANKAN SHARMA", "ANIRUDHHA PAUL", "JUNAYED ALI KHAN", "KRISHNADUL MAITY",
            "SNEHA DAS", "PIYUSH KUMAR", "SATTWIK BATABYAL", "ATANU KUNDU", "ARIJIT KAR",
            "NILANAJANA PANJA", "DURGAPADA KARAN", "DEBANKUR MALLICK", "JEET DAS", "SOUMYA GAYEN",
            "SOUMALLYA CHANDRA CHANDRA", "DEBAJYOTI PAUL", "ASHIF REZA", "SUBHRADEEP DAS", "SAYAN DE",
            "VIKAS VERMA", "ANANGSHA HALDER", "NISHANT TEWARY", "RISHAV NEOGI", "SAIFUDDIN MOLLAH",
            "ARIJIT ROY", "NEHA MAITY", "ASHMITA DAS", "AYAN PRAMANICK"
        ],
        'CYBER SECURITY IV': [
            "SUJAN HALDAR", "MEHBUB HOSSAIN", "ARNAB GHOSH", "JAGANNATH MONDAL", "ANISH SAHA", "ARKADYUTI SAMANTA", "MD. RISHAD",
            "SHIBAJI MONDAL", "MOHAN NAYEK", "Shreya Jha", "ARIJIT GHOSH", "RAHUL DEV JANA", "ARITRA ADAK", "RAKESH KAYAL",
            "RUPAM HAZRA", "SURJA NARAYAN GOSWAMI", "MOULI DEY", "SABUJ BISWAS", "SAGNIK MONDAL", "ATANU SASMAL", "ARPITA PAUL",
            "NILANJAN JANA", "TUHIN MONDAL", "DISHA HALDER", "TITHI PATTANAYAK", "RAJDEEP MONDAL", "PRABHAT MONDAL",
            "ARPITA MAITY", "AYAN SAMANTA", "SANKET HALDER", "SRIJANI MANDAL", "SUBHAM FADIKAR", "PURBALI DAS",
            "SOUBHIK DAS", "CHAYAN KAYAL", "SAYANTAN PATRA", "NILANJAN DEY", "SAMPA SAHOO", "SATYABRATA GHOSH", "RAHUL DAS",
            "SHREYA KAYAL", "PRITAM DAS", "SUSHOBHAN HALDAR", "SUMAN PRADHAN", "ANIMESH PATRA", "MD TOUFIK CHOWDHURY",
            "SOUMOSISH JANA", "SUHAS HALDER", "SURAJIT SHIT", "AFRIT BAGANI", "TAMALIKA SAR", "AMITAVA GIRI", "ARNAB HALDER",
            "SUSMITA SAU", "ARNAB SARDAR", "SK SOYEB"
        ],
        'DATA SCIENCE IV': [
            "SUDIP SARKAR", "SUMANA SENAPATI", "RAJIB MONDAL", "SOUMIK DAS", "Shuvamoy Pradhan", "ASTIK BHANDARI", "SOMNATH SAMANTA",
            "RAMIJ RAI GAYEN", "ABU RAIHAN", "SAYAN DAS", "SAMYAK GHOSH", "SURAJIT PATRA", "ANKITA BAUL", "SWIKRITI CHANDRA", "SUBHADIP MAITY",
            "TAPAS PAL", "MD SAMIM MALLIK", "RINAB DEY", "RANAJIT HAZRA", "SAYAN PAUL", "RAHUL DHARA", "JIT MANDAL", "SK SUHEL AHAMED", "SOUNAMI MAITY",
            "SOMA PRAMANIK", "KRISHNAGOPAL JAY", "SUKANYA KHAN", "RITAM KOLEY", "SUBHAJIT MAITY", "SOUMYADIP DHARA", "PRANAB SAMANTA", "Jyoti Mondal", "SUDIP MAITY",
            "Sumana Samanta", "SRIZONI MAITY", "BAISHAKHI SING", "BAISHIK PODDAR", "MANAN MAITY", "SK MAMNUR ISLAM", "ADRIJA SINHA", "JAHARLAL BARUI", "SUDIPTA KHAN",
            "Anwesha Das", "TUFAN BERA", "ANIMESH MAHANTY", "DEBRAJ PAUL", "SAPTADEEP HALDER", "ANKITA BERA", "Harsha Guchhait", "HAREKRISHNA ADHIKARY", "SUPRIO ADHIKARI"
        ]
    }

# Simulate database for registered users
registered_users = {}

# Function to generate OTP
def generate_otp():
    return random.randint(100000, 999999)

# Streamlit UI for login page
def login_page():
    st.title('🔐 TNU_ATTENDANCE - Login')

    # Login form
    name = st.text_input('Name')
    email = st.text_input('Email')
    otp = st.text_input('Enter OTP', type='password')

    # Button to generate OTP
    if st.button('📧 Send OTP'):
        otp_value = generate_otp()
        st.session_state.sent_otp = otp_value  # Store OTP in session for feedback
        st.session_state.email = email  # Store email in session
        st.session_state.name = name  # Store name in session
        registered_users[email] = otp_value  # Store OTP for verification
        st.session_state.otp_sent = True  # Flag to indicate OTP was sent

    # Show OTP if it was sent
    if st.session_state.get('otp_sent'):
        st.info(f"OTP sent to {st.session_state.email}: {st.session_state.sent_otp}")

    # Button to log in
    if st.button('🔓 Log In'):
        stored_otp = st.session_state.get('sent_otp')
        stored_email = st.session_state.get('email')
        stored_name = st.session_state.get('name')
        
        if email == stored_email and otp == str(stored_otp):
            st.session_state.logged_in = True
            st.session_state.username = email
            st.session_state.user_name = name
            st.session_state.shortlisted = False
            if 'saved_attendances' not in st.session_state:
                st.session_state.saved_attendances = {}
            st.success(f'Logged in successfully as {name}!')
        else:
            st.error('Invalid email or OTP')

# Streamlit UI for shortlist page
def shortlist_page():
    st.title('📋 TNU_ATT - Shortlist')

    # Short List form
    school = st.selectbox('School', ['NONE', 'SCHOOL OF SCIENCE AND TECHNOLOGY'], key='school')
    department = st.selectbox('Department', ['NONE', 'AI & ML', 'DATA SCIENCE', 'CYBER SECURITY'], key='department')
    semester = st.selectbox('Semester', ['NONE', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII'], key='semester')

    # Add new student
    new_student = st.text_input('Add new student')
    if st.button('➕ Add     student'):
        if new_student:
            key = f'{department} {semester}'
            if key in st.session_state.people:
                st.session_state.people[key].append(new_student)
                st.success(f'Student {new_student} added successfully!')
            else:
                st.error('Invalid department or semester selection.')
    
    # Buttons to reset or proceed
    col1, col2 = st.columns([1, 2])
    if col1.button('🔄 RESET'):
        # Clear specific keys in session state and rerun the app
        del st.session_state['school']
        del st.session_state['department']
        del st.session_state['semester']
        st.rerun()

    key = f'{department} {semester}'
    if key in st.session_state.people:
        st.subheader('📜 List of People')
        if st.button('🗹 Mark All Present'):
            for person in st.session_state.people[key]:
                st.session_state[f"checkbox_{person}"] = True

        for person in st.session_state.people[key]:
            checkbox_key = f"checkbox_{person}"
            st.checkbox(person, key=checkbox_key)
        
        if st.button('💾 SAVE'):
            attendances_to_save = [(person, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) for person in st.session_state.people[key] if st.session_state.get(f"checkbox_{person}")]
            if st.session_state.username not in st.session_state.saved_attendances:
                st.session_state.saved_attendances[st.session_state.username] = []
            st.session_state.saved_attendances[st.session_state.username].append(attendances_to_save)
            st.success('Attendances saved successfully!')

        st.sidebar.button('📂 Saved Attendances', on_click=saved_attendances_page)
        
    # Button to go back to login page
    if st.button('🔙 Logout'):
        st.session_state.logged_in = False
        st.rerun()

# Function to display saved shortlisted candidates
def saved_attendances_page():
    st.title('📂 Saved Attendances')
    username = st.session_state.username
    saved_attendances = st.session_state.saved_attendances.get(username, [])
    if saved_attendances:
        st.write(f"Saved attendances by {username}:")
        for idx, attendance in enumerate(saved_attendances, start=1):
            with st.expander(f"Attendance {idx}"):
                for person, time in attendance:
                    st.write(f"- {person} ({time})")
    else:
        st.write('No attendances saved.')

# Main function to handle page navigation based on login status
def main():
    st.session_state.setdefault('logged_in', False)

    if not st.session_state.logged_in:
        login_page()
    else:
        if 'view_saved_attendances' in st.session_state:
            saved_attendances_page()
        else:
            shortlist_page()

if __name__ == '__main__':
    main()
