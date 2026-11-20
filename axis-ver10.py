import random
import pickle
from datetime import date

import pandas as pd
import streamlit as st

FILE = "mybookuser.dat"



class User:
    def __init__(self):
        self.name = ""
        self.id = random.randint(1, 10000000)
        self.age = ""
        self.gender = ""
        self.height = ""
        self.weight = ""
        self.email = ""
        self.password = ""
        self.verify = ""
        self.fitness_tests = []

    def create_profile(self):
        print("\n USER CREATION")
        self.name = input("Digit your name: ")
        self.age = input("Digit your age: ")
        while True:
            self.gender = input("Indicate your gender (Male/Female): ")
            if self.gender.upper() in ["MALE", "M", "FEMALE", "F"]:
                print()
                break
            else:
                print("Please enter either Male or Female\n")
        self.height = input("Enter your height: ")
        self.weight = input("Enter your weight: ")
        self.email = input("Digit your email: ")
        while True:
            self.password = input("Create a password: ")
            self.verify = input("Please enter the password again: ")
            if self.password == self.verify:
                break
            else:
                print("The passwords should match")

    def display_users_info(self):
        print("\n USER DATA")
        print("ID: ", self.id)
        print("Name: ", self.name)
        print("Gender: ", self.gender)
        print("Age: ", self.age)
        print("Height: ", self.height, "cm")
        print("Weight: ", self.weight, "kg")
        print("Email: ", self.email)
        print("Total Tests Recorded: ", len(self.fitness_tests))


class FitnessTest:
    def __init__(self):
        self.test_date = ""
        self.push_ups = 0
        self.sit_ups = 0
        self.bench_press_1rm = 0.0
        self.leg_press_1rm = 0.0
        self.sit_and_reach = 0.0
        self.run_distance = 0.0

    def input_scores(self):
        print("FITNESS TEST SCORES")
        self.test_date = input("Enter test date (DD/MM/YYYY): ").strip()
        self.push_ups = int(input("Enter number of push-ups: "))
        self.sit_ups = int(input("Enter number of sit-ups: "))
        self.bench_press_1rm = float(input("Enter bench press 1RM (kg): "))
        self.leg_press_1rm = float(input("Enter leg press 1RM (kg): "))
        self.sit_and_reach = float(input("Enter sit and reach score (cm): "))
        self.run_distance = float(input("Enter 12-min run distance (meters): "))

    def display_test(self):
        print(f"\n  [Fecha: {self.test_date}]")
        print(f"Push-ups: {self.push_ups} | Sit-ups: {self.sit_ups}")
        print(f"Bench Press 1RM: {self.bench_press_1rm} kg | Leg Press 1RM: {self.leg_press_1rm} kg")
        print(f"Sit & Reach: {self.sit_and_reach} cm | Distance: {self.run_distance} m")

def load_users():
    users = []
    try:
        with open(FILE, "rb") as f:
            while True:
                try:
                    users.append(pickle.load(f))
                except EOFError:
                    break
    except FileNotFoundError:
        pass
    return users


def save_users(users):
    with open(FILE, "wb") as f:
        for u in users:
            pickle.dump(u, f)

LEVELS = {1: "Poor", 2: "Below Average", 3: "Average", 4: "Above Average", 5: "Excellent"}

PUSH = {"M": [(52, 40, 23, 18), (46, 35, 22, 17), (30, 22, 17, 12), (25, 17, 13, 10), (21, 13, 10, 7), (18, 11, 8, 5)],
        "F": [(43, 35, 18, 12), (40, 31, 15, 10), (27, 20, 13, 8), (24, 15, 11, 5), (21, 11, 7, 2), (17, 12, 5, 2)]}
SIT = {"M": [(48, 42, 38, 33), (43, 37, 33, 29), (36, 31, 27, 22), (31, 26, 22, 17), (26, 22, 18, 13), (23, 17, 12, 7)],
       "F": [(42, 36, 32, 27), (36, 31, 25, 21), (29, 24, 20, 15), (25, 20, 15, 7), (19, 12, 5, 3), (16, 12, 4, 2)]}
