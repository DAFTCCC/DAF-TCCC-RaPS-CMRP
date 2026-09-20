# v4.1.2 — Unified Web + Android synchronization

- Established `/web` as the single FieldReady application source for both GitHub Pages and Android.
- Added an Android WebView wrapper using `WebViewAssetLoader` so the exact web app runs offline inside the APK.
- Added Gradle `syncWebAssets` to copy `/web` into the APK before every Android build.
- Added Android CSV/JSON export bridge to `Downloads/FieldReady` and file-picker support for JSON Restore.
- Added GitHub Actions for Android APK build and GitHub Pages deployment.
- Preserved the v4.1.1 web behavior: password gate, MAJCOM/base structure, study skills, full RaPS CMC, clocks/stopwatches, 5×5 failure workflow, and longitudinal participant comparison.
- Added explicit documentation that feature synchronization is not the same as cross-device record synchronization.
