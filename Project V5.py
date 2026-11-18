import random
import pickle
import tkinter as tk
from tkinter import messagebox


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


myUserList = []
try:
    userFile = open("mybookuser.dat", "rb")
    while True:
        try:
            u_obj = pickle.load(userFile)
            myUserList.append(u_obj)
        except EOFError:
            break
    userFile.close()
    print(f"{len(myUserList)} uploaded from 'mybookuser.dat'.")
except FileNotFoundError:
    print("'mybookuser.dat'not found. New one will be created when saved.")

current_user = None
usr = User()


def calculation_module(current_user):
    test = current_user.fitness_tests[-1]
    age = int(current_user.age)
    weight = float(current_user.weight)
    if current_user.gender.upper() in ["MALE", "M"]:
        sex = "M"
    else:
        sex = "F"
    bench_ratio = test.bench_press_1rm / weight
    leg_ratio = test.leg_press_1rm / weight
    vo2max = (0.022351 * test.run_distance) - 11.3
    if age <= 19:
        age_group = "15-19"
    elif age <= 29:
        age_group = "20-29"
    elif age <= 39:
        age_group = "30-39"
    elif age <= 49:
        age_group = "40-49"
    elif age <= 59:
        age_group = "50-59"
    else:
        age_group = "60+"
    # VO2 max table
    if age <= 29:
        vo2_group = "20-29"
    elif age <= 39:
        vo2_group = "30-39"
    elif age <= 49:
        vo2_group = "40-49"
    elif age <= 59:
        vo2_group = "50-59"
    elif age <= 69:
        vo2_group = "60-69"
    else:
        vo2_group = "70+"

    if sex == "M" and age_group == "15-19":
        if test.push_ups >= 52:
            push_level = 5
        elif test.push_ups >= 40:
            push_level = 4
        elif test.push_ups >= 23:
            push_level = 3
        elif test.push_ups >= 18:
            push_level = 2
        else:
            push_level = 1
    elif sex == "M" and age_group == "20-29":
        if test.push_ups >= 46:
            push_level = 5
        elif test.push_ups >= 35:
            push_level = 4
        elif test.push_ups >= 22:
            push_level = 3
        elif test.push_ups >= 17:
            push_level = 2
        else:
            push_level = 1
    elif sex == "M" and age_group == "30-39":
        if test.push_ups >= 30:
            push_level = 5
        elif test.push_ups >= 22:
            push_level = 4
        elif test.push_ups >= 17:
            push_level = 3
        elif test.push_ups >= 12:
            push_level = 2
        else:
            push_level = 1
    elif sex == "M" and age_group == "40-49":
        if test.push_ups >= 25:
            push_level = 5
        elif test.push_ups >= 17:
            push_level = 4
        elif test.push_ups >= 13:
            push_level = 3
        elif test.push_ups >= 10:
            push_level = 2
        else:
            push_level = 1
    elif sex == "M" and age_group == "50-59":
        if test.push_ups >= 21:
            push_level = 5
        elif test.push_ups >= 13:
            push_level = 4
        elif test.push_ups >= 10:
            push_level = 3
        elif test.push_ups >= 7:
            push_level = 2
        else:
            push_level = 1
    elif sex == "M" and age_group == "60+":
        if test.push_ups >= 18:
            push_level = 5
        elif test.push_ups >= 11:
            push_level = 4
        elif test.push_ups >= 8:
            push_level = 3
        elif test.push_ups >= 5:
            push_level = 2
        else:
            push_level = 1
    elif sex == "F" and age_group == "15-19":
        if test.push_ups >= 43:
            push_level = 5
        elif test.push_ups >= 35:
            push_level = 4
        elif test.push_ups >= 18:
            push_level = 3
        elif test.push_ups >= 12:
            push_level = 2
        else:
            push_level = 1
    elif sex == "F" and age_group == "20-29":
        if test.push_ups >= 40:
            push_level = 5
        elif test.push_ups >= 31:
            push_level = 4
        elif test.push_ups >= 15:
            push_level = 3
        elif test.push_ups >= 10:
            push_level = 2
        else:
            push_level = 1
    elif sex == "F" and age_group == "30-39":
        if test.push_ups >= 27:
            push_level = 5
        elif test.push_ups >= 20:
            push_level = 4
        elif test.push_ups >= 13:
            push_level = 3
        elif test.push_ups >= 8:
            push_level = 2
        else:
            push_level = 1
    elif sex == "F" and age_group == "40-49":
        if test.push_ups >= 24:
            push_level = 5
        elif test.push_ups >= 15:
            push_level = 4
        elif test.push_ups >= 11:
            push_level = 3
        elif test.push_ups >= 5:
            push_level = 2
        else:
            push_level = 1
    elif sex == "F" and age_group == "50-59":
        if test.push_ups >= 21:
            push_level = 5
        elif test.push_ups >= 11:
            push_level = 4
        elif test.push_ups >= 7:
            push_level = 3
        elif test.push_ups >= 2:
            push_level = 2
        else:
            push_level = 1
    elif sex == "F" and age_group == "60+":
        if test.push_ups >= 17:
            push_level = 5
        elif test.push_ups >= 12:
            push_level = 4
        elif test.push_ups >= 5:
            push_level = 3
        elif test.push_ups >= 2:
            push_level = 2
        else:
            push_level = 1

    if sex == "M" and age_group == "15-19":
        if test.sit_ups >= 48:
            sit_level = 5
        elif test.sit_ups >= 42:
            sit_level = 4
        elif test.sit_ups >= 38:
            sit_level = 3
        elif test.sit_ups >= 33:
            sit_level = 2
        else:
            sit_level = 1
    elif sex == "M" and age_group == "20-29":
        if test.sit_ups >= 43:
            sit_level = 5
        elif test.sit_ups >= 37:
            sit_level = 4
        elif test.sit_ups >= 33:
            sit_level = 3
        elif test.sit_ups >= 29:
            sit_level = 2
        else:
            sit_level = 1
    elif sex == "M" and age_group == "30-39":
        if test.sit_ups >= 36:
            sit_level = 5
        elif test.sit_ups >= 31:
            sit_level = 4
        elif test.sit_ups >= 27:
            sit_level = 3
        elif test.sit_ups >= 22:
            sit_level = 2
        else:
            sit_level = 1
    elif sex == "M" and age_group == "40-49":
        if test.sit_ups >= 31:
            sit_level = 5
        elif test.sit_ups >= 26:
            sit_level = 4
        elif test.sit_ups >= 22:
            sit_level = 3
        elif test.sit_ups >= 17:
            sit_level = 2
        else:
            sit_level = 1
    elif sex == "M" and age_group == "50-59":
        if test.sit_ups >= 26:
            sit_level = 5
        elif test.sit_ups >= 22:
            sit_level = 4
        elif test.sit_ups >= 18:
            sit_level = 3
        elif test.sit_ups >= 13:
            sit_level = 2
        else:
            sit_level = 1
    elif sex == "M" and age_group == "60+":
        if test.sit_ups >= 23:
            sit_level = 5
        elif test.sit_ups >= 17:
            sit_level = 4
        elif test.sit_ups >= 12:
            sit_level = 3
        elif test.sit_ups >= 7:
            sit_level = 2
        else:
            sit_level = 1
    elif sex == "F" and age_group == "15-19":
        if test.sit_ups >= 42:
            sit_level = 5
        elif test.sit_ups >= 36:
            sit_level = 4
        elif test.sit_ups >= 32:
            sit_level = 3
        elif test.sit_ups >= 27:
            sit_level = 2
        else:
            sit_level = 1
    elif sex == "F" and age_group == "20-29":
        if test.sit_ups >= 36:
            sit_level = 5
        elif test.sit_ups >= 31:
            sit_level = 4
        elif test.sit_ups >= 25:
            sit_level = 3
        elif test.sit_ups >= 21:
            sit_level = 2
        else:
            sit_level = 1
    elif sex == "F" and age_group == "30-39":
        if test.sit_ups >= 29:
            sit_level = 5
        elif test.sit_ups >= 24:
            sit_level = 4
        elif test.sit_ups >= 20:
            sit_level = 3
        elif test.sit_ups >= 15:
            sit_level = 2
        else:
            sit_level = 1
    elif sex == "F" and age_group == "40-49":
        if test.sit_ups >= 25:
            sit_level = 5
        elif test.sit_ups >= 20:
            sit_level = 4
        elif test.sit_ups >= 15:
            sit_level = 3
        elif test.sit_ups >= 7:
            sit_level = 2
        else:
            sit_level = 1
    elif sex == "F" and age_group == "50-59":
        if test.sit_ups >= 19:
            sit_level = 5
        elif test.sit_ups >= 12:
            sit_level = 4
        elif test.sit_ups >= 5:
            sit_level = 3
        elif test.sit_ups >= 3:
            sit_level = 2
        else:
            sit_level = 1
    elif sex == "F" and age_group == "60+":
        if test.sit_ups >= 16:
            sit_level = 5
        elif test.sit_ups >= 12:
            sit_level = 4
        elif test.sit_ups >= 4:
            sit_level = 3
        elif test.sit_ups >= 2:
            sit_level = 2
        else:
            sit_level = 1

    if sex == "M" and age_group == "15-19":
        if bench_ratio >= 1.48:
            bench_level = 5
        elif bench_ratio >= 1.22:
            bench_level = 4
        elif bench_ratio >= 1.06:
            bench_level = 3
        elif bench_ratio >= 0.93:
            bench_level = 2
        else:
            bench_level = 1
    elif sex == "M" and age_group == "20-29":
        if bench_ratio >= 1.48:
            bench_level = 5
        elif bench_ratio >= 1.22:
            bench_level = 4
        elif bench_ratio >= 1.06:
            bench_level = 3
        elif bench_ratio >= 0.93:
            bench_level = 2
        else:
            bench_level = 1
    elif sex == "M" and age_group == "30-39":
        if bench_ratio >= 1.24:
            bench_level = 5
        elif bench_ratio >= 1.04:
            bench_level = 4
        elif bench_ratio >= 0.93:
            bench_level = 3
        elif bench_ratio >= 0.83:
            bench_level = 2
        else:
            bench_level = 1
    elif sex == "M" and age_group == "40-49":
        if bench_ratio >= 1.1:
            bench_level = 5
        elif bench_ratio >= 0.93:
            bench_level = 4
        elif bench_ratio >= 0.84:
            bench_level = 3
        elif bench_ratio >= 0.76:
            bench_level = 2
        else:
            bench_level = 1
    elif sex == "M" and age_group == "50-59":
        if bench_ratio >= 0.97:
            bench_level = 5
        elif bench_ratio >= 0.84:
            bench_level = 4
        elif bench_ratio >= 0.75:
            bench_level = 3
        elif bench_ratio >= 0.68:
            bench_level = 2
        else:
            bench_level = 1
    elif sex == "M" and age_group == "60+":
        if bench_ratio >= 0.89:
            bench_level = 5
        elif bench_ratio >= 0.77:
            bench_level = 4
        elif bench_ratio >= 0.68:
            bench_level = 3
        elif bench_ratio >= 0.63:
            bench_level = 2
        else:
            bench_level = 1
    elif sex == "F" and age_group == "15-19":
        if bench_ratio >= 0.9:
            bench_level = 5
        elif bench_ratio >= 0.74:
            bench_level = 4
        elif bench_ratio >= 0.65:
            bench_level = 3
        elif bench_ratio >= 0.56:
            bench_level = 2
        else:
            bench_level = 1
    elif sex == "F" and age_group == "20-29":
        if bench_ratio >= 0.9:
            bench_level = 5
        elif bench_ratio >= 0.74:
            bench_level = 4
        elif bench_ratio >= 0.65:
            bench_level = 3
        elif bench_ratio >= 0.56:
            bench_level = 2
        else:
            bench_level = 1
    elif sex == "F" and age_group == "30-39":
        if bench_ratio >= 0.76:
            bench_level = 5
        elif bench_ratio >= 0.63:
            bench_level = 4
        elif bench_ratio >= 0.57:
            bench_level = 3
        elif bench_ratio >= 0.51:
            bench_level = 2
        else:
            bench_level = 1
    elif sex == "F" and age_group == "40-49":
        if bench_ratio >= 0.71:
            bench_level = 5
        elif bench_ratio >= 0.57:
            bench_level = 4
        elif bench_ratio >= 0.52:
            bench_level = 3
        elif bench_ratio >= 0.47:
            bench_level = 2
        else:
            bench_level = 1
    elif sex == "F" and age_group == "50-59":
        if bench_ratio >= 0.61:
            bench_level = 5
        elif bench_ratio >= 0.52:
            bench_level = 4
        elif bench_ratio >= 0.46:
            bench_level = 3
        elif bench_ratio >= 0.42:
            bench_level = 2
        else:
            bench_level = 1
    elif sex == "F" and age_group == "60+":
        if bench_ratio >= 0.64:
            bench_level = 5
        elif bench_ratio >= 0.51:
            bench_level = 4
        elif bench_ratio >= 0.45:
            bench_level = 3
        elif bench_ratio >= 0.4:
            bench_level = 2
        else:
            bench_level = 1

    if sex == "M" and age_group == "15-19":
        if leg_ratio >= 2.27:
            leg_level = 5
        elif leg_ratio >= 2.05:
            leg_level = 4
        elif leg_ratio >= 1.91:
            leg_level = 3
        elif leg_ratio >= 1.74:
            leg_level = 2
        else:
            leg_level = 1
    elif sex == "M" and age_group == "20-29":
        if leg_ratio >= 2.27:
            leg_level = 5
        elif leg_ratio >= 2.05:
            leg_level = 4
        elif leg_ratio >= 1.91:
            leg_level = 3
        elif leg_ratio >= 1.74:
            leg_level = 2
        else:
            leg_level = 1
    elif sex == "M" and age_group == "30-39":
        if leg_ratio >= 2.07:
            leg_level = 5
        elif leg_ratio >= 1.85:
            leg_level = 4
        elif leg_ratio >= 1.71:
            leg_level = 3
        elif leg_ratio >= 1.59:
            leg_level = 2
        else:
            leg_level = 1
    elif sex == "M" and age_group == "40-49":
        if leg_ratio >= 1.92:
            leg_level = 5
        elif leg_ratio >= 1.74:
            leg_level = 4
        elif leg_ratio >= 1.62:
            leg_level = 3
        elif leg_ratio >= 1.51:
            leg_level = 2
        else:
            leg_level = 1
    elif sex == "M" and age_group == "50-59":
        if leg_ratio >= 1.8:
            leg_level = 5
        elif leg_ratio >= 1.64:
            leg_level = 4
        elif leg_ratio >= 1.52:
            leg_level = 3
        elif leg_ratio >= 1.39:
            leg_level = 2
        else:
            leg_level = 1
    elif sex == "M" and age_group == "60+":
        if leg_ratio >= 1.73:
            leg_level = 5
        elif leg_ratio >= 1.56:
            leg_level = 4
        elif leg_ratio >= 1.43:
            leg_level = 3
        elif leg_ratio >= 1.3:
            leg_level = 2
        else:
            leg_level = 1
    elif sex == "F" and age_group == "15-19":
        if leg_ratio >= 1.82:
            leg_level = 5
        elif leg_ratio >= 1.58:
            leg_level = 4
        elif leg_ratio >= 1.44:
            leg_level = 3
        elif leg_ratio >= 1.27:
            leg_level = 2
        else:
            leg_level = 1
    elif sex == "F" and age_group == "20-29":
        if leg_ratio >= 1.82:
            leg_level = 5
        elif leg_ratio >= 1.58:
            leg_level = 4
        elif leg_ratio >= 1.44:
            leg_level = 3
        elif leg_ratio >= 1.27:
            leg_level = 2
        else:
            leg_level = 1
    elif sex == "F" and age_group == "30-39":
        if leg_ratio >= 1.61:
            leg_level = 5
        elif leg_ratio >= 1.39:
            leg_level = 4
        elif leg_ratio >= 1.27:
            leg_level = 3
        elif leg_ratio >= 1.15:
            leg_level = 2
        else:
            leg_level = 1
    elif sex == "F" and age_group == "40-49":
        if leg_ratio >= 1.48:
            leg_level = 5
        elif leg_ratio >= 1.29:
            leg_level = 4
        elif leg_ratio >= 1.18:
            leg_level = 3
        elif leg_ratio >= 1.08:
            leg_level = 2
        else:
            leg_level = 1
    elif sex == "F" and age_group == "50-59":
        if leg_ratio >= 1.37:
            leg_level = 5
        elif leg_ratio >= 1.17:
            leg_level = 4
        elif leg_ratio >= 1.05:
            leg_level = 3
        elif leg_ratio >= 0.95:
            leg_level = 2
        else:
            leg_level = 1
    elif sex == "F" and age_group == "60+":
        if leg_ratio >= 1.32:
            leg_level = 5
        elif leg_ratio >= 1.13:
            leg_level = 4
        elif leg_ratio >= 0.99:
            leg_level = 3
        elif leg_ratio >= 0.88:
            leg_level = 2
        else:
            leg_level = 1

    if sex == "M" and age_group == "15-19":
        if test.sit_and_reach >= 39:
            flex_level = 5
        elif test.sit_and_reach >= 33:
            flex_level = 4
        elif test.sit_and_reach >= 28:
            flex_level = 3
        elif test.sit_and_reach >= 23:
            flex_level = 2
        else:
            flex_level = 1
    elif sex == "M" and age_group == "20-29":
        if test.sit_and_reach >= 39:
            flex_level = 5
        elif test.sit_and_reach >= 33:
            flex_level = 4
        elif test.sit_and_reach >= 28:
            flex_level = 3
        elif test.sit_and_reach >= 23:
            flex_level = 2
        else:
            flex_level = 1
    elif sex == "M" and age_group == "30-39":
        if test.sit_and_reach >= 37:
            flex_level = 5
        elif test.sit_and_reach >= 31:
            flex_level = 4
        elif test.sit_and_reach >= 26:
            flex_level = 3
        elif test.sit_and_reach >= 21:
            flex_level = 2
        else:
            flex_level = 1
    elif sex == "M" and age_group == "40-49":
        if test.sit_and_reach >= 34:
            flex_level = 5
        elif test.sit_and_reach >= 27:
            flex_level = 4
        elif test.sit_and_reach >= 22:
            flex_level = 3
        elif test.sit_and_reach >= 17:
            flex_level = 2
        else:
            flex_level = 1
    elif sex == "M" and age_group == "50-59":
        if test.sit_and_reach >= 35:
            flex_level = 5
        elif test.sit_and_reach >= 26:
            flex_level = 4
        elif test.sit_and_reach >= 22:
            flex_level = 3
        elif test.sit_and_reach >= 15:
            flex_level = 2
        else:
            flex_level = 1
    elif sex == "M" and age_group == "60+":
        if test.sit_and_reach >= 32:
            flex_level = 5
        elif test.sit_and_reach >= 23:
            flex_level = 4
        elif test.sit_and_reach >= 19:
            flex_level = 3
        elif test.sit_and_reach >= 13:
            flex_level = 2
        else:
            flex_level = 1
    elif sex == "F" and age_group == "15-19":
        if test.sit_and_reach >= 40:
            flex_level = 5
        elif test.sit_and_reach >= 35:
            flex_level = 4
        elif test.sit_and_reach >= 31:
            flex_level = 3
        elif test.sit_and_reach >= 26:
            flex_level = 2
        else:
            flex_level = 1
    elif sex == "F" and age_group == "20-29":
        if test.sit_and_reach >= 40:
            flex_level = 5
        elif test.sit_and_reach >= 35:
            flex_level = 4
        elif test.sit_and_reach >= 31:
            flex_level = 3
        elif test.sit_and_reach >= 26:
            flex_level = 2
        else:
            flex_level = 1
    elif sex == "F" and age_group == "30-39":
        if test.sit_and_reach >= 39:
            flex_level = 5
        elif test.sit_and_reach >= 34:
            flex_level = 4
        elif test.sit_and_reach >= 30:
            flex_level = 3
        elif test.sit_and_reach >= 25:
            flex_level = 2
        else:
            flex_level = 1
    elif sex == "F" and age_group == "40-49":
        if test.sit_and_reach >= 37:
            flex_level = 5
        elif test.sit_and_reach >= 32:
            flex_level = 4
        elif test.sit_and_reach >= 28:
            flex_level = 3
        elif test.sit_and_reach >= 23:
            flex_level = 2
        else:
            flex_level = 1
    elif sex == "F" and age_group == "50-59":
        if test.sit_and_reach >= 37:
            flex_level = 5
        elif test.sit_and_reach >= 30:
            flex_level = 4
        elif test.sit_and_reach >= 27:
            flex_level = 3
        elif test.sit_and_reach >= 23:
            flex_level = 2
        else:
            flex_level = 1
    elif sex == "F" and age_group == "60+":
        if test.sit_and_reach >= 34:
            flex_level = 5
        elif test.sit_and_reach >= 28:
            flex_level = 4
        elif test.sit_and_reach >= 25:
            flex_level = 3
        elif test.sit_and_reach >= 21:
            flex_level = 2
        else:
            flex_level = 1

    if sex == "M" and vo2_group == "20-29":
        if vo2max >= 56:
            cardio_level = 5
        elif vo2max >= 51:
            cardio_level = 4
        elif vo2max >= 46:
            cardio_level = 3
        elif vo2max >= 42:
            cardio_level = 2
        else:
            cardio_level = 1
    elif sex == "M" and vo2_group == "30-39":
        if vo2max >= 54:
            cardio_level = 5
        elif vo2max >= 48:
            cardio_level = 4
        elif vo2max >= 44:
            cardio_level = 3
        elif vo2max >= 41:
            cardio_level = 2
        else:
            cardio_level = 1
    elif sex == "M" and vo2_group == "40-49":
        if vo2max >= 53:
            cardio_level = 5
        elif vo2max >= 46:
            cardio_level = 4
        elif vo2max >= 42:
            cardio_level = 3
        elif vo2max >= 38:
            cardio_level = 2
        else:
            cardio_level = 1
    elif sex == "M" and vo2_group == "50-59":
        if vo2max >= 49:
            cardio_level = 5
        elif vo2max >= 43:
            cardio_level = 4
        elif vo2max >= 39:
            cardio_level = 3
        elif vo2max >= 35:
            cardio_level = 2
        else:
            cardio_level = 1
    elif sex == "M" and vo2_group == "60-69":
        if vo2max >= 45:
            cardio_level = 5
        elif vo2max >= 39:
            cardio_level = 4
        elif vo2max >= 35:
            cardio_level = 3
        elif vo2max >= 32:
            cardio_level = 2
        else:
            cardio_level = 1
    elif sex == "M" and vo2_group == "70+":
        if vo2max >= 43:
            cardio_level = 5
        elif vo2max >= 36:
            cardio_level = 4
        elif vo2max >= 32:
            cardio_level = 3
        elif vo2max >= 29:
            cardio_level = 2
        else:
            cardio_level = 1
    elif sex == "F" and vo2_group == "20-29":
        if vo2max >= 49:
            cardio_level = 5
        elif vo2max >= 44:
            cardio_level = 4
        elif vo2max >= 40:
            cardio_level = 3
        elif vo2max >= 36:
            cardio_level = 2
        else:
            cardio_level = 1
    elif sex == "F" and vo2_group == "30-39":
        if vo2max >= 47:
            cardio_level = 5
        elif vo2max >= 42:
            cardio_level = 4
        elif vo2max >= 37:
            cardio_level = 3
        elif vo2max >= 34:
            cardio_level = 2
        else:
            cardio_level = 1
    elif sex == "F" and vo2_group == "40-49":
        if vo2max >= 45:
            cardio_level = 5
        elif vo2max >= 39:
            cardio_level = 4
        elif vo2max >= 36:
            cardio_level = 3
        elif vo2max >= 33:
            cardio_level = 2
        else:
            cardio_level = 1
    elif sex == "F" and vo2_group == "50-59":
        if vo2max >= 41:
            cardio_level = 5
        elif vo2max >= 36:
            cardio_level = 4
        elif vo2max >= 32:
            cardio_level = 3
        elif vo2max >= 29:
            cardio_level = 2
        else:
            cardio_level = 1
    elif sex == "F" and vo2_group == "60-69":
        if vo2max >= 37:
            cardio_level = 5
        elif vo2max >= 33:
            cardio_level = 4
        elif vo2max >= 29:
            cardio_level = 3
        elif vo2max >= 27:
            cardio_level = 2
        else:
            cardio_level = 1
    elif sex == "F" and vo2_group == "70+":
        if vo2max >= 37:
            cardio_level = 5
        elif vo2max >= 30:
            cardio_level = 4
        elif vo2max >= 28:
            cardio_level = 3
        elif vo2max >= 26:
            cardio_level = 2
        else:
            cardio_level = 1

    return vo2max, push_level, sit_level, bench_level, leg_level, flex_level, cardio_level


