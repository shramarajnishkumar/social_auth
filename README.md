## **Project setup Guide**
### **Step 1: Clone the project from [github](https://github.com/shramarajnishkumar/social_auth.git)**
### **Step 2: open the project in your IDE**
### **Step 3: create the virtual environment using the following command**
### **Step 4: python3 -m venv <your-environment-name>**
### **Step 5: Activate the virtual environment using the following command**
### **Step 6: source <your-environment-name>/bin/activate**
### **Step 7: Install the required packages using the following command**
### **Step 8: pip install -r requirements.txt**
### **Step 9: migrate the project using the following command**
### **Step 10: python3 manage.py makemigrations**
### **Step 11: python3 manage.py migrate**
### **Step 12: run the project using the following command**
### **Step 13: python3 manage.py runserver**



## **Google Login Integration Guide**

### **Step 1: Create a Google OAuth App**
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click **Select a project** → **New Project**
3. Give it a name and click **Create**
4. Navigate to **APIs & Services** → **Credentials**
5. Click **Create Credentials** → **OAuth 2.0 Client ID**
6. Choose **Application Type**:
   - **Web Application** (for web apps)
   - **Android/iOS** (for mobile apps)
7. Set **Authorized Redirect URIs**:
   - Example: `http://localhost:8000/google/callback/`
8. Click **Create** and save your **Client ID** and **Client Secret**


### **Step 2: Enable Google OAuth API**
1. Go to **APIs & Services** → **Library**
2. Search for **"Google+ API"** or **"Google Identity Services"**
3. Click **Enable API**


## **GitHub OAuth 2.0 Integration in Django REST Framework**

### **Step 1: Create a GitHub OAuth App**
1. Go to [GitHub Developer Settings](https://github.com/settings/developers)
2. Click "New OAuth App"
3. Fill in the details:
4. Application name: (Your app name)
5. Homepage URL: http://127.0.0.1:8000/
6. Authorization callback URL: http://127.0.0.1:8000/github/callback/
7. Click Register application
8. Copy Client ID and Client Secret


## **GitHub OAuth 2.0 Integration in Django REST Framework**
### **Step 1: Create a LinkedIn OAuth App**
1. Go to [LinkedIn Developer Portal](https://www.linkedin.com/developers/apps)
2. Click "Create App" and fill in the details:
    App Name: (Your app name)
    LinkedIn Page: (If applicable)
    Email: Your contact email


3. Once created, go to the Auth tab.
4. Add OAuth Redirect URLs: http://127.0.0.1:8000/linkedin/callback/
5. Enable OAuth 2.0 permissions:
    r_liteprofile (Basic profile)
    r_emailaddress (Email)
6. Copy Client ID and Client Secret





