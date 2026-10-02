[app]

# (str) Title of your application
title = Youtube Downloader

# (str) Package name
package.name = youtubedownloader

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy,yt_dlp,certifi,openssl

# (list) Permissions
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# (int) Target Android API
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (str) Android NDK version
android.ndk = 25b

# (list) The Android architectures to build for
android.archs = arm64-v8a

# (bool) Fullscreen mode
fullscreen = 0

# (list) Orientation
orientation = portrait

[buildozer]

# (int) Log level
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
