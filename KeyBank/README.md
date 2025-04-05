# Public_Python_Projects_1
---

## 🔧 Projects Included

This repo includes self-contained Python scripts such as:

- ✅ **Password Manager** – Create and retrieve passwords stored securely in a SQL Server database.
- 📦 Other handy CLI utilities (coming soon).

---

## 📁 Project Structure

```
Public_Python_Projects/
│
├── password_manager.py     # Main script to insert/retrieve passwords
├── pwcreate.py             # Module to generate secure passwords & get timestamps
├── script.sql              # SQL script to create the necessary table
├── README.md               # This file
```

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash or CMD
git clone https://github.com/abinash2017/Public_Python_Projects.git
cd Public_Python_Projects
```

### 2. Install Python Dependencies

```bash or CMD
pip install pymssql colorama
```

### 3. Create the Database Table

Make sure you have SQL Server running and a database created (e.g., `MARK_1`).

Then, execute the `script.sql` file to create the required table:

#### Using SQL Server Management Studio (SSMS)
1. Open `script.sql` in SSMS.
2. Connect to your SQL Server and your database (e.g., `MARK_1`).
3. Run the script.



## 💻 How to Run

```bash or CMD
python password_manager.py
```

Follow the prompts:
- Choose to insert a new password or view an old one.
- Enter the application name when prompted.
- Passwords are stored and retrieved from your SQL Server database.

---

## 🧠 Future Additions

- [ ] Add encryption for stored passwords
- [ ] Master password to unlock the app
- [ ] Option to export passwords
- [ ] GUI version

---

