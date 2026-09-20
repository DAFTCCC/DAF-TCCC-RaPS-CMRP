# FIELDREADY ANDROID APK BUILD REPOSITORY — v4.1.2

**Use this package when your goal is to build the Android `.apk`.**

Upload the **contents of this folder** to the root of a GitHub repository. Then run:

**GitHub → Actions → Build FieldReady Android APK → Run workflow**

The workflow builds the Android application from the included `/android` project and copies the included `/web` FieldReady source into the Android app so the APK matches the web version.

## Included
- `/android` — Android Studio / Gradle project
- `/web` — synchronized FieldReady web source embedded into the APK during build
- `/.github/workflows/build-android.yml` — APK build workflow
- `/tools` — synchronization verification

## Not included
- GitHub Pages deployment workflow. This package is for the APK build only.

Version: v4.1.2