BENCH = {"M": [(1.48, 1.22, 1.06, 0.93), (1.48, 1.22, 1.06, 0.93), (1.24, 1.04, 0.93, 0.83),
               (1.1, 0.93, 0.84, 0.76), (0.97, 0.84, 0.75, 0.68), (0.89, 0.77, 0.68, 0.63)],
         "F": [(0.9, 0.74, 0.65, 0.56), (0.9, 0.74, 0.65, 0.56), (0.76, 0.63, 0.57, 0.51),
               (0.71, 0.57, 0.52, 0.47), (0.61, 0.52, 0.46, 0.42), (0.64, 0.51, 0.45, 0.4)]}
LEG = {"M": [(2.27, 2.05, 1.91, 1.74), (2.27, 2.05, 1.91, 1.74), (2.07, 1.85, 1.71, 1.59),
             (1.92, 1.74, 1.62, 1.51), (1.8, 1.64, 1.52, 1.39), (1.73, 1.56, 1.43, 1.3)],
       "F": [(1.82, 1.58, 1.44, 1.27), (1.82, 1.58, 1.44, 1.27), (1.61, 1.39, 1.27, 1.15),
             (1.48, 1.29, 1.18, 1.08), (1.37, 1.17, 1.05, 0.95), (1.32, 1.13, 0.99, 0.88)]}
FLEX = {"M": [(39, 33, 28, 23), (39, 33, 28, 23), (37, 31, 26, 21), (34, 27, 22, 17), (35, 26, 22, 15), (32, 23, 19, 13)],
        "F": [(40, 35, 31, 26), (40, 35, 31, 26), (39, 34, 30, 25), (37, 32, 28, 23), (37, 30, 27, 23), (34, 28, 25, 21)]}
# VO2 age groups: 20-29, 30-39, 40-49, 50-59, 60-69, 70+
VO2 = {"M": [(56, 51, 46, 42), (54, 48, 44, 41), (53, 46, 42, 38), (49, 43, 39, 35), (45, 39, 35, 32), (43, 36, 32, 29)],
       "F": [(49, 44, 40, 36), (47, 42, 37, 34), (45, 39, 36, 33), (41, 36, 32, 29), (37, 33, 29, 27), (37, 30, 28, 26)]}



def get_group(age, limits):
    i = 0
    while i < len(limits) and age > limits[i]:
        i += 1
    return i


def get_level(value, cutoffs):
    level = 5
    i = 0
    while i < len(cutoffs) and value < cutoffs[i]:
        level -= 1
        i += 1
    return level


def calculation_module(user, test=None):
    test = test or user.fitness_tests[-1]  # last test taken by default
    age = int(user.age)
    weight = float(user.weight)
    sex = "M" if user.gender.upper() in ["MALE", "M"] else "F"
    bench_ratio = test.bench_press_1rm / weight  # relative strength
    leg_ratio = test.leg_press_1rm / weight
    vo2max = (0.022351 * test.run_distance) - 11.3

    g = get_group(age, [19, 29, 39, 49, 59])   # strength / flexibility group
    v = get_group(age, [29, 39, 49, 59, 69])   # VO2 group

    levels = {
        "Push-ups": get_level(test.push_ups, PUSH[sex][g]),
        "Sit-ups": get_level(test.sit_ups, SIT[sex][g]),
        "Bench press": get_level(bench_ratio, BENCH[sex][g]),
        "Leg press": get_level(leg_ratio, LEG[sex][g]),
        "Flexibility": get_level(test.sit_and_reach, FLEX[sex][g]),
        "Cardio (VO2 max)": get_level(vo2max, VO2[sex][v]),
    }
    return {"vo2max": vo2max, "bench_ratio": bench_ratio, "leg_ratio": leg_ratio, "levels": levels}


def weak_areas(levels):
    weak = [a for a, lv in levels.items() if lv <= 2]
    if not weak:
        lowest = min(levels.values())
        weak = [a for a, lv in levels.items() if lv == lowest][:1]
    return weak


def current_user(users):
    email = st.session_state.get("email")
    for u in users:
        if u.email == email:
            return u
    return None


def latest_test_or_stop(user):
    if not user.fitness_tests:
        st.info("No fitness tests yet. Record one in **Record Fitness Test** first.")
        st.stop()
    return user.fitness_tests[-1]

