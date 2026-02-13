# 🚀 Deploy FocusFlow to Vercel

## Quick Deploy (Recommended)

### Option 1: Web UI (Easiest!)
1. Go to https://vercel.com
2. Sign up with GitHub, GitLab, or Bitbucket
3. Click "Add New Project"
4. Import your FocusFlow folder or repository
5. Click "Deploy"
6. Done! 🎉

### Option 2: Command Line
```bash
cd ~/FocusFlow
npx vercel
```

Follow the prompts:
- Set up and deploy? **Y**
- Which scope? (Select your account)
- Link to existing project? **N**
- What's your project's name? **focusflow** (or any name)
- In which directory is your code? **./** (just press Enter)
- Want to override settings? **N**

That's it! Vercel will give you a URL like:
`https://focusflow-abc123.vercel.app`

## Deploy Updates

After making changes:
```bash
cd ~/FocusFlow
npx vercel --prod
```

## Custom Domain (Optional)

1. Go to your Vercel dashboard
2. Select your project
3. Go to Settings → Domains
4. Add your custom domain
5. Follow DNS instructions

## Environment Variables

If you add a backend later:
1. Go to Vercel dashboard
2. Select project → Settings → Environment Variables
3. Add your API keys, Firebase config, etc.

## Auto-Deploy with Git

1. Push FocusFlow to GitHub
2. Import from Vercel dashboard
3. Every git push = automatic deploy! 🔥

---

**Your FocusFlow will be live at:**
`https://your-project-name.vercel.app`

Install it on your phone:
- iOS Safari: Share → Add to Home Screen
- Android Chrome: Menu → Add to Home screen

🎉 You're live!
