# FieldReady synchronization architecture

## Release rule

`web/` is authoritative. Android is a native WebView shell around the exact same files.

Flow:

`web source` → `GitHub Pages`

`web source` → Gradle `syncWebAssets` → `Android assets/www` → `APK`

This eliminates the previous pattern where two separately edited applications drifted apart.

## What stays identical

Scoring, critical flags, timers, assessment stopwatches, participant IDs, timepoints, MAJCOM/base lists, study arms, longitudinal record logic, exports, failure taxonomy, and password gate all originate in the same JavaScript/HTML/CSS files.

## What is platform-specific

Android adds only the native shell, file picker, and export-to-Downloads bridge. It does not redefine clinical or study logic.

## Data synchronization boundary

Data are still local to each runtime. An APK install and a browser do not share `localStorage`. Use Backup/Restore for controlled transfer today. Use an authenticated backend for true cross-device data synchronization.
