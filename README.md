# Internet Miror
<!-- markdownlint-configure-file { "MD004": { "style": "consistent" } } -->
<!-- markdownlint-disable MD033 -->

### Step 1: Clone the repository

```bash
git clone --depth 1 https://github.com/gussieIsASucessfullWarlock/Internet-Mirror.git
```

### Step 2: Run

```bash
bash install.sh
```

### Step 3: Configure MySql

<p>The script will automaticly run the MySql Secure Installation. You must configure mysql properly for the app to work.</p>

```bash
Password Strength: 0
```

```bash
New Password: Your Choice
```

```bash
Verify Password: Your Choice
```

```bash
Do you wish to continue with the password provided? y
```



```bash
Remove anonymous users? (Press y|Y for Yes, any other key for No) : y
```

```bash
Disallow root login remotely? (Press y|Y for Yes, any other key for No) : n
```

```bash
Remove test database and access to it? (Press y|Y for Yes, any other key for No) : y
```

```bash
Reload privilege tables now? (Press y|Y for Yes, any other key for No) : y
```

### Step 3: Configure Run At Boot
Run:

```bash
sudo crontab -e 
```

Chose Nano and write:

```bash
@reboot python3 /bin/stest.py &
```

then save and close the file.

```bash
sudo reboot
```

### Step 3: Configure The Web Page

Open your web browser and type:

<a href="http://localhost:3000">http://serverip:3000</a>

Go To: Settings > Data Sources > Add data source

```bash
Select: MySql
```
```bash
Host: localhost:3306
```
```bash
Database: Connections
```
```bash
User: root
```
```bash
Password: Password you set in step 3
```

Then Create your dashboard how-ever you want.