def auth_screen(users):
    login_tab, register_tab = st.tabs(["Log In", "Register New User"])

    with login_tab:
        with st.form("login"):
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            if st.form_submit_button("Log In", type="primary"):
                for u in users:
                    if u.email == email and u.password == password:
                        st.session_state["email"] = u.email
                        st.rerun()
                st.error("Invalid email or password.")

    with register_tab:
        with st.form("register"):
            name = st.text_input("Name")
            c1, c2 = st.columns(2)
            age = c1.number_input("Age", min_value=15, max_value=100, value=18, step=1)
            gender = c2.selectbox("Gender", ["Male", "Female"])
            c3, c4 = st.columns(2)
            height = c3.number_input("Height (cm)", min_value=100.0, max_value=250.0, value=170.0)
            weight = c4.number_input("Weight (kg)", min_value=30.0, max_value=300.0, value=70.0)
            email = st.text_input("Email", key="reg_email")
            password = st.text_input("Password", type="password", key="reg_pw")
            verify = st.text_input("Repeat password", type="password")
            if st.form_submit_button("Register", type="primary"):
                if not name.strip() or not email.strip() or not password:
                    st.error("Name, email and password are required.")
                elif password != verify:
                    st.error("The passwords should match.")
                elif any(u.email == email for u in users):
                    st.error("That email is already registered.")
                else:
                    usr = User()
                    usr.name, usr.age, usr.gender = name.strip(), str(int(age)), gender
                    usr.height, usr.weight = str(height), str(weight)
                    usr.email, usr.password, usr.verify = email.strip(), password, verify
                    users.append(usr)
                    save_users(users)
                    st.success(f"User '{usr.name}' registered and saved! Now log in.")

    st.caption("1 Timothy 4:8 - For physical training is of some value, but godliness has value "
               "for all things, holding promise for both the present life and the life to come.")


def dashboard_page(user):
    st.header(f"Welcome, {user.name}")
    st.subheader("Profile summary")
    c = st.columns(4)
    c[0].metric("Age", user.age)
    c[1].metric("Gender", user.gender)
    c[2].metric("Height", f"{user.height} cm")
    c[3].metric("Weight", f"{user.weight} kg")
    c = st.columns(3)
    c[0].metric("User ID", user.id)
    c[1].metric("Tests recorded", len(user.fitness_tests))
    c[2].metric("Last test", user.fitness_tests[-1].test_date if user.fitness_tests else "-")
    st.caption(f"Email: {user.email}")
    st.info("Use the menu on the left: record a test, see your metrics and assessment, "
            "get a workout plan and track your progress.")


def record_page(user, users):
    st.header("Fitness Test Entry")
    with st.form("record", clear_on_submit=True):
        test_date = st.date_input("Test date", value=date.today(), format="DD/MM/YYYY")
        c1, c2 = st.columns(2)
        push_ups = c1.number_input("1-minute push-ups", min_value=0, step=1)
        sit_ups = c2.number_input("1-minute sit-ups", min_value=0, step=1)
        bench = c1.number_input("Bench press 1RM (kg)", min_value=0.0, step=0.5)
        leg = c2.number_input("Leg press 1RM (kg)", min_value=0.0, step=0.5)
        reach = c1.number_input("Sit and reach (cm)", min_value=-30.0, max_value=80.0, step=0.5)
        run = c2.number_input("12-minute walk/run distance (m)", min_value=0.0, step=10.0)
        if st.form_submit_button("Save Test", type="primary"):
            ft = FitnessTest()
            ft.test_date = test_date.strftime("%d/%m/%Y")
            ft.push_ups, ft.sit_ups = int(push_ups), int(sit_ups)
            ft.bench_press_1rm, ft.leg_press_1rm = float(bench), float(leg)
            ft.sit_and_reach, ft.run_distance = float(reach), float(run)
            user.fitness_tests.append(ft)
            save_users(users)
            st.success(f"Test registered and saved for {user.name}!")


def calculation_page(user):
    st.header("Calculation Module")
    latest_test_or_stop(user)
    r = calculation_module(user)
    st.caption("Your last test converted into standardized metrics.")
    c = st.columns(3)
    c[0].metric("VO2 max (ml/kg/min)", f"{r['vo2max']:.1f}")
    c[1].metric("Bench press / body weight", f"{r['bench_ratio']:.2f}")
    c[2].metric("Leg press / body weight", f"{r['leg_ratio']:.2f}")
    with st.expander("Formulas"):
        st.markdown("- VO2 max = 0.022351 x distance (m) - 11.3\n"
                    "- Relative strength = 1RM (kg) / body weight (kg)")


