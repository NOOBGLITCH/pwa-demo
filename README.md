
```markdown
# 🚀 Instant PWA DEMO Setup

This project transforms BrowserPlay TV into a high-performance **Progressive Web App (PWA)** that triggers the native Chrome install prompt instantly.

---

## 📁 File Structure
- `index.html` - UI with instant prompt logic.
- `manifest.json` - App metadata.
- `service-worker.js` - Fast-activation engine.
- `image.py` - Pillow-based icon generator.
- `image.png` - Source logo (any size will be fine).

---

## 🛠️ Step 1: Generate App Icons
The `image.py` script creates all required resolutions from your `image.png`.

**Install Pillow:**
```bash
pip3 install Pillow

```

**Run Generator:**

```bash
python3 image.py

```

*Generated sizes: 72x72, 96x96, 128x128, 144x144, 152x152, 192x192, 384x384, 512x512.*

---

## ⚡ Step 2: Make it Instantly Installable

This setup uses **Fast Activation Logic**:

1. **`skipWaiting()`**: Bypasses the browser's standard waiting period.
2. **`clients.claim()`**: Forces the Service Worker to take control of the page immediately.
3. **Maskable Icons**: Satisfies Chrome's high-quality PWA criteria.

---

## 🌟 Credits & Resources

* **PWA Generator Tool**: [pwagenerator.netlify.app](https://pwagenerator.netlify.app/)
* **GitHub Repo**: [opensource254/pwa-generator](https://github.com/opensource254/pwa-generator)
* **Community**: [r/PWA](https://www.reddit.com/r/PWA/)

---

## 💡 Pro Tips for Developers

> [!IMPORTANT]
> **Environment Compatibility:** Local "Classic 27" or legacy setups do not support modern PWA debugging. **GitHub Codespaces is not recommended** for this project due to Service Worker port limitations.

* **Dev Environment**: Use **CodeSandbox.io**. It provides the full HTTPS environment required for PWA prompts.
* **Production Hosting**: **Vercel** or **Netlify** are the best choices (Superior to GitHub Pages for PWAs).
* **Local Testing**: Always use `localhost`. PWA features are disabled on standard `http://`.

---

**Developed by NOOBGLITCH**

---


