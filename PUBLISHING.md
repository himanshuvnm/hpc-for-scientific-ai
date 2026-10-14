# Create and publish the GitHub repository

The downloaded starter is **not yet hosted on GitHub**. Only the owner can create the remote repository and configure Pages.

1. On GitHub, create a **public, empty** repository named `hpc-for-scientific-ai`. Do not generate a second README, license, or `.gitignore`.
2. Extract the starter archive. In a terminal, `cd` into the extracted `hpc-for-scientific-ai` directory.
3. Run (replace `YOUR_USERNAME` with your GitHub username):

```bash
git init -b main
git add .
git commit -m "Initial release: HPC for Scientific AI v0.1"
git remote add origin https://github.com/YOUR_USERNAME/hpc-for-scientific-ai.git
git push -u origin main
```

4. In GitHub: **Settings → Pages → Build and deployment → Deploy from a branch → main /docs → Save**.
5. The site will appear at `https://YOUR_USERNAME.github.io/hpc-for-scientific-ai/` after Pages deployment finishes.
6. Replace `YOUR_USERNAME` in `docs/index.html` with your actual account name and push again to activate GitHub links on the homepage.
7. Under **Actions**, inspect the Python CI workflow and ensure it passes. Enable any repository permission prompts GitHub requires.

Do not mark any Roar/Aurora example as verified until it has run under an authorized allocation and its non-sensitive evidence has been reviewed.
