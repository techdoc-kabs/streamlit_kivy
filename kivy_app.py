import streamlit as st
st.set_page_config(page_title="MindsReief-Hub", layout="wide")
from db_connection import run_query
import importlib
import base64
import auth
import appointment_page

if "db_pool" not in st.session_state:
    st.session_state.db_pool = None

def set_custom_background(bg_color="skyblue", sidebar_img=None, sidebar_width="200px"):
    page_bg_img = f"""
        <style>
        [data-testid="stAppViewContainer"] > .main {{
            background-color: {bg_color if bg_color else "transparent"};
            background-size: 140%;
            background-position: top left;
            background-repeat: repeat;
            background-attachment: local;
            padding-top: 0px;}}
        /* Reduce sidebar width */
        section[data-testid="stSidebar"] {{
            width: {sidebar_width} !important;
            min-width: {sidebar_width} !important;}}

        [data-testid="stSidebar"] > div:first-child {{
            {"background-image: url('data:image/png;base64," + sidebar_img + "');" if sidebar_img else ""}
            background-position: center; 
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-size: cover;}}

        [data-testid="stHeader"] {{
            background: rgba(0,0,0,0);
            padding-top: 0px;
        }}

        [data-testid="stToolbar"] {{
            right: 2rem;
        }}
        </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


def load_role_module():
        username = st.session_state.user_info.get("username")
        user = run_query(
            "SELECT role, is_active FROM users WHERE username=%s",
            (username,),
            fetch="one")
        if not user:
            st.error(f"User '{username}' not found in database.")
            return

        if user["is_active"] == 0:
            st.warning("🚫 Your account has been deactivated. Please contact admin.")
            for key in ["logged_in", "user_info", "show_login", "admin_redirect"]:
                st.session_state[key] = False if isinstance(st.session_state.get(key), bool) else ""
            return
        st.session_state["user_role"] = user["role"]
        role_modules = {
            "Admin": "admin",
            "Admin2": "super_admin",
            "Therapist": "therapist",
            "Teacher": "teachers_page",
            "Parent": "parents_page",
            "Student": "student_page"}
        module_name = role_modules.get(user["role"])
        if not module_name:
            st.warning(f"No module defined for role: {user['role']}")
            return
        try:
            module = importlib.import_module(module_name)
        except ModuleNotFoundError as mnf:
            st.error(f"Module '{module_name}' not found. Make sure '{module_name}.py' exists.\n{mnf}")
            st.text(traceback.format_exc())
            return
        except Exception as e:
            st.error(f"Unexpected error while importing module '{module_name}': {e}")
            st.text(traceback.format_exc())
            return
        if hasattr(module, "main") and callable(module.main):
            try:
                module.main()
            except Exception as e:
                st.error(f"Error running main() of '{module_name}': {e}")
                st.text(traceback.format_exc())
        else:
            st.error(f"Module '{module_name}' does not have a callable main() function.")




def get_first_name_from_username(username):
    query = "SELECT first_name FROM users WHERE username = %s"
    result = run_query(query, (username,), fetch="one")
    if result and result.get("first_name"):
        return result["first_name"]
    return username

img = get_img_as_base64("images/IMG.webp")

defaults = {
    "page": "login",
    "show_login": False,
    "show_signup": False,
    "logged_in": False,
    "user_name": "",
    "user_role": "",
    "admin_redirect": False,
    "notified": False}

for key, val in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = val

def parse_timestamp(ts):
    if isinstance(ts, str):
        return datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
    return ts

def format_duration(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"


def logout():
    username = st.session_state.get("user_name")
    if username:
        # Fetch user info
        query = "SELECT user_id, role, full_name FROM users WHERE username = %s"
        user = run_query(query, (username,), fetch="one")
        if user:
            user_id = user["user_id"]
            role = user["role"]
            name = user["full_name"]
            ts_query = """
                SELECT timestamp FROM sessions
                WHERE user_id = %s AND event_type = 'login'
                ORDER BY timestamp DESC LIMIT 1
            """
            login_row = run_query(ts_query, (user_id,), fetch="one")
            if login_row:
                login_time = parse_timestamp(login_row["timestamp"])
                logout_time = datetime.now()
                duration_sec = int((logout_time - login_time).total_seconds())
                readable_duration = format_duration(duration_sec)
                insert_session_event(user_id, role, name, "logout", readable_duration)
    for key in ["logged_in", "user_name", "user_role", "show_login", "admin_redirect", "notified", "user_info"]:
        if key in st.session_state:
            del st.session_state[key]
    st.query_params["page"] = "home"
    st.success("👋 Logged out successfully.")
    st.rerun()


# ------------------- SESSION EVENT -------------------
def insert_session_event(user_id, role, name, event_type, session_duration=None):
    query = """
        INSERT INTO sessions (user_id, role, name, event_type, timestamp, session_duration)
        VALUES (%s, %s, %s, %s, CURRENT_TIMESTAMP, %s)
    """
    run_action(query, (user_id, role, name, event_type, session_duration))
# ------------------- FEEDBACK -------------------
def save_feedback(message, name="Anonymous"):
    query = "INSERT INTO feedbacks (name, message) VALUES (%s, %s)"
    run_action(query, (name, message))
# ------------------- APPOINTMENTS -------------------
def save_appointment(name, email, date, appointment_time, reason, tel=""):
    query = """
        INSERT INTO online_appointments (name, email, tel, date, time, reason)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    run_action(query, (name, email, tel, str(date), str(appointment_time), reason))


###### DRIVER CODE ################
def main():
    query_params = st.query_params
    page = query_params.get("page", "home")
    import menu_page
    menu_page.main()
    if st.session_state.get("logged_in") and st.session_state.get("user_info"):
        set_custom_background(bg_color=None, sidebar_img=img, sidebar_width="280px")
        username = st.session_state.user_info["username"]
        first_name = get_first_name_from_username(username)
        st.sidebar.success(f"👋 Welcome, {first_name}")
        user = run_query("SELECT is_active, role FROM users WHERE username=%s", (username,), fetch="one")
        if user and user["is_active"] == 0:
            st.warning("🚫 Your account has been deactivated. Please contact admin.")
            for key in ["logged_in", "user_info", "show_login", "admin_redirect"]:
                st.session_state[key] = False if isinstance(st.session_state.get(key), bool) else ""
            return

    if "page_override" in st.session_state:
        page = st.session_state.pop("page_override")
    else:
        page = st.query_params.get("page", "home")

    import menu_page
    menu_page.main()

    if page == "home":
        import home_page
        home_page.main()
        home_page.static_book_button()  # Floating button

    elif page == "appointment":
        import appointment_page
        appointment_page.appointment_page()

    # --- SIGNIN ---
    elif page == "signin":
        with st.spinner("Loading ..."):
            if st.session_state.get("logged_in"):
                load_role_module()
                with st.sidebar:
                    if st.button("🚪 Logout"):
                        logout()
            else:
                if st.session_state.get("show_login"):
                    auth.show_login_dialog()
                elif st.session_state.get("show_signup"):
                    auth.show_signup_dialog()
                else:
                    st.session_state.show_login = True
                    st.rerun()
        
        if st.button("⬅ Back to Home"):
            st.query_params["page"] = "home"
    # --- HELP ---
    elif page == "help":
        st.write("### ❓ Help Page")
        st.write("This is where help content will appear.")
        if st.button("⬅ Back to Home"):
            st.query_params["page"] = "home"
if __name__ == "__main__":
    main()


