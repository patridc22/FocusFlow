# 📱 How to Install FocusFlow on Your Phone

FocusFlow is a Progressive Web App (PWA) that works on any device! Here's how to add it to your home screen:

## 📱 iPhone/iPad (iOS Safari)

1. **Open Safari** and go to your FocusFlow website
2. **Tap the Share button** (square with arrow pointing up) at the bottom
3. **Scroll down** and tap **"Add to Home Screen"**
4. **Name it** "FocusFlow" (or whatever you like)
5. **Tap "Add"** in the top right
6. **Done!** 🎉 The app icon will appear on your home screen

### iOS Tips:
- Must use **Safari** (not Chrome or other browsers)
- The app will open in full-screen mode (no browser bars!)
- Works offline once installed
- Looks and feels like a native app

---

## 🤖 Android (Chrome/Firefox)

1. **Open Chrome** (or your browser) and go to your FocusFlow website
2. **Tap the three dots** menu (⋮) in the top right
3. **Tap "Add to Home screen"** or "Install app"
4. **Name it** "FocusFlow"
5. **Tap "Add"** or "Install"
6. **Done!** 🎉 The app icon will appear on your home screen

### Android Tips:
- You may see an automatic "Install" banner at the bottom
- Works in Chrome, Firefox, Samsung Internet, and other modern browsers
- The app will open in standalone mode
- Push notifications supported (coming soon!)

---

## 💻 Desktop (Windows/Mac/Linux)

### Chrome/Edge/Brave:
1. **Open the website** in Chrome, Edge, or Brave
2. **Look for the install icon** (⊕ or computer icon) in the address bar
3. **Click "Install"**
4. **Done!** The app opens in its own window

### Instructions:
- Or go to **Settings** → **More Tools** → **Install FocusFlow**
- The app will appear in your applications folder
- Opens in its own window (no browser tabs!)

---

## ✨ Features After Installing:

✅ **Works Offline** - Access your tasks without internet
✅ **Home Screen Icon** - Quick access like a native app
✅ **Full Screen** - No browser bars, immersive experience
✅ **Fast Loading** - Cached for instant startup
✅ **Auto Updates** - Always get the latest features
✅ **Cross-Device Sync** - Same data everywhere (with account)

---

## 🌐 Hosting Your Own Instance

### Option 1: Quick Test (Local)
```bash
cd ~/FocusFlow
python3 -m http.server 8000
# Open: http://localhost:8000
```

### Option 2: Deploy to Netlify (Free & Easy)
1. Go to [netlify.com](https://netlify.com)
2. Drag & drop the FocusFlow folder
3. Get instant URL: `your-app.netlify.app`
4. Share with anyone!

### Option 3: Deploy to Vercel (Free)
```bash
npm install -g vercel
cd ~/FocusFlow
vercel
```

### Option 4: Deploy to GitHub Pages (Free)
1. Create GitHub repo
2. Upload FocusFlow files
3. Enable GitHub Pages
4. Access at: `username.github.io/focusflow`

### Option 5: Custom Domain
- Use any hosting (Netlify, Vercel, etc.)
- Add your own domain
- Enable HTTPS (required for PWA features)

---

## 🔧 Troubleshooting

**"Add to Home Screen" not showing?**
- Make sure you're using HTTPS (not HTTP)
- For local testing, use `localhost` (which is allowed)
- Clear browser cache and try again

**Icons not loading?**
- Run the icon generator: `create-icons.html`
- Download both `icon-192.png` and `icon-512.png`
- Place them in the FocusFlow folder

**App not working offline?**
- Make sure Service Worker registered successfully
- Check browser console for errors
- Try reinstalling the app

**Updates not showing?**
- Uninstall and reinstall the app
- Or clear cache: Settings → Storage → Clear Data

---

## 📊 PWA Stats

- ✅ Installable on iOS, Android, Windows, Mac, Linux
- ✅ Works offline
- ✅ 100% browser-based (no app stores!)
- ✅ Instant updates
- ✅ Tiny size (~500KB)
- ✅ No permissions needed

---

## 🎯 Next Steps

1. Install the app on your phone
2. Add some tasks and goals
3. Choose your favorite theme
4. Start being productive!

**Need help?** Check the browser console (F12) for error messages.

Made with 💜 for ADHD warriors everywhere!