top = tk.Tk()
top.title("FITADVISOR / AXIS SYSTEM")
top.geometry("380x520")
frame = tk.Frame(top, padx=15, pady=15)
frame.pack(fill="both", expand=True)

LEVELS = {1: "Poor", 2: "Below Average", 3: "Average", 4: "Above Average", 5: "Excellent"}




def button(text, cmd):
    tk.Button(frame, text=text, command=cmd, width=25).pack()


def form(fields, secret=()):
    entries = {}
    for name in fields:
        tk.Label(frame, text=name).pack()
        e = tk.Entry(frame, show="*" if name in secret else "")
        e.pack()
        entries[name] = e
    return entries


def login_screen():
    global current_user
    current_user = None
    e = form(["Email", "Password"], secret=["Password"])

    def log_in():
        global current_user
        for u in myUserList:
            if u.email == e["Email"].get() and u.password == e["Password"].get():
                current_user = u
                return dashboard()
        messagebox.showerror("Error", "Invalid email or password.")

    button("Log In", log_in)
    button("Register New User", register_screen)
    button("Exit", top.destroy)


def register_screen():
    e = form(["Name", "Age", "Gender (Male/Female)", "Height (cm)", "Weight (kg)",
              "Email", "Password", "Repeat password"], secret=["Password", "Repeat password"])


    button(text="Register",)
    button("Back", login_screen)


def dashboard():
    button(text="Display My Info")
    button(text="Record Fitness Test")
    button(text="Calculation Module")
    button(text ="Display My Fitness Tests")
    button(text="Log Out")
    button(text="Exit Program")





login_screen()
top.mainloop()
