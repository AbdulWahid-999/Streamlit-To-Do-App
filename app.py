import streamlit as st 

# Page Configuration
st.set_page_config(page_title="To-Do-List App", page_icon="✅", layout="centered")

# Custom CSS for Modern UI
st.markdown("""
    <style>
        /* Center Title */
        .title {
            font-size: 36px;
            font-weight: bold;
            color: #2E86C1; 
            text-align: center;
            margin-bottom: 20px;
        }

        /* Task Input Box */
        .stTextInput {
            font-size: 18px !important;
            padding: 10px !important;
            border-radius: 8px !important;
            width: 100% !important;
            border: 2px solid #2E86C1 !important;
        }

        /* Buttons */
        .stButton > button {
            font-size: 18px !important;
            padding: 10px 20px !important;
            border-radius: 8px !important;
            background-color: #2E86C1 !important;
            color: white !important;
            border: none !important;
            transition: background 0.3s ease-in-out !important;
        }

        .stButton > button:hover {
            background-color: #21618C !important;
        }

        /* Task List */
        .task {
            font-size: 20px;
            padding: 12px;
            border-radius: 8px;
            background-color: #ffffff;
            margin: 5px 0;
            box-shadow: 4px 4px 15px rgba(0,0,0,0.1);
            transition: transform 0.2s ease-in-out;
        }

        /* Checkbox Label Styling */
        .stCheckbox {
            font-size: 18px !important;
        }

        /* Footer */
        .footer {
            text-align: center;
            color: gray;
            margin-top: 30px;
            font-size: 14px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='title'>📝 To-Do List</div>", unsafe_allow_html=True)

# Initialize task list in session state
if "task_list" not in st.session_state:
    st.session_state.task_list = []

task = st.text_input("Enter Your Task", "")

if st.button("Add Your Task"):
    if task.strip():  # Avoid adding empty tasks
        st.session_state["task_list"].append(task.strip().title())

# Display tasks with checkboxes
for i, t in enumerate(st.session_state["task_list"].copy()):  # Iterate safely
    if st.checkbox(f"{i+1}. {t}", key=f"checkbox_{i}"):
        st.session_state["task_list"].remove(t)
        st.rerun()  # Refresh UI after removing a task

# Clear all tasks button (placed outside loop)
if st.button("Clear All Tasks"):
    st.session_state["task_list"] = []
    st.rerun()  # Refresh UI

# Footer
st.markdown("<div class='footer'>✅ Made with Streamlit</div>", unsafe_allow_html=True)
