# Batavia Aerospace — Website

> **Stack:** HTML · CSS · Vanilla JS · JSON content files · No build step · GitHub Pages

---

## Table of Contents

1. [Folder Structure](#folder-structure)
2. [From Zero to Live — Complete Setup Guide](#from-zero-to-live)
   - Step 1 — Install Git
   - Step 2 — Create the GitHub repository
   - Step 3 — Download & connect the site files
   - Step 4 — Run locally
   - Step 5 — Push to GitHub
   - Step 6 — Enable GitHub Pages
   - Step 7 — Connect your custom domain
   - Step 8 — Set up Google Analytics
3. [Everyday Workflow — Making Updates](#everyday-workflow)
4. [Content Editing Reference](#content-editing-reference)
   - Add an Update
   - Add a Team Member
   - Change a Photo
   - Add a Rocket Project
   - Add Flight Data
   - Add a Certification
   - Change Site Settings
5. [Image Guidelines](#image-guidelines)
6. [Troubleshooting](#troubleshooting)

---

## Folder Structure

```
batavia-aerospace/
│
├── index.html                   ← Main page (rarely needs editing)
├── serve.py                     ← Local preview server
├── .gitignore
│
├── content/                     ← ✅ EDIT THESE for all content changes
│   ├── config.json              ← Email, donate URL, social links, stats
│   ├── updates.json             ← News posts (add newest at the top)
│   ├── team.json                ← Team member names, roles, photo paths
│   ├── rocketry-projects.json  ← Rocket projects and flight data
│   ├── aviation.json            ← RC aircraft and goals
│   └── certifications.json     ← L1/L2 certifications
│
├── assets/
│   ├── css/style.css            ← All styling
│   ├── js/render.js             ← Reads JSON and builds the page
│   └── images/
│       ├── logo-patch.png
│       ├── hcb-logo.png
│       ├── team/                ← Headshots
│       ├── rocketry/            ← Rocket photos and CAD renders
│       └── aviation/            ← RC aircraft photos
│
└── docs/
    └── ANALYTICS.md             ← Analytics setup detail
```

---

## From Zero to Live

Follow these steps exactly, in order. Estimated total time: **30–45 minutes**.

---

### Step 1 — Install Git

**Check if you already have it:**
Open Terminal (Mac) or Command Prompt (Windows) and type:
```
git --version
```
If you see a version number, skip to Step 2.

**If not installed:**
- **Mac:** Run `xcode-select --install` in Terminal, click Install in the popup
- **Windows:** Download from [git-scm.com/download/win](https://git-scm.com/download/win), run installer with all defaults

After installing, set your name and email (one time only):
```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

---

### Step 2 — Create the GitHub Repository

1. Go to [github.com](https://github.com) and sign in (or create a free account)
2. Click the **+** icon (top right) → **New repository**
3. Fill in:
   - **Repository name:** `batavia-aerospace-site`
   - **Description:** `Batavia Aerospace website`
   - **Visibility:** Public ← required for free GitHub Pages
   - **Do NOT** check "Add a README file" or any other init options
4. Click **Create repository**
5. You'll land on an empty repo page. **Copy the URL** shown — it looks like:
   `https://github.com/YOUR-USERNAME/batavia-aerospace-site.git`
   Keep this page open, you'll need the URL in Step 3.

---

### Step 3 — Download & Connect the Site Files

1. **Unzip** the `batavia-aerospace-site.zip` file you downloaded from Claude
2. **Rename** the unzipped folder to `batavia-aerospace-site` (remove any `-1` or copy suffix)
3. Open **Terminal** (Mac) or **Command Prompt** (Windows)
4. Navigate into the folder. Replace the path with wherever you unzipped it:

   **Mac:**
   ```bash
   cd ~/Downloads/batavia-aerospace-site
   ```
   **Windows:**
   ```bash
   cd C:\Users\YourName\Downloads\batavia-aerospace-site
   ```

5. Initialize Git and connect to GitHub:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Batavia Aerospace website"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/batavia-aerospace-site.git
   git push -u origin main
   ```
   > Replace `YOUR-USERNAME` with your actual GitHub username.
   > If prompted for a password, use a **Personal Access Token**, not your GitHub password.
   > Generate one at: GitHub → Settings → Developer settings → Personal access tokens → Generate new token (classic) → check `repo` → copy it.

6. Refresh your GitHub repo page — you should see all the files appear. ✅

---

### Step 4 — Run Locally (Preview Before Publishing)

You need Python 3 for the local server (it comes pre-installed on Mac).

**Mac:**
```bash
python3 serve.py
```

**Windows:**
```bash
python serve.py
```

Your browser will open automatically at `http://localhost:8080`.
The full site should load with all your images and content.

**To stop the server:** press `Ctrl+C` in the terminal.

> ⚠️ You must use `serve.py` — double-clicking `index.html` won't work because
> browsers block the `fetch()` calls that load JSON files from local disk.

---

### Step 5 — Push Updates to GitHub

After making any change to content or images:

```bash
git add .
git commit -m "Brief description of what you changed"
git push
```

Examples of good commit messages:
```
git commit -m "Add G8 launch update — April 2026"
git commit -m "Update team photo for Matteo"
git commit -m "Add Grainger 9 project"
```

---

### Step 6 — Enable GitHub Pages (Free Hosting)

1. Go to your repo on GitHub
2. Click **Settings** (top menu of the repo)
3. Click **Pages** in the left sidebar
4. Under **Source**, select:
   - Branch: `main`
   - Folder: `/ (root)`
5. Click **Save**
6. Wait 60–90 seconds, then your site will be live at:
   `https://YOUR-USERNAME.github.io/batavia-aerospace-site/`

> Every time you `git push`, GitHub Pages automatically rebuilds within ~60 seconds.

---

### Step 7 — Connect Your Custom Domain

This connects a domain you own (e.g. `batavia-aerospace.com`) to your GitHub Pages site.

**7a. In GitHub — add your domain:**

1. Go to your repo → Settings → Pages
2. Under **Custom domain**, type your domain (e.g. `batavia-aerospace.com`) and click **Save**
3. GitHub will create a file called `CNAME` in your repo automatically

**7b. In your domain registrar — add DNS records:**

Log into wherever you bought the domain (Namecheap, Google Domains, GoDaddy, Squarespace, etc.) and find the **DNS settings** for your domain. Add these records:

| Type  | Host / Name | Value              |
|-------|-------------|-------------------|
| A     | @           | 185.199.108.153   |
| A     | @           | 185.199.109.153   |
| A     | @           | 185.199.110.153   |
| A     | @           | 185.199.111.153   |
| CNAME | www         | YOUR-USERNAME.github.io |

> The exact labels ("Host", "Name", "Points to") vary by registrar but the values are the same.

**7c. Wait for DNS to propagate:**

DNS changes take **5 minutes to 48 hours** to go live globally. Usually it's under 30 minutes.

**7d. Enable HTTPS:**

Once the domain is working, go back to GitHub → Settings → Pages and check:
**"Enforce HTTPS"** ✅

Your site will now be live at `https://batavia-aerospace.com` (or whatever domain you bought).

**Domain registrar quick links:**
- **Namecheap:** Domain List → Manage → Advanced DNS
- **Google Domains / Squarespace:** DNS → Custom Records
- **GoDaddy:** My Products → DNS → Add

---

### Step 8 — Set Up Google Analytics (Free Traffic Tracking)

**8a. Create a GA4 property:**

1. Go to [analytics.google.com](https://analytics.google.com) — sign in with a Google account
2. Click **Start measuring**
3. Account name: `Batavia Aerospace` → Next
4. Property name: `Batavia Aerospace Website` → Next
5. Choose **Web** → enter your site URL → Stream name: `Main`
6. Click **Create stream**
7. Copy your **Measurement ID** — it looks like `G-A1B2C3D4E5`

**8b. Add it to the site:**

Open `index.html` and find these two lines near the top:
```html
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
...
gtag('config', 'G-XXXXXXXXXX');
```
Replace both `G-XXXXXXXXXX` with your real Measurement ID.

Also open `content/config.json` and update:
```json
"googleAnalyticsId": "G-A1B2C3D4E5"
```

**8c. Push the change:**
```bash
git add .
git commit -m "Add Google Analytics tracking ID"
git push
```

**8d. View your dashboard:**

→ [analytics.google.com](https://analytics.google.com) → click your property
- **Realtime** → see live visitors right now
- **Reports → Acquisition** → where visitors come from (Instagram, direct, Google, etc.)
- **Reports → Engagement → Pages** → which sections people visit most

> ℹ️ Analytics data starts showing after 24–48 hours of the first real visit.

---

## Everyday Workflow

```
Make a change to a JSON file or add an image
        ↓
python3 serve.py    ← preview at localhost:8080
        ↓
Looks good?
        ↓
git add .
git commit -m "What you changed"
git push            ← live on your domain in ~60 seconds
```

---

## Content Editing Reference

### 📰 Add a News Update

Open `content/updates.json`. Copy this block and paste it at the **very top** of the array (before the first `{`):

```json
{
  "date": "Friday, April 10, 2026",
  "title": "Your Update Title",
  "description": "Description of what happened."
},
```

The newest update should always be first in the file. Remove old ones if the list gets too long.

---

### 👤 Add a Team Member

Open `content/team.json`. Add a new object to the array:

```json
{
  "name": "First Last",
  "role": "Project Member",
  "subrole": "Their Focus Area",
  "photo": "assets/images/team/first-last.png"
}
```

Then add their photo to `assets/images/team/` with the matching filename.

---

### 🖼️ Change a Photo

1. Add your new image file to the correct folder:
   - Team headshots → `assets/images/team/`
   - Rocket/launch photos → `assets/images/rocketry/`
   - RC aircraft photos → `assets/images/aviation/`

2. Update the path in the relevant JSON file to match the new filename.

**Use descriptive filenames.** Good: `g8-launch-april2026.jpg`. Bad: `IMG_5234.jpg`.

---

### 🚀 Add a New Rocket Project

Open `content/rocketry-projects.json`. Add a new object to the array:

```json
{
  "id": "grainger-9",
  "name": "Grainger 9",
  "status": "progress",
  "statusLabel": "In Progress",
  "description": "Description of the project.",
  "designNotes": "Construction notes here.",
  "images": [
    "assets/images/rocketry/g9-main.png",
    "assets/images/rocketry/g9-detail.png",
    "assets/images/rocketry/g9-cad.png"
  ],
  "flightData": [],
  "meta": [
    { "label": "Launch Date",    "value": "TBD"               },
    { "label": "Location",       "value": "QCRC, Princeton IL" },
    { "label": "Motor Class",    "value": "M-class"            },
    { "label": "Target Altitude","value": "~10,000 ft"         }
  ],
  "cadLink": null
}
```

**Status values:** `launched` · `progress` · `planned`

---

### 📊 Add Flight Data to a Project

Once a rocket has flown, add its data. In `content/rocketry-projects.json`, find the project and update `"flightData"`:

```json
"flightData": [
  {
    "label": "J500 · March 2026",
    "id": "g8-j500",
    "stats": [
      { "label": "Altitude",       "value": "6,400 ft"         },
      { "label": "Max Velocity",   "value": "890 ft/s"         },
      { "label": "Time to Apogee", "value": "15.2 s"           },
      { "label": "Flight Time",    "value": "112 s"            },
      { "label": "Motor",          "value": "J500T (900 Ns)"   },
      { "label": "Thrust-to-Wt",  "value": "13.2:1"           }
    ]
  }
]
```

If there are multiple flights, just add more objects to the array — they become tabs on the site.

Also update `"status"` from `"progress"` to `"launched"` and `"statusLabel"` to `"Launched"`.

---

### 🏅 Add a Certification

Open `content/certifications.json`. Add to the array:

```json
{
  "name": "First Last",
  "program": "High Power Rocketry",
  "certification": "L1 Certified",
  "date": "Month DD, YYYY",
  "location": "Location Name",
  "description": "Brief description of the certification flight."
}
```

---

### ⚙️ Change Global Site Settings

Open `content/config.json`:

| Field | What it changes |
|-------|----------------|
| `email` | Contact email in the Join section |
| `donateUrl` | HCB donation link used on all donate buttons |
| `googleAnalyticsId` | Your GA4 Measurement ID |
| `social.instagram` | Instagram profile URL |
| `social.tiktok` | TikTok profile URL |
| `social.youtube` | YouTube channel URL |
| `social.linkedin` | LinkedIn page URL |
| `stats` | The four numbers in the About section |
| `joinBullets` | Tags shown in the Join section |
| `heroImage` | Background photo on the main hero section |
| `aboutImage` | Photo in the About section |

---

## Image Guidelines

| Type | Dimensions | Format | Notes |
|------|-----------|--------|-------|
| Team headshots | 600 × 600 px | PNG or JPG | Square crop, face centered |
| Rocket photos | 1200 × 900 px | JPG | Landscape preferred |
| CAD renders | 1400 × 700 px | PNG | Dark background looks best |
| Hero background | 1920 × 1080 px | JPG | High detail, people/action |
| RC aircraft | 1200 × 800 px | JPG | Landscape preferred |

**Always compress images before uploading** — large images slow the site significantly.
Free tool: [squoosh.app](https://squoosh.app) — drag in the image, set Quality to 80%, download.

---

## Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| Page is blank / content missing | Opened index.html directly | Use `python3 serve.py` instead |
| Image not showing | Wrong filename or path | Check the path in the JSON exactly matches the file (case-sensitive) |
| JSON edit broke the site | Syntax error (missing comma, bracket) | Validate at [jsonlint.com](https://jsonlint.com) |
| Site not updating after `git push` | GitHub Pages cache | Wait 60–90 seconds, hard refresh (Ctrl+Shift+R) |
| Custom domain not working | DNS hasn't propagated | Wait up to 48 hours; check at [dnschecker.org](https://dnschecker.org) |
| HTTPS not available | Domain just connected | Enable in GitHub → Settings → Pages → Enforce HTTPS |
| Analytics shows no data | Too soon after setup | GA4 takes 24–48 hours to show data |
| `git push` asks for password | GitHub removed password auth | Use a Personal Access Token instead (see Step 3) |
