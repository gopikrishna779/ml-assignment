import random
import sqlite3
import tkinter as tk
from tkinter import messagebox

# ==========================================
# DATABASE SETUP
# ==========================================

conn = sqlite3.connect("smart_fan_rl.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS training_log (
    episode INTEGER,
    room TEXT,
    temperature TEXT,
    fan_speed TEXT,
    reward INTEGER
)
""")

conn.commit()

# ==========================================
# ROOM TEMPERATURE DATA
# ==========================================

rooms = {
    "Hall": "Hot",
    "Bedroom": "Warm",
    "Kitchen": "Hot",
    "Study": "Normal"
}

# ==========================================
# FAN SPEED BASED ON TEMPERATURE
# ==========================================

fan_speeds = {
    "Cold": "OFF",
    "Normal": "LOW",
    "Warm": "MEDIUM",
    "Hot": "HIGH"
}

# ==========================================
# STORE TRAINING DATA
# ==========================================

for episode in range(1, 101):

    room = random.choice(list(rooms.keys()))

    temperature = rooms[room]

    speed = fan_speeds[temperature]

    reward = 10

    cursor.execute(
        "INSERT INTO training_log VALUES (?, ?, ?, ?, ?)",
        (episode, room, temperature, speed, reward)
    )

conn.commit()

# ==========================================
# MAIN WINDOW
# ==========================================

root = tk.Tk()

root.title("AI Smart Fan Controller")

root.geometry("1000x700")

root.configure(bg="white")

# ==========================================
# TITLE
# ==========================================

title = tk.Label(
    root,
    text="AI Smart Fan Speed Controller",
    font=("Arial", 24, "bold"),
    bg="white",
    fg="black"
)

title.pack(pady=20)

# ==========================================
# CANVAS
# ==========================================

canvas = tk.Canvas(
    root,
    width=900,
    height=500,
    bg="lightgray"
)

canvas.pack()

# ==========================================
# ROOM POSITIONS
# ==========================================

room_positions = {
    "Hall": (50, 50, 400, 220),
    "Bedroom": (500, 50, 850, 220),
    "Kitchen": (50, 280, 400, 450),
    "Study": (500, 280, 850, 450)
}

# ==========================================
# ROOM COLORS
# ==========================================

colors = {
    "Cold": "skyblue",
    "Normal": "lightgreen",
    "Warm": "orange",
    "Hot": "red"
}

# ==========================================
# FAN ICONS
# ==========================================

fan_icons = {
    "OFF": "⚫",
    "LOW": "🌀",
    "MEDIUM": "🌪",
    "HIGH": "💨"
}

# ==========================================
# DRAW ROOMS
# ==========================================

for room, temperature in rooms.items():

    x1, y1, x2, y2 = room_positions[room]

    room_color = colors[temperature]

    speed = fan_speeds[temperature]

    icon = fan_icons[speed]

    # Room Box
    canvas.create_rectangle(
        x1,
        y1,
        x2,
        y2,
        fill=room_color,
        width=4
    )

    # Room Name
    canvas.create_text(
        (x1 + x2) // 2,
        y1 + 30,
        text=room,
        font=("Arial", 18, "bold")
    )

    # Temperature
    canvas.create_text(
        (x1 + x2) // 2,
        y1 + 80,
        text=f"Temperature : {temperature}",
        font=("Arial", 14, "bold")
    )

    # Fan Speed
    canvas.create_text(
        (x1 + x2) // 2,
        y1 + 130,
        text=f"Fan Speed : {speed}",
        font=("Arial", 14, "bold")
    )

    # Fan Icon
    canvas.create_text(
        (x1 + x2) // 2,
        y1 + 180,
        text=icon,
        font=("Arial", 40)
    )

# ==========================================
# SHOW DATABASE LOGS
# ==========================================

def show_logs():

    cursor.execute("SELECT * FROM training_log LIMIT 10")

    rows = cursor.fetchall()

    log_text = ""

    for row in rows:

        log_text += (
            f"Episode : {row[0]}\n"
            f"Room : {row[1]}\n"
            f"Temperature : {row[2]}\n"
            f"Fan Speed : {row[3]}\n"
            f"Reward : {row[4]}\n"
            f"------------------------\n"
        )

    messagebox.showinfo("Training Logs", log_text)

# ==========================================
# BUTTON
# ==========================================

button = tk.Button(
    root,
    text="Show AI Training Logs",
    command=show_logs,
    font=("Arial", 14, "bold"),
    bg="black",
    fg="white",
    padx=20,
    pady=10
)

button.pack(pady=20)

# ==========================================
# TERMINAL OUTPUT
# ==========================================

print("\n========= AI SMART FAN OUTPUT =========\n")

for room, temperature in rooms.items():

    speed = fan_speeds[temperature]

    print(f"Room Name      : {room}")
    print(f"Temperature    : {temperature}")
    print(f"Selected Speed : {speed}")
    print("----------------------------------")

# ==========================================
# RUN WINDOW
# ==========================================

root.mainloop()

# ==========================================
# CLOSE DATABASE
# ==========================================

conn.close()