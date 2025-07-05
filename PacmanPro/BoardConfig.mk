#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

# Include the common BoardConfig.
include device/nothing/Aerodactyl/BoardConfig-common.mk

# Bootloader
TARGET_BOOTLOADER_BOARD_NAME := PacmanPro

# Properties
TARGET_VENDOR_PROP += $(DEVICE_PATH)/PacmanPro/vendor.prop

# Inherit the proprietary files
include vendor/nothing/PacmanPro/BoardConfigVendor.mk