def assessment_page(user):
    st.header("Personalized Assessment")
    latest_test_or_stop(user)
    levels = calculation_module(user)["levels"]
    st.caption("Your last test compared with age/gender standards.")
    for area, lv in levels.items():
        c1, c2 = st.columns([1, 2])
        c1.markdown(f"**{area}**")
        c2.progress(lv / 5, text=f"{lv}/5 - {LEVELS[lv]}")
    weak = weak_areas(levels)
    st.subheader("Areas to improve")
    for a in weak:
        st.warning(f"{a}: {LEVELS[levels[a]]}")


def workout_recommendations_page(user):
  st.header("💪 Your Personalized Workout Plan")

  test = latest_test_or_stop(user)
  calc = calculation_module(user, test)
  levels = calc["levels"]

  user_plan = RecommendationEngine.get_user_plan(levels)
  weekly_schedule = RecommendationEngine.generate_weekly_schedule(user_plan)

  st.subheader(f"Fitness Assessment Results ({test.test_date})")
  cols = st.columns(3)
  for idx, (metric, info) in enumerate(user_plan.items()):
    cols[idx % 3].metric(metric, f"Level {info['level']}", LEVELS[info["level"]])

  st.divider()

  st.subheader("🎯 Priority Focus Areas")
  focus_areas = [m for m, info in user_plan.items() if info["is_focus"]]

  if focus_areas:
    st.warning("⚠️ **Your Priority Target(s) (Level 1 & 2 Focus):**")
    for m in focus_areas:
      st.write(
          f"• **{m}** (Level {user_plan[m]['level']}):"
          f" {user_plan[m]['exercise']}"
      )
  else:
    st.success(
        "🎉 **High Overall Fitness!** All scores are Level 3 or higher. Focus on"
        " maintaining your current fitness level."
    )

  st.divider()

  st.subheader("📅 Your Customized Weekly Routine")
  for day_name, exercises in weekly_schedule.items():
    st.markdown(f"**{day_name}:**")
    for ex in exercises:
      st.write(f"  - {ex}")

  st.divider()
  st.caption(
      "⚠️ *Safety Note: Always warm up before exercising and stop if you feel"
      " discomfort or pain.*"
  )


def progress_page(user):
    st.header("Progress Tracking")
    tests = user.fitness_tests
    if not tests:
        st.info("No test records found.")
        st.stop()
    rows = [{"Test": f"#{i} {t.test_date}", "Push-ups": t.push_ups, "Sit-ups": t.sit_ups,
             "Bench 1RM (kg)": t.bench_press_1rm, "Leg 1RM (kg)": t.leg_press_1rm,
             "Sit & Reach (cm)": t.sit_and_reach, "Run (m)": t.run_distance}
            for i, t in enumerate(tests, 1)]
    df = pd.DataFrame(rows).set_index("Test")
    if len(tests) >= 2:
        st.subheader("Last test vs previous")
        cols = st.columns(3)
        for i, name in enumerate(df.columns):
            now, before = df[name].iloc[-1], df[name].iloc[-2]
            cols[i % 3].metric(name, f"{now:g}", f"{now - before:+g}")
    else:
        st.caption("Record another test to compare results over time.")
    metric = st.selectbox("Chart", list(df.columns))
    st.line_chart(df[metric])
    st.subheader("All tests")
    st.dataframe(df)


def main():
    st.set_page_config(page_title="AXIS", page_icon="💠")
    st.title("AXIS")
    st.caption("PERSONALIZED FITNESS ANALYSIS")

    users = load_users()
    user = current_user(users)

    if user is None:
        auth_screen(users)
        return

    pages = {
        "Dashboard": lambda: dashboard_page(user),
        "Record Fitness Test": lambda: record_page(user, users),
        "Calculation Module": lambda: calculation_page(user),
        "Personalized Assessment": lambda: assessment_page(user),
        "Workout Recommendation": lambda: workout_page(user),
        "Progress Tracking": lambda: progress_page(user),
    }
    st.sidebar.markdown(f"**{user.name}**")
    choice = st.sidebar.radio("Menu", list(pages))
    if st.sidebar.button("Log Out"):
        st.session_state.pop("email", None)
        st.rerun()
    pages[choice]()


if __name__ == "__main__":
    main()