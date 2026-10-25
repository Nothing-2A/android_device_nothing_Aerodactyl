#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from the custom device configuration.
$(call inherit-product, device/nothing/Aerodactyl/device-PacmanPro.mk)

# Inherit from the LineageOS configuration.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

PRODUCT_BRAND := Nothing
PRODUCT_DEVICE := PacmanPro
PRODUCT_MANUFACTURER := Nothing
PRODUCT_MODEL := A142P
PRODUCT_NAME := lineage_PacmanPro

PRODUCT_GMS_CLIENTID_BASE := android-nothing

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc="sys_mssi_64_ww_armv82-user 17 CP2A.260605.016 2610151824 release-keys" \
    BuildFingerprint=Nothing/PacmanPro/PacmanPro:17/CP2A.260605.016/2610151824:user/release-keys \
    BuildSystemFingerprint=alps/sys_mssi_64_64only_ww_armv82/mssi_64_64only_ww_armv82:17/CP2A.260605.016/2610151824:user/release-keys \
    DeviceName=PacmanPro \
    DeviceProduct=PacmanPro \
    SystemDevice=PacmanPro \
    SystemName=PacmanPro
