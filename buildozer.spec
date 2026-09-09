[app]

# Lotto365 Kivy Android application
title = Lotto365
package.name = lotto365
package.domain = com.kym
source.dir = .
source.include_exts = py,wav,png,jpg,kv,atlas
version = 1.0.0

# Only the packages actually used by this program.
requirements = python3,kivy

orientation = portrait
fullscreen = 0

# Modern Android phones are normally ARM64.
android.archs = arm64-v8a

# Debug APK for installation on your phone.
android.debug_artifact = apk
android.release_artifact = aab

[buildozer]
log_level = 2
warn_on_root = 1
