[app]

# (str) Title of your application
title = Youtube Downloader

# (str) Package name
package.name = youtubedownloader

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

#تفضل إعدادات ملف **`buildozer.spec`** جاهزة بالكامل ومُعدلة لتناسب تطبيقك وتتفادى أخطاء البناء:

```ini
[app]

# (str) Title of your application
title = Youtube Downloader

# (str) Package name
package.name = youtubedownloader

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,yt_dlp,certifi,openssl

# (list) Permissions
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API required.
android.minapi = 21

# (str) Android NDK version
android.ndk = 25b

# (list) The Android architectures to build for
android.archs = arm64-v8a

# (bool) Indicate whether the application should be fullscreen or not
fullscreen = 0

# (list) Orientation
orientation = portrait

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = ignore)
warn_on_root = 1
