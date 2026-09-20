# Changelog

## v4.1.4 — APK validation repair
- Removed `.nojekyll` from the APK build's required-file validation.
- `.nojekyll` remains optional in the source tree but is not needed by Android.
- Preserved setup-android v4 / Android 35 build repair from v4.1.3.
- Bumped Android versionCode/versionName and artifact names to v4.1.4.


## v4.1.4 — Android build repair

- Fixed GitHub Actions failure caused by the retired Android SDK `tools` package.
- Replaced `android-actions/setup-android@v3` with `android-actions/setup-android@v4`.
- Explicitly limits setup action package installation to `platform-tools`.
- Installs `platforms;android-35` and `build-tools;35.0.0` directly with `sdkmanager`.
- Added JavaScript syntax checks before Gradle build.
- Added Gradle `--stacktrace` to make any future build failure easier to diagnose.
- Updated APK artifact/file names to v4.1.4.
- No study scoring, skill content, timers, longitudinal logic, or web UI behavior changed in this repair.