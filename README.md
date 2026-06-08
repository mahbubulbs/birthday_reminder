# 📌 Birthday Reminder App (Odoo Module)

## 🎯 Overview

This module is a simple **Birthday Reminder & Wish automation app** built on the Odoo framework.
It allows users to store birthdays and automatically send reminders or wishes based on scheduled dates.

---

## 🚀 Features

* 📅 Store user birthdays
* 🔔 Daily automatic birthday reminder (cron job)
* 📧 Email notification for birthday wishes
* 👤 Simple form & list UI
* 🧠 Easy to extend for SMS / WhatsApp integration (future scope)

---

## 🧱 Module Structure

```text
birthday_reminder/
│
├── models/              # Python business logic
├── views/               # XML UI (menu, form, list)
├── data/                # Scheduled actions, email templates
├── security/           # Access rights (CSV)
├── __init__.py
├── __manifest__.py
└── README.md
```

---

## ⚙️ Installation

1. Clone this repo inside Odoo custom addons folder:

```bash
git clone https://github.com/mahbubulbs/birthday_reminder.git
```

2. Restart Odoo server:

```bash
./odoo-bin -c odoo.conf
```

3. Activate developer mode

4. Install module:

```
Apps → Birthday Reminder → Install
```

---

## 🧠 How It Works

1. User adds birthday in form view
2. System stores date in database
3. Cron job runs daily
4. If today matches birthday → email sent automatically

---

## 📧 Email Automation

* Uses Odoo mail template system
* Triggered via scheduled action (`ir.cron`)

---

## 🔐 Security

* Access controlled via `ir.model.access.csv`
* Only internal users can manage records

---

## 📦 Future Improvements

* WhatsApp / SMS integration
* Age calculation feature
* Reminder before 1–7 days
* Multi-language support
* Dashboard view

---

## 👨‍💻 Author

**Md Mahbubul Hasan**


---

## 📄 License

This project is for learning and development purposes.

---


