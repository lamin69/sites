[app]

# (str) Title of your application
title = Lamine File Transfer LFT

# (str) Package name
package.name = laminefiletransfer

# (str) Package domain (needed for android/ios packaging)
package.domain = org.lft

# (str) Source code where the main.py file is located
source.dir = .

# (str) Source code where the main.py file is located
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to include (let empty to include all the files)
source.include_patterns = assets/*, icons/*

# (str) Application versioning (recommend using date format YYYY.MM.DD)
version = 2024.07.06

# (list) Application dependencies
requirements = python3,kivy==2.2.1,ftplib,paramiko==2.11.0,pysmb==1.2.8,pywebdav==0.9.8,aiohttp==3.8.4

# (list) Permissions required by your application
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (str) Supported screen orientations
orientation = portrait

# (str) Icon for the application
icon.filename = %(source.dir)s/assets/icon.png

# (str) Presplash image for the application
presplash.filename = %(source.dir)s/assets/presplash.png

# (int) Android API level to target
android.api = 30

# (int) Minimum API level (21 = Android 5.0)
android.minapi = 21

# (str) NDK version to use (use a version higher than 25 as per the environment support)
android.ndk = 25b

# (int) NDK API level to use
android.ndk_api = 21

# (str) Keystore for signing the APK (if needed for deployment)
android.release_keystore = %(source.dir)s/release.keystore
android.release_keyalias = mykey
android.release_keystore_password = password
android.release_keyalias_password = password

# (str) Architecture support
android.archs = armeabi-v7a, arm64-v8a, x86, x86_64

# (list) Patterns to exclude from the source distribution
source.exclude_exts = spec,md

# (bool) Enable logging
log_level = 2

# Additional Build Settings
# (str) Additional options for buildozer
buildozer_options = --debug

# (bool) Whether to include the system Python site packages
include_system_packages = False
