# GitHub Webhook Project

## 🚀 Project Overview

This is a full-stack project that tracks GitHub pull requests and push events in real-time using GitHub webhooks. It stores event data in a backend database and displays them in a clean, user-friendly Flutter web UI. The app helps visualize repository activity like branch creations, PRs, and merges.

---

## 🔗 Live Links

- 🖥️ **Frontend (Flutter Web)**: [Deployed App](https://testapp-50a7b.web.app/)
- 🧠 **Backend Webhook Repo**: [action_repo](https://github.com/jayPatel029/action-repo)
- 💻 **Frontend Code Repo**: [frontend_repo](https://github.com/jayPatel029/frontend-webhook)
- 🎥 **Demo Video**: [Watch Demo]([https://your-demo-video-url.com](https://drive.google.com/file/d/1YKxl1Eu-y9awf68w0wU_AIgRScb3wMcY/view?usp=sharing))

---

## 🧪 How to Test the Deployed App

You can simulate GitHub events and watch them update in real-time on the frontend by doing the following:

1. **Visit the Deployed App**  
   👉 [Open Frontend](https://testapp-50a7b.web.app)

2. **Open the GitHub Action Repo**  
   👉 [Open action_repo](https://github.com/jayPatel029/action-repo)

3. **Trigger Events:**
   - Fork or clone the repo if needed.
   - Create a new branch:
     ```bash
     git checkout -b test-feature
     ```
   - Make some changes and push the branch:
     ```bash
     git add .
     git commit -m "Test commit"
     git push origin test-feature
     ```
   - Create a Pull Request from `test-feature` to `main`.
   - Merge or close the PR.
   - Reopen the PR or edit it if needed.

4. **Watch in Real Time:**  
   Events like **push**, **pull_request opened**, **merged**, etc., will appear in the frontend UI.

---

## 🛠️ Tech Stack

- **Frontend**: Flutter Web
- **Backend**: Flask + MongoDB
- **GitHub Webhooks**: PRs, Merges, Pushes

---

Feel free to star the repo if you find it useful! ⭐
