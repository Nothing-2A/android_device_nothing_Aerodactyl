#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from the custom common configuration.
$(call inherit-product, device/nothing/Aerodactyl/device-common.mk)

# Init
$(call soong_config_set,libinit,vendor_init_lib,//$(LOCAL_PATH):init_nothing_pacmanpro)

# Overlays
PRODUCT_PACKAGES += \
    NothingWifiResPacman \
    SettingsOverlayPacmanPro

# Inherit the proprietary files
$(call inherit-product, vendor/nothing/PacmanPro/PacmanPro-vendor.mk)
