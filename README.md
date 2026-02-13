# 🎯 FocusFlow - ADHD Task Manager

An ADHD-friendly task organization app with gamification and calendar integration!

## ✨ Features

### 🎮 Gamification
- **Points & Levels** - Earn 10-100 XP per task based on priority
- **Daily Streaks** - Track your consistency with fire emoji 🔥
- **Achievements** - Unlock 6 achievements as you progress
- **Epic Celebrations** - Motivational messages and floating emojis when you complete tasks!

### 📅 Calendar Integration
- **Google Calendar** - Auto-sync tasks with reminders (OAuth in production)
- **Apple Calendar** - Export tasks as .ics files
- **Due Dates & Times** - Set when tasks need to be done
- **Smart Reminders** - 15-minute advance notifications

### 📊 Organization Options
- **View by Category** - Work, Personal, Health, Learning, Finance, Social
- **View by Time** - Today, This Week, This Month, Later
- **View by Priority** - Low, Medium, High, Urgent (color-coded)
- **Custom Sections** - Collapsible sections to reduce overwhelm

### 👤 Profile & Progress
- **Customizable Avatar** - Choose from 16 fun emojis
- **Detailed Stats** - Track completed tasks, streaks, and progress
- **Achievement System** - Earn badges for milestones
- **Level Progression** - Visual progress bars

### 🧠 ADHD-Friendly Design
- Clear visual hierarchy with color-coding
- Satisfying click interactions
- Reduced clutter with collapsible sections
- Big, easy-to-tap buttons
- Visual progress tracking everywhere
- Instant feedback and celebrations

## 🚀 Getting Started

1. Open `index.html` in your web browser
2. Click **"+ Add Task"** to create your first task
3. Click **"📅 Calendar"** to set up calendar integration
4. Click **"Profile"** to customize your avatar and view achievements

## 📱 Calendar Setup

### Google Calendar
1. Click the **"📅 Calendar"** button
2. Click **"Connect Google Calendar"**
3. In production, this uses OAuth - for now it's demo mode
4. Enable "Auto-sync tasks with reminders"
5. Tasks with reminders will sync automatically!

### Apple Calendar / iCal
1. Click the **"📅 Calendar"** button
2. Click **"📥 Export to Calendar (.ics)"**
3. Download the .ics file
4. Double-click to open in Apple Calendar
5. Or import into Outlook, Google Calendar, or any calendar app!

## 🎯 Task Features

- **Task Title** - What needs to be done
- **Notes** - Additional details
- **Category** - Organize by life area
- **Priority** - Visual color-coding
- **Due Date** - When it needs to be done
- **Due Time** - Specific time of day
- **Reminder** - Sync to calendar for notifications

## 🏆 Achievements

- 🎯 **First Steps** - Complete your first task
- 🔥 **On a Roll** - Maintain a 3-day streak
- ⚡ **Week Warrior** - Maintain a 7-day streak
- 💪 **Productivity Pro** - Complete 10 tasks
- 👑 **Task Master** - Complete 50 tasks
- 🌟 **Rising Star** - Reach Level 5

## 💾 Data Storage

All your data is saved locally in your browser:
- Tasks persist between sessions
- Profile and stats are saved
- Calendar settings are remembered
- No server needed!

## 🔒 Privacy

- Everything runs locally in your browser
- No data is sent to any servers
- Calendar integration is opt-in
- Your data stays on your device

## 🛠️ For Production

To make this production-ready:

### Google Calendar Integration
```javascript
// Add OAuth 2.0 flow
const CLIENT_ID = 'your-google-client-id';
const API_KEY = 'your-google-api-key';
const SCOPES = 'https://www.googleapis.com/auth/calendar.events';

// Initialize Google API
gapi.load('client:auth2', initClient);
```

### Apple Calendar
The current .ics export works with:
- Apple Calendar (macOS/iOS)
- Microsoft Outlook
- Google Calendar (import)
- Any RFC 5545 compliant calendar app

### Backend (Optional)
Add a backend for:
- Cloud sync across devices
- Push notifications
- Social features
- Analytics

## 📖 Tech Stack

- **React 18** - UI framework
- **Google Calendar API** - Calendar integration structure
- **iCalendar (.ics)** - Universal calendar export
- **LocalStorage** - Data persistence
- **Vanilla CSS** - Styling with animations

## 🎨 Color Scheme

- **Primary**: Purple gradient (#667eea → #764ba2)
- **Success**: Green (#48bb78)
- **Warning**: Orange (#ed8936)
- **Danger**: Red (#f56565)
- **Priority Urgent**: Purple (#9f7aea)

## 📝 Future Ideas

- [ ] Recurring tasks
- [ ] Subtasks / checklists
- [ ] Pomodoro timer integration
- [ ] Dark mode
- [ ] Mobile app (React Native)
- [ ] Team collaboration
- [ ] AI task suggestions
- [ ] Voice commands
- [ ] Habit tracking
- [ ] Weekly reviews

## 💡 Tips for ADHD Users

1. **Start Small** - Add just 1-3 tasks to begin
2. **Use Priorities** - Focus on High/Urgent first
3. **Set Reminders** - Don't rely on memory alone
4. **Celebrate Wins** - Enjoy the animations!
5. **Daily Streaks** - Build consistency slowly
6. **Collapse Sections** - Reduce visual overwhelm
7. **Time Boxing** - Set realistic due times
8. **Categories** - Group similar tasks together

## 🐛 Support

This is a prototype/demo app. For issues or suggestions:
1. Check browser console for errors
2. Try clearing localStorage: `localStorage.clear()`
3. Refresh the page

## 📄 License

Free to use and modify for personal or commercial projects!

---

Made with 💜 for people with ADHD who want to stay organized without the overwhelm.

**Remember: Progress over perfection! 🚀**
