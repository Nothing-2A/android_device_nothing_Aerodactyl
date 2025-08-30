#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from the custom device configuration.
$(call inherit-product, device/nothing/Aerodactyl/device-PacmanPro.mk)

# Inherit from the YAAP configuration.
$(call inherit-product, vendor/yaap/config/common_full_phone.mk)

# YAAP Flags
TARGET_ENABLE_BLUR := false
PERF_ANIM_OVERRIDE := true

PRODUCT_BRAND := Nothing
PRODUCT_DEVICE := PacmanPro
PRODUCT_MANUFACTURER := Nothing
PRODUCT_MODEL := A142P
PRODUCT_NAME := yaap_PacmanPro

PRODUCT_GMS_CLIENTID_BASE := android-nothing

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc="sys_mssi_64_ww_armv82-user 15 AP3A.240905.015.A2 2504101524 release-keys" \
    BuildFingerprint=Nothing/PacmanPro/PacmanPro:15/AP3A.240905.015.A2/2504101524:user/release-keys \
    DeviceName=PacmanPro \
    DeviceProduct=PacmanPro \
    SystemDevice=PacmanPro \
    SystemName=PacmanPro
