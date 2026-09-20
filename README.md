# FieldReady APK BUILD v4.1.3

This package is the **Android APK build repository only**.

## What changed in v4.1.3

The prior workflow used `android-actions/setup-android@v3`. In September 2026, Google stopped serving the deprecated Android SDK `tools` package. That version of the action attempted to install `tools`, so the workflow failed during Android SDK setup with:

`Warning: Failed to find package 'tools'`

v4.1.3 updates the workflow to `android-actions/setup-android@v4`, explicitly installs only `platform-tools`, then installs the required Android 35 platform and build tools with `sdkmanager`.

## Build the APK

1. Extract this ZIP.
2. Upload **everything inside the extracted folder** to the root of the GitHub repository.
3. Commit the files to `main`.
4. Open **Actions**.
5. Select **Build FieldReady Android APK**.
6. Choose **Run workflow**.
7. After the workflow finishes, download the artifact named **FieldReady-Competency-Study-v4.1.3-APK**.
8. Extract the artifact ZIP to get `FieldReady-Competency-Study-v4.1.3.apk`.

The `/web` directory remains the single source for the FieldReady interface embedded in the Android application.
